from paddleocr import PaddleOCR

# 创建 PaddleOCR 实例
ocr = PaddleOCR(det_model_dir='model/det_model', rec_model_dir='model/rec_model')

# 使用 download 方法下载检测和识别模型
# ocr.download()