
# PaddleOCR + Flask Dockerized Application / 基于 PaddleOCR 和 Flask 的 Docker 化应用

This project demonstrates how to use PaddleOCR with Flask to create a Dockerized application that processes input images and outputs the bounding box coordinates, detected text, and associated probabilities.

这个项目演示了如何使用 PaddleOCR 和 Flask 创建一个 Docker 化的应用，该应用可以处理输入的图像并输出文字框的坐标、识别的文字及其概率。

## Table of Contents / 目录

- [Introduction / 简介](#introduction--简介)
- [Features / 特性](#features--特性)
- [Installation / 安装](#installation--安装)
- [Usage / 使用方法](#usage--使用方法)
- [API Endpoints / API 端点](#api-endpoints--api-端点)
- [Example / 示例](#example--示例)
- [Contributing / 贡献](#contributing--贡献)
- [License / 许可证](#license--许可证)

## Introduction / 简介

This project leverages PaddleOCR for optical character recognition (OCR) and Flask to create a web service. The service accepts an image, processes it using PaddleOCR, and returns the bounding box coordinates, recognized text, and the probabilities of the text recognition.

该项目利用 PaddleOCR 进行光学字符识别（OCR），并使用 Flask 创建一个 Web 服务。该服务接受图像，使用 PaddleOCR 处理图像，并返回文字框的坐标、识别的文字及其概率。

## Features / 特性

- **OCR with PaddleOCR**: Utilizes PaddleOCR to extract text from images.
- **Web Service with Flask**: Provides a RESTful API to interact with the OCR functionality.
- **Dockerized**: The application is containerized using Docker for easy deployment.

- **使用 PaddleOCR 进行 OCR**: 利用 PaddleOCR 从图像中提取文字。
- **使用 Flask 提供 Web 服务**: 提供一个 RESTful API 来与 OCR 功能进行交互。
- **Docker 化**: 使用 Docker 容器化应用，便于部署。

## Installation / 安装

### Prerequisites / 前提条件

- Docker
- Docker Compose

### Steps / 步骤

1. Clone the repository / 克隆仓库:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Build the Docker image / 构建 Docker 镜像:

    ```bash
    docker-compose build
    ```

3. Run the Docker container / 运行 Docker 容器:

    ```bash
    docker-compose up
    ```

## Usage / 使用方法

Once the Docker container is running, you can use the API to process images.

Docker 容器运行后，您可以使用 API 来处理图像。

### API Endpoints / API 端点

#### Load Model / 加载模型

- **Endpoint**: `/load_model`
- **Method**: `POST`
- **Description**: Load the PaddleOCR model. This should be done before making predictions.

- **端点**: `/load_model`
- **方法**: `POST`
- **描述**: 加载 PaddleOCR 模型。在进行预测之前应执行此操作。

#### Request Example / 请求示例:

```bash
curl -X POST http://localhost:5000/load_model
```

#### Predict / 预测

- **Endpoint**: `/predict`
- **Method**: `POST`
- **Content-Type**: `multipart/form-data`
- **Parameters**:
  - `file`: The image file to be processed.

- **端点**: `/predict`
- **方法**: `POST`
- **内容类型**: `multipart/form-data`
- **参数**:
  - `file`: 要处理的图像文件。

#### Response / 响应

- **Content-Type**: `application/json`
- **Body**:

    ```json
    {
      "boxes": [
        [x1, y1, x2, y2],
        [x3, y3, x4, y4],
        ...
      ],
      "text": [
        "recognized_text_1",
        "recognized_text_2",
        ...
      ],
      "probabilities": [
        prob1,
        prob2,
        ...
      ]
    }
    ```

## Example / 示例

To test the API, you can use `curl` or any other API testing tool.

要测试 API，您可以使用 `curl` 或任何其他 API 测试工具。

### Loading the Model / 加载模型

```bash
curl -X POST http://localhost:5000/load_model
```

### Predicting Text from an Image / 从图像中预测文字

```bash
curl -X POST http://localhost:5000/predict -F "file=@/path/to/your/image.png"
```

You should receive a JSON response containing the bounding box coordinates, recognized text, and probabilities.

您将收到一个 JSON 响应，其中包含文字框的坐标、识别的文字及其概率。

## Contributing / 贡献

We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) to learn how you can contribute.

我们欢迎贡献！请阅读我们的 [贡献指南](CONTRIBUTING.md) 了解如何做出贡献。

## License / 许可证

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

该项目根据 MIT 许可证授权。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

## File Structure / 文件结构

```plaintext
.
├── README.md
├── app.py
├── docker-compose.yml
├── Dockerfile
└── test.py
```

- `app.py`: The main Flask application file.
- `docker-compose.yml`: Docker Compose file to setup and run the application.
- `Dockerfile`: Dockerfile to build the application image.
- `test.py`: Script to test the application.

- `app.py`: 主 Flask 应用文件。
- `docker-compose.yml`: Docker Compose 文件，用于设置和运行应用。
- `Dockerfile`: 构建应用镜像的 Dockerfile。
- `test.py`: 测试应用的脚本。

## How It Works / 工作原理

1. **PaddleOCR**: The application uses PaddleOCR to detect and recognize text in the input images.
2. **Flask**: A lightweight WSGI web application framework used to create the RESTful API.
3. **Docker**: The application is containerized using Docker for ease of deployment and scaling.

1. **PaddleOCR**: 该应用使用 PaddleOCR 来检测和识别输入图像中的文字。
2. **Flask**: 轻量级 WSGI Web 应用框架，用于创建 RESTful API。
3. **Docker**: 使用 Docker 容器化应用，便于部署和扩展。

## Setup Details / 设置细节

### app.py

The `app.py` file contains the Flask application code which handles the incoming requests, processes the images using PaddleOCR, and returns the results.

`app.py` 文件包含处理传入请求、使用 PaddleOCR 处理图像并返回结果的 Flask 应用代码。

### docker-compose.yml

The `docker-compose.yml` file sets up the services required for the application, including the Flask application service.

`docker-compose.yml` 文件设置应用所需的服务，包括 Flask 应用服务。

### Dockerfile

The `Dockerfile` defines the environment for the Flask application, including all dependencies such as PaddleOCR.

`Dockerfile` 定义了 Flask 应用的环境，包括 PaddleOCR 等所有依赖项。

### test.py

The `test.py` script can be used to test the application locally before deploying it in a Docker container.

`test.py` 脚本可用于在将应用部署到 Docker 容器之前本地测试应用。

## Getting Started / 入门指南

1. Ensure you have Docker and Docker Compose installed.
2. Clone the repository and navigate to the project directory.
3. Build the Docker image and run the container using Docker Compose.
4. Use the provided API endpoint to process images and get OCR results.

1. 确保已安装 Docker 和 Docker Compose。
2. 克隆仓库并导航到项目目录。
3. 构建 Docker 镜像并使用 Docker Compose 运行容器。
4. 使用提供的 API 端点处理图像并获取 OCR 结果。

---

We hope you find this project useful and easy to set up. For any issues or contributions, please refer to the [Contributing](#contributing) section.

我们希望您发现这个项目有用且易于设置。如有任何问题或贡献，请参阅 [贡献](#contributing--贡献) 部分。
