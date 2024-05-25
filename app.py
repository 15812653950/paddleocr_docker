from flask import Flask, request, jsonify

import cv2
from paddleocr import PaddleOCR
from werkzeug.utils import secure_filename
import paddle
import uuid
import os
from PIL import Image

app = Flask(__name__)
# 假设您有一个函数来获取安全的上传目录路径
upload_dir = 'png'  # 请替换为实际的上传目录路径
# 确保上传目录存在
os.makedirs(upload_dir, exist_ok=True)
global model_name
global model
global loaded_flag
loaded_flag = False


@app.route('/load_model', methods=['GET','POST'])
def load_model():
    # 离线加载 PaddleOCR 模型（支持多语言）
    global model
    global loaded_flag
    model = PaddleOCR(
        det_model_dir='model/det_model',  # 检测模型路径
        rec_model_dir='model/rec_model',  # 识别模型路径
        cls_model_dir='model/cls_model',  # 方向分类模型路径
        use_angle_cls=True,
        lang='ch'
    )
    loaded_flag =  True
    return jsonify({
        'model': 'loaded'
    })
@app.route('/', methods=['POST','GET'])
def index():
    return "baidu : paddleocr"

@app.route('/predict', methods=['POST'])
def predict():
    if loaded_flag:
        print("模型已启动")
    else:
        load_model()
    try:
        # Debugging info
        print("Request received")
        print("Headers:", request.headers)
        print("Form data:", request.form)
        print("Files:", request.files)
        
        if 'file' not in request.files:
            return jsonify({"code": 404, "msg": "No file part", "data": {}}), 404
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"code": 404, "msg": "No selected file", "data": {}}), 404

        # Debugging info
        print(f"File received: {file.filename}")
        # 生成 UUID 文件名并保存文件
        name = uuid.uuid4()
        filename = f"{name}.png"
        file.save(filename)
        result = model.ocr(filename, cls=True)
        predictions = []
        for res in result:
            for line in res:
                box_coords = line[0]
                text, score = line[1]
                xmin = min(point[0] for point in box_coords)
                ymin = min(point[1] for point in box_coords)
                xmax = max(point[0] for point in box_coords)
                ymax = max(point[1] for point in box_coords)

            # 创建预测结果字典并添加到列表中
                predictions.append({
                    "score": score,
                    "label": text,
                    "box": {
                        "xmin": xmin,
                        "ymin": ymin,
                        "xmax": xmax,
                        "ymax": ymax
                    }
                })

        # 打印或处理predictions列表
        print(predictions)
        os.remove(filename)
        return jsonify({"code": 200, "msg": "Success", "data": predictions}), 200

    except Exception as e:
        return jsonify({"code": 404, "msg": str(e), "data": {}}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
