# AvatarPyCor 部署指南

## 🚀 服务路径配置

AvatarPyCor 支持配置服务路径，便于在Ingress中进行路径转发。

### 环境变量

- `SERVICE_PATH`: 服务路径，默认为空（根路径）
- 示例: `SERVICE_PATH=/avatar-pycor`

### 访问路径

| 配置 | 主页 | API接口 | 测试接口 |
|------|------|---------|----------|
| 无路径 | `http://localhost:5000/` | `http://localhost:5000/avatar/json` | `http://localhost:5000/test` |
| `/avatar-pycor` | `http://localhost:5000/` | `http://localhost:5000/avatar-pycor/avatar/json` | `http://localhost:5000/avatar-pycor/test` |

## 🐳 Docker 部署

### 1. 构建镜像

```bash
# 使用服务路径
docker build -t avatar-generator:latest .

# 或指定服务路径
docker build --build-arg SERVICE_PATH=/avatar-pycor -t avatar-generator:latest .
```

### 2. 运行容器

```bash
# 无服务路径
docker run -d \
  --name avatar-generator \
  -p 5000:5000 \
  avatar-generator:latest

# 使用服务路径
docker run -d \
  --name avatar-generator \
  -p 5000:5000 \
  -e SERVICE_PATH=/avatar-pycor \
  avatar-generator:latest
```

### 3. 使用构建脚本

```bash
./build.sh
```

## ☸️ Kubernetes 部署

### 1. 应用配置

```bash
# 应用所有K8s配置
kubectl apply -f k8s/

# 或使用kustomize
kubectl apply -k k8s/
```

### 2. 验证部署

```bash
# 检查Pod状态
kubectl get pods -n avatar-generator

# 检查服务状态
kubectl get svc -n avatar-generator

# 检查Ingress状态
kubectl get ingress -n avatar-generator
```

### 3. 访问服务

- **主页**: https://api.binrc.com/
- **服务**: https://api.binrc.com/avatar-pycor/
- **测试**: https://api.binrc.com/avatar-pycor/test
- **API**: https://api.binrc.com/avatar-pycor/avatar/json

## 🔧 Ingress 配置

### Nginx Ingress 配置

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: avatar-generator-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /avatar-pycor$2
spec:
  rules:
  - host: api.binrc.com
    http:
      paths:
      - path: /avatar-pycor(/|$)(.*)
        pathType: Prefix
        backend:
          service:
            name: avatar-generator-service
            port:
              number: 80
```

### 路径重写规则

- 请求: `https://api.binrc.com/avatar-pycor/test`
- 转发: `http://avatar-generator-service:80/avatar-pycor/test`

## 🧪 测试

### 1. 本地测试

```bash
# 测试服务路径配置
python test_service_path.py

# 测试API接口
curl http://localhost:5000/avatar-pycor/test
curl http://localhost:5000/avatar-pycor/avatar/json?size=200&gender=0
```

### 2. 生产环境测试

```bash
# 测试主页
curl https://api.binrc.com/

# 测试服务
curl https://api.binrc.com/avatar-pycor/test

# 测试API
curl https://api.binrc.com/avatar-pycor/avatar/json?size=200&gender=0
```

## 📋 配置说明

### 环境变量

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| `SERVICE_PATH` | 空 | 服务路径前缀 |
| `FLASK_ENV` | production | Flask环境 |
| `PYTHONPATH` | /app | Python路径 |
| `FLASK_APP` | app.py | Flask应用文件 |

### 健康检查

- **路径**: `/avatar-pycor/test` (如果配置了服务路径)
- **路径**: `/test` (如果未配置服务路径)
- **端口**: 5000
- **间隔**: 30秒
- **超时**: 30秒

## 🔍 故障排除

### 1. 服务无法访问

```bash
# 检查Pod状态
kubectl describe pod -n avatar-generator

# 检查日志
kubectl logs -n avatar-generator -l app=avatar-generator

# 检查服务
kubectl describe svc -n avatar-generator avatar-generator-service
```

### 2. 路径转发问题

```bash
# 检查Ingress配置
kubectl describe ingress -n avatar-generator

# 检查Nginx配置
kubectl exec -n ingress-nginx deployment/ingress-nginx-controller -- nginx -t
```

### 3. 环境变量问题

```bash
# 检查ConfigMap
kubectl describe configmap -n avatar-generator avatar-generator-config

# 检查Pod环境变量
kubectl exec -n avatar-generator deployment/avatar-generator -- env | grep SERVICE_PATH
``` 