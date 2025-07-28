#!/bin/bash

# AvatarPyCor 构建脚本

set -e

echo "🚀 开始构建 AvatarPyCor 服务..."

# 检查Docker是否安装
if ! command -v docker &> /dev/null; then
    echo "❌ Docker 未安装，请先安装 Docker"
    exit 1
fi

# 设置变量
IMAGE_NAME="avatar-generator"
TAG="latest"
FULL_IMAGE_NAME="${IMAGE_NAME}:${TAG}"

echo "📦 构建 Docker 镜像: ${FULL_IMAGE_NAME}"

# 构建镜像
docker build -t ${FULL_IMAGE_NAME} .

if [ $? -eq 0 ]; then
    echo "✅ 镜像构建成功!"
    
    # 显示镜像信息
    echo "📋 镜像信息:"
    docker images ${FULL_IMAGE_NAME}
    
    # 询问是否运行容器
    read -p "🤔 是否立即运行容器? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🐳 启动容器..."
        docker run -d \
            --name avatar-generator \
            -p 5000:5000 \
            -e SERVICE_PATH=/avatar-pycor \
            --restart unless-stopped \
            ${FULL_IMAGE_NAME}
        
        echo "✅ 容器启动成功!"
        echo "🌐 访问地址:"
        echo "  - 主页: http://localhost:5000"
        echo "  - 服务: http://localhost:5000/avatar-pycor"
        echo "  - 测试: http://localhost:5000/avatar-pycor/test"
        echo "📊 容器状态:"
        docker ps | grep avatar-generator
    fi
else
    echo "❌ 镜像构建失败!"
    exit 1
fi 