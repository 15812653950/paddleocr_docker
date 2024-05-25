# 使用官方 PaddlePaddle GPU 镜像作为基础镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends libgl1-mesa-glx libgomp1 libglib2.0-0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip cache purge

RUN pip install shapely -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install scikit-image -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install imgaug -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pyclipper -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install lmdb -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install tqdm -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install rapidfuzz -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install opencv-contrib-python -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install cython -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install Pillow>=10.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pyyaml -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install common -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install dual -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install tight -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install data -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install prox -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install distributed -i https://pypi.tuna.tsinghua.edu.cn/simple


RUN pip install Flask -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install Pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install paddlepaddle==2.6.1 -i https://mirror.baidu.com/pypi/simple
# RUN pip install paddle==1.0.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install paddleocr==2.7.3 -i https://pypi.tuna.tsinghua.edu.cn/simple


# 复制应用程序文件和目录到容器的工作目录中
COPY . /app

# 暴露端口
EXPOSE 5000

# 运行 Flask 应用
CMD ["python", "app.py"]
