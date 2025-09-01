#!/bin/bash

# AvatarPyCor Kubernetes 部署脚本

set -e

echo "🚀 开始部署 AvatarPyCor 到 Kubernetes..."

# 检查kubectl是否安装
if ! command -v kubectl &> /dev/null; then
    echo "❌ kubectl 未安装，请先安装 kubectl"
    exit 1
fi

# 检查kustomize是否安装
if ! command -v kustomize &> /dev/null; then
    echo "⚠️  kustomize 未安装，使用 kubectl apply"
    # 使用kubectl直接应用
    kubectl apply -f k8s/namespace.yaml
    kubectl apply -f k8s/configmap.yaml
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    kubectl apply -f k8s/ingress.yaml
    kubectl apply -f k8s/hpa.yaml
else
    echo "📦 使用 kustomize 部署..."
    kustomize build k8s/ | kubectl apply -f -
fi

echo "⏳ 等待部署完成..."
kubectl wait --for=condition=available --timeout=300s deployment/avatar-pycor -n avatar-pycor

echo "✅ 部署完成！"
echo ""
echo "📋 查看状态:"
echo "  kubectl get pods -n avatar-generator"
echo "  kubectl get svc -n avatar-generator"
echo "  kubectl get ingress -n avatar-generator"
echo ""
echo "📊 查看日志:"
echo "  kubectl logs -f deployment/avatar-generator -n avatar-generator"
echo ""
echo "🌐 访问服务:"
echo "  集群内: kubectl port-forward svc/avatar-generator-service 8080:80 -n avatar-generator"
echo "  然后访问: http://localhost:8080" 