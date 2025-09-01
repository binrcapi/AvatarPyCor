#!/bin/bash

# AvatarPyCor 部署脚本

set -e

echo "🚀 开始部署 AvatarPyCor..."

# 检查Docker是否安装
if ! command -v docker &> /dev/null; then
    echo "❌ Docker 未安装，请先安装 Docker"
    exit 1
fi

# 构建Docker镜像
echo "📦 构建 Docker 镜像..."
docker build -t registry.cn-shanghai.aliyuncs.com/binrchq/avatar-pycor:latest .

# 推送镜像到Docker Hub（可选）
if [ "$1" = "--push" ]; then
    echo "📤 推送镜像到 Docker Hub..."
    docker push registry.cn-shanghai.aliyuncs.com/binrchq/avatar-pycor:latest
fi

# 使用Docker Compose启动服务
echo "🏃 启动服务..."
docker-compose up -d

echo "✅ 部署完成！"
echo "🌐 访问地址: http://localhost:5000"
echo "📊 健康检查: http://localhost:5000/test"
echo ""
echo "📋 常用命令:"
echo "  查看日志: docker-compose logs -f"
echo "  停止服务: docker-compose down"
echo "  重启服务: docker-compose restart" 