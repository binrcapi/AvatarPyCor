# AvatarPyCor Golang 使用示例

## 快速开始

### 1. 环境要求

- Go 1.21 或更高版本
- 网络连接（用于访问API）

### 2. 运行示例

```bash
cd examples
go run go_example.go
```

### 3. 编译可执行文件

```bash
cd examples
go build -o avatar-generator go_example.go
./avatar-generator
```

## 功能特性

### 主要功能

1. **生成单个头像** - 获取SVG格式的头像数据
2. **保存SVG头像** - 下载并保存SVG格式文件
3. **保存PNG头像** - 下载并保存PNG格式文件（需要服务端支持）
4. **批量保存头像** - 批量生成并打包下载
5. **获取JSON数据** - 获取头像的元数据信息
6. **API连接测试** - 测试API服务是否可用

### 参数说明

- `size`: 头像尺寸 (100-400像素)
- `gender`: 性别类型
  - `"0"`: 随机性别
  - `"1"`: 男性
  - `"2"`: 女性
- `format`: 文件格式
  - `"svg"`: SVG矢量格式
  - `"png"`: PNG位图格式

## 代码示例

### 基本用法

```go
package main

import (
    "fmt"
    "log"
)

func main() {
    // 创建客户端
    generator := NewAvatarGenerator("https://api.binrc.com")
    
    // 生成头像
    result, err := generator.GenerateAvatar(300, "1")
    if err != nil {
        log.Fatal("生成失败:", err)
    }
    
    if result.Success {
        fmt.Printf("头像生成成功，尺寸: %d\n", result.Data.Size)
        // 保存SVG文件
        err = os.WriteFile("avatar.svg", []byte(result.Data.SVG), 0644)
        if err != nil {
            log.Fatal("保存失败:", err)
        }
    }
}
```

### 保存文件示例

```go
// 保存SVG头像
err := generator.SaveAvatar(280, "2", "svg", "female_avatar")
if err != nil {
    log.Printf("保存SVG失败: %v", err)
}

// 保存PNG头像
err = generator.SaveAvatar(400, "0", "png", "random_avatar")
if err != nil {
    log.Printf("保存PNG失败: %v", err)
}
```

### 批量生成示例

```go
// 批量保存5个SVG头像
err := generator.BatchSaveAvatars(5, 200, "1", "svg")
if err != nil {
    log.Printf("批量保存失败: %v", err)
}
```

## 错误处理

示例代码包含了完整的错误处理：

```go
result, err := generator.GenerateAvatar(300, "1")
if err != nil {
    // 网络错误或其他系统错误
    log.Printf("请求失败: %v", err)
    return
}

if !result.Success {
    // API返回的业务错误
    log.Printf("生成失败: %s", result.Error)
    return
}

// 成功处理
fmt.Println("头像生成成功")
```

## 自定义配置

### 修改API地址

```go
// 使用自定义API地址
generator := NewAvatarGenerator("http://localhost:5000")
```

### 修改超时时间

```go
// 在NewAvatarGenerator中修改Client的Timeout
generator := &AvatarGenerator{
    BaseURL: "https://api.binrc.com",
    Client:  &http.Client{Timeout: 60 * time.Second}, // 60秒超时
}
```

## 输出示例

运行示例后的典型输出：

```
🎨 AvatarPyCor Golang 使用示例
================================

0️⃣ 测试API连接:
✅ API测试成功: {"status":"success","message":"AvatarPyCor API is running!"}

1️⃣ 生成单个头像:
✅ 头像生成成功
📏 尺寸: 300
👤 性别: 1
📄 SVG长度: 2847 字符

2️⃣ 保存SVG头像:
✅ SVG头像已保存: female_avatar.svg

3️⃣ 保存PNG头像:
✅ PNG头像已保存: random_avatar.png

4️⃣ 批量保存SVG头像:
✅ 批量SVG头像已保存: avatars_svg_1703123456.zip

5️⃣ 批量保存PNG头像:
✅ 批量PNG头像已保存: avatars_png_1703123457.zip

6️⃣ 获取头像JSON数据:
✅ JSON数据获取成功
📏 尺寸: 250
👤 性别: 0

🎉 示例运行完成！

📋 生成的文件:
  female_avatar.svg (2847 bytes)
  random_avatar.png (15678 bytes)
  avatars_svg_1703123456.zip (12456 bytes)
  avatars_png_1703123457.zip (23456 bytes)
```

## 注意事项

1. **PNG格式支持**: PNG格式需要服务端安装`cairosvg`库
2. **文件权限**: 确保程序有写入当前目录的权限
3. **网络连接**: 需要稳定的网络连接访问API
4. **错误处理**: 建议在生产环境中添加更详细的错误处理逻辑
5. **并发安全**: 当前实现是线程安全的，可以并发使用

## 依赖说明

本示例只使用了Go标准库，无需安装额外的依赖包：

- `net/http` - HTTP客户端
- `encoding/json` - JSON处理
- `bytes` - 字节缓冲区
- `io` - 输入输出操作
- `os` - 文件系统操作
- `time` - 时间处理
- `strings` - 字符串处理 