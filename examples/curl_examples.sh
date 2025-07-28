#!/bin/bash

# AvatarPyCor cURL 使用示例

BASE_URL="https://api.binrc.com"

echo "🎨 AvatarPyCor cURL 使用示例"
echo "================================"

# 1. 生成单个头像
echo -e "\n1️⃣ 生成单个头像:"
curl -X POST "${BASE_URL}/avatar/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "size": 300,
    "gender": "1"
  }' | jq '.'

# 2. 保存SVG头像
echo -e "\n2️⃣ 保存SVG头像:"
curl -X POST "${BASE_URL}/avatar/save" \
  -H "Content-Type: application/json" \
  -d '{
    "size": 280,
    "gender": "2",
    "format": "svg",
    "filename": "female_avatar"
  }' \
  --output "female_avatar.svg"

echo "✅ SVG头像已保存: female_avatar.svg"

# 3. 保存PNG头像
echo -e "\n3️⃣ 保存PNG头像:"
curl -X POST "${BASE_URL}/avatar/save" \
  -H "Content-Type: application/json" \
  -d '{
    "size": 400,
    "gender": "0",
    "format": "png",
    "filename": "random_avatar"
  }' \
  --output "random_avatar.png"

echo "✅ PNG头像已保存: random_avatar.png"

# 4. 批量保存SVG头像
echo -e "\n4️⃣ 批量保存SVG头像:"
curl -X POST "${BASE_URL}/avatar/save/batch" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 3,
    "size": 200,
    "gender": "1",
    "format": "svg"
  }' \
  --output "avatars_svg.zip"

echo "✅ 批量SVG头像已保存: avatars_svg.zip"

# 5. 批量保存PNG头像
echo -e "\n5️⃣ 批量保存PNG头像:"
curl -X POST "${BASE_URL}/avatar/save/batch" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 2,
    "size": 300,
    "gender": "2",
    "format": "png"
  }' \
  --output "avatars_png.zip"

echo "✅ 批量PNG头像已保存: avatars_png.zip"

# 6. 获取JSON数据
echo -e "\n6️⃣ 获取头像JSON数据:"
curl "${BASE_URL}/avatar/json?size=250&gender=0" | jq '.'

# 7. 测试接口
echo -e "\n7️⃣ 测试接口:"
curl "${BASE_URL}/test" | jq '.'

echo -e "\n🎉 示例运行完成！"
echo -e "\n📋 生成的文件:"
ls -la *.svg *.png *.zip 2>/dev/null || echo "没有生成文件" 