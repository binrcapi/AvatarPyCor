# AvatarPyCor - Python头像生成器

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

一个基于Python的头像生成器，支持随机生成个性化头像并导出SVG/PNG格式。

## 📋 目录

- [项目简介](#项目简介)
- [主要特性](#主要特性)
- [快速开始](#快速开始)
- [API使用](#api使用)
- [编程语言示例](#编程语言示例)
- [项目结构](#项目结构)
- [部署指南](#部署指南)
- [开发说明](#开发说明)
- [使用示例](#使用示例)
- [致谢](#致谢)
- [许可证](#许可证)

## 🎯 项目简介

AvatarPyCor 是一个用Python实现的头像生成器，支持随机生成各种风格的头像。项目基于原Vue.js版本的头像生成器进行Python化改造，提供了简洁的API接口和Web界面。

### ✨ 主要特性

- 🎨 **随机头像生成** - 支持多种图层组合和颜色搭配
- 👥 **性别区分** - 支持男性、女性、中性头像生成
- 🎯 **智能搭配** - 自动处理图层冲突和颜色协调
- 🌈 **丰富色彩** - 多种颜色主题，贴近黄种人肤色
- 📱 **多尺寸支持** - 支持100x100到400x400等多种尺寸
- 🔧 **API接口** - 提供RESTful API服务
- 🌐 **Web界面** - 简洁易用的Web操作界面
- 📦 **多格式导出** - 支持SVG和PNG格式
- 🚀 **容器化部署** - 支持Docker和Kubernetes部署

## 🚀 快速开始

### 环境要求

- Python 3.7+
- pip

### 安装依赖

```bash
# 克隆项目
git clone https://github.com/binrclab/AvatarPyCor.git
cd AvatarPyCor

# 安装简化版本依赖（推荐）
pip install -r requirements_simple.txt

# 或安装完整版本依赖
pip install -r requirements.txt
```

### 运行测试

```bash
python test.py
```

### 启动Web服务

```bash
python main.py
```

### 访问应用

启动后访问：http://localhost:5000

## 🌐 API使用

### 在线API服务

我们提供了在线API服务：https://api.binrc.com/avatar/

### API接口列表

| 接口 | 方法 | 描述 |
|------|------|------|
| `/avatar` | GET | 生成单个头像 |
| `/avatar/generate` | POST | 生成单个头像 |
| `/avatar/json` | GET | 获取头像JSON数据 |
| `/avatar/batch` | POST | 批量生成头像 |
| `/avatar/save` | POST | 保存单个头像文件 |
| `/avatar/save/batch` | POST | 批量保存头像文件 |
| `/test` | GET | 测试接口 |

### 详细接口说明

#### 1. 生成单个头像

```bash
curl -X POST "https://api.binrc.com/avatar/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "size": 280,
    "gender": "0"
  }'
```

**参数说明：**
- `size`: 头像尺寸 (100-400)
- `gender`: 性别类型
  - `"0"`: 随机
  - `"1"`: 男性
  - `"2"`: 女性

**响应示例：**
```json
{
  "success": true,
  "data": {
    "svg": "<svg width=\"280\" height=\"280\"...",
    "size": 280,
    "gender": "0"
  }
}
```

#### 2. 批量生成头像

```bash
curl -X POST "https://api.binrc.com/avatar/batch" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 5,
    "size": 200,
    "gender": "1"
  }'
```

**参数说明：**
- `amount`: 生成数量 (1-10)
- `size`: 头像尺寸
- `gender`: 性别类型

#### 3. 获取JSON格式头像数据

```bash
curl "https://api.binrc.com/avatar/json?size=280&gender=0"
```

#### 4. 保存单个头像文件

```bash
# 保存SVG格式
curl -X POST "https://api.binrc.com/avatar/save" \
  -H "Content-Type: application/json" \
  -d '{
    "size": 280,
    "gender": "0",
    "format": "svg",
    "filename": "my_avatar"
  }' \
  --output "my_avatar.svg"

# 保存PNG格式
curl -X POST "https://api.binrc.com/avatar/save" \
  -H "Content-Type: application/json" \
  -d '{
    "size": 280,
    "gender": "0",
    "format": "png",
    "filename": "my_avatar"
  }' \
  --output "my_avatar.png"
```

**参数说明：**
- `size`: 头像尺寸 (100-400)
- `gender`: 性别类型 ("0": 随机, "1": 男性, "2": 女性)
- `format`: 文件格式 ("svg" 或 "png")
- `filename`: 文件名（可选，默认为时间戳）

#### 5. 批量保存头像文件

```bash
# 批量保存SVG格式
curl -X POST "https://api.binrc.com/avatar/save/batch" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 5,
    "size": 200,
    "gender": "1",
    "format": "svg"
  }' \
  --output "avatars_svg.zip"

# 批量保存PNG格式
curl -X POST "https://api.binrc.com/avatar/save/batch" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 3,
    "size": 300,
    "gender": "2",
    "format": "png"
  }' \
  --output "avatars_png.zip"
```

**参数说明：**
- `amount`: 生成数量 (1-10)
- `size`: 头像尺寸
- `gender`: 性别类型
- `format`: 文件格式 ("svg" 或 "png")

## 💻 编程语言示例

### Python

```python
import requests

# 生成头像
response = requests.post("https://api.binrc.com/avatar/generate", json={
    "size": 280,
    "gender": "2"
})
result = response.json()

if result["success"]:
    svg_content = result["data"]["svg"]
    # 保存SVG文件
    with open("avatar.svg", "w") as f:
        f.write(svg_content)
```

### JavaScript

```javascript
// 生成头像
async function generateAvatar(size = 280, gender = "0") {
    const response = await fetch("https://api.binrc.com/avatar/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ size, gender })
    });
    return await response.json();
}

// 使用示例
generateAvatar(300, "2").then(result => {
    if (result.success) {
        console.log("头像SVG:", result.data.svg);
    }
});
```

### Golang

```go
package main

import (
    "fmt"
    "net/http"
    "bytes"
    "encoding/json"
)

// 生成头像
func generateAvatar(size int, gender string) (*AvatarResponse, error) {
    reqBody := map[string]interface{}{
        "size":   size,
        "gender": gender,
    }
    
    jsonData, _ := json.Marshal(reqBody)
    resp, err := http.Post("https://api.binrc.com/avatar/generate", 
        "application/json", bytes.NewBuffer(jsonData))
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()
    
    var result AvatarResponse
    json.NewDecoder(resp.Body).Decode(&result)
    return &result, nil
}

// 使用示例
func main() {
    result, err := generateAvatar(300, "2")
    if err == nil && result.Success {
        fmt.Println("头像SVG:", result.Data.SVG)
    }
}
```

### cURL

```bash
# 生成女性头像
curl -X POST "https://api.binrc.com/avatar/generate" \
  -H "Content-Type: application/json" \
  -d '{"size": 280, "gender": "2"}' \
  | jq '.data.svg' > female_avatar.svg

# 保存SVG头像
curl -X POST "https://api.binrc.com/avatar/save" \
  -H "Content-Type: application/json" \
  -d '{"size": 280, "gender": "2", "format": "svg"}' \
  --output "female_avatar.svg"

# 保存PNG头像
curl -X POST "https://api.binrc.com/avatar/save" \
  -H "Content-Type: application/json" \
  -d '{"size": 280, "gender": "2", "format": "png"}' \
  --output "female_avatar.png"
```

## 📁 项目结构

```
AvatarPyCor/
├── config/                 # 配置文件
│   ├── colors.py          # 颜色配置
│   └── layer_configs.py   # 图层配置
├── models/                 # 数据模型
│   ├── enums.py           # 枚举定义
│   └── dto.py             # 数据传输对象
├── utils/                  # 工具函数
│   └── random_utils.py    # 随机选择工具
├── resource/               # 素材资源
│   ├── Background/        # 背景素材
│   ├── Hair/             # 头发素材
│   ├── Eyes/             # 眼睛素材
│   └── ...               # 其他素材
├── static/                 # 静态文件
│   └── index.html         # Web界面
├── examples/               # 使用示例
│   ├── python_example.py  # Python示例
│   ├── javascript_example.js # JavaScript示例
│   ├── go_example.go      # Golang示例
│   ├── go.mod             # Go模块文件
│   ├── README_GO.md       # Go示例说明
│   └── curl_examples.sh   # cURL示例
├── k8s/                    # Kubernetes配置
│   ├── namespace.yaml     # 命名空间
│   ├── deployment.yaml    # 部署配置
│   ├── service.yaml       # 服务配置
│   ├── ingress.yaml       # 入口配置
│   └── ...               # 其他K8s配置
├── avatar_creator_simple.py # 头像生成核心逻辑
├── app.py                  # Flask应用
├── main.py                 # 主程序入口
├── test.py                 # 测试脚本
├── requirements.txt        # 完整依赖
├── requirements_simple.txt # 简化依赖
├── Dockerfile              # Docker配置
├── docker-compose.yml      # Docker Compose配置
├── deploy.sh               # 部署脚本
├── k8s-deploy.sh           # K8s部署脚本
└── README.md              # 项目说明
```

## 🚀 部署指南

### Docker部署

```bash
# 构建镜像
docker build -t avatar-generator .

# 运行容器
docker run -p 5000:5000 avatar-generator

# 或使用Docker Compose
docker-compose up -d
```

### Kubernetes部署

```bash
# 部署到K8s集群
./k8s-deploy.sh
```

### 生产环境部署

```bash
# 使用部署脚本
./deploy.sh
```

## 🎨 配置说明

### 图层配置

项目支持多种图层类型：
- **Base**: 头部基础
- **Hair**: 头发样式
- **Eyes**: 眼睛样式
- **Eyebrows**: 眉毛样式
- **Mouth**: 嘴巴样式
- **Ear**: 耳朵样式
- **Ear Ring**: 耳环装饰
- **Glasses**: 眼镜装饰
- **Headwear**: 头饰装饰
- **Hat**: 帽子装饰
- **Mask**: 面具装饰
- **Background**: 背景样式

### 颜色配置

- **Base**: 肤色配置，贴近黄种人
- **Hair**: 头发颜色配置
- **Background**: 背景颜色配置
- **其他图层**: 根据图层特性配置颜色

## 🔧 开发说明

### 添加新素材

1. 将SVG文件放入对应的`resource/`目录
2. 在`config/layer_configs.py`中添加配置
3. 更新颜色配置（如需要）

### 自定义配置

可以修改以下文件来自定义头像生成：
- `config/colors.py` - 颜色配置
- `config/layer_configs.py` - 图层配置
- `avatar_creator_simple.py` - 生成逻辑

## 📚 使用示例

### 运行Python示例

```bash
cd examples
python python_example.py
```

### 运行JavaScript示例

```bash
cd examples
node javascript_example.js
```

### 运行Golang示例

```bash
cd examples
go run go_example.go
```

### 运行cURL示例

```bash
cd examples
chmod +x curl_examples.sh
./curl_examples.sh
```

## 🙏 致谢

本项目基于 [wave-charts/avatar-gen](https://github.com/wave-charts/avatar-gen) 项目进行Python化改造。

**原项目信息：**
- 项目地址：https://github.com/wave-charts/avatar-gen
- 在线演示：https://avatar.oooo.so
- 许可证：MIT License
- 作者：wave-charts

感谢原项目作者提供的优秀设计和素材资源，本项目仅用于学习和研究目的。

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📞 联系方式

- 项目地址：https://github.com/binrclab/AvatarPyCor
- 在线API：https://api.binrc.com/avatar/
- 在线演示：https://avatar.binrc.com/ 