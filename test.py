from paddleocr import PaddleOCR, draw_ocr
import cv2
from PIL import Image

import re

def parse_box_coords(coords_str):
    # 使用正则表达式匹配坐标
    matches = re.findall(r'\b\d+\.\d+\b', coords_str)
    
    # 将匹配的数字字符串转换为浮点数
    parsed_coords = [float(coord) for coord in matches]
    
    # 将坐标分为四个点
    box_coords = [parsed_coords[i:i+2] for i in range(0, len(parsed_coords), 2)]
    
    return box_coords
# 离线加载 PaddleOCR 模型（支持多语言）
ocr = PaddleOCR(
    det_model_dir='model/det_model',  # 检测模型路径
    rec_model_dir='model/rec_model',  # 识别模型路径
    cls_model_dir='model/cls_model',  # 方向分类模型路径
    use_angle_cls=True,
    lang='ch'
)


ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
img_path = '1.png'
result = ocr.ocr(img_path, cls=True)
print(result)
# for idx in range(len(result)):
#     res = result[idx]
#     for line in res:
#         print(line)
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
##result 

# [[[1231.0, 199.0], [1370.0, 199.0], [1370.0, 238.0], [1231.0, 238.0]], ('機電工程署', 0.9721844792366028)]
# [[[1273.0, 234.0], [1372.0, 234.0], [1372.0, 275.0], [1273.0, 275.0]], ('EMSD', 0.9723778963088989)]
# [[[954.0, 296.0], [1164.0, 296.0], [1164.0, 328.0], [954.0, 328.0]], ('收件日期Receipt date：', 0.9715615510940552)]
# [[[1237.0, 290.0], [1447.0, 277.0], [1449.0, 315.0], [1240.0, 328.0]], ('03-10-2023', 0.9690977334976196)]
# [[[756.0, 300.0], [906.0, 305.0], [905.0, 340.0], [755.0, 334.0]], ('本不必填寫', 0.9945353269577026)]


# # 显示结果
# from PIL import Image
# result = result[0]
# image = Image.open(img_path).convert('RGB')
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, txts, scores, font_path='fonts/HanaMinB.otf')
# im_show = Image.fromarray(im_show)
# im_show.save('result.jpg')