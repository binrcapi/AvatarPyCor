#!/usr/bin/env python3
"""
AvatarPyCor Python 使用示例
"""

import requests
import json
import os
from typing import Optional

class AvatarGenerator:
    """头像生成器客户端"""
    
    def __init__(self, base_url: str = "https://api.binrc.com"):
        self.base_url = base_url.rstrip('/')
    
    def generate_avatar(self, size: int = 280, gender: str = "0") -> dict:
        """生成单个头像"""
        url = f"{self.base_url}/avatar/generate"
        data = {
            "size": size,
            "gender": gender
        }
        response = requests.post(url, json=data)
        return response.json()
    
    def save_avatar_svg(self, size: int = 280, gender: str = "0", filename: str = None) -> bool:
        """保存SVG头像"""
        url = f"{self.base_url}/avatar/save"
        data = {
            "size": size,
            "gender": gender,
            "format": "svg",
            "filename": filename or f"avatar_{int(time.time())}"
        }
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            # 保存文件
            with open(f"{data['filename']}.svg", "wb") as f:
                f.write(response.content)
            print(f"✅ SVG头像已保存: {data['filename']}.svg")
            return True
        else:
            print(f"❌ 保存失败: {response.text}")
            return False
    
    def save_avatar_png(self, size: int = 280, gender: str = "0", filename: str = None) -> bool:
        """保存PNG头像"""
        url = f"{self.base_url}/avatar/save"
        data = {
            "size": size,
            "gender": gender,
            "format": "png",
            "filename": filename or f"avatar_{int(time.time())}"
        }
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            # 保存文件
            with open(f"{data['filename']}.png", "wb") as f:
                f.write(response.content)
            print(f"✅ PNG头像已保存: {data['filename']}.png")
            return True
        else:
            print(f"❌ 保存失败: {response.text}")
            return False
    
    def batch_save_avatars(self, amount: int = 5, size: int = 280, gender: str = "0", format: str = "svg") -> bool:
        """批量保存头像"""
        url = f"{self.base_url}/avatar/save/batch"
        data = {
            "amount": amount,
            "size": size,
            "gender": gender,
            "format": format
        }
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            # 保存ZIP文件
            filename = f"avatars_{format}_{int(time.time())}.zip"
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"✅ 批量头像已保存: {filename}")
            return True
        else:
            print(f"❌ 批量保存失败: {response.text}")
            return False
    
    def get_avatar_json(self, size: int = 280, gender: str = "0") -> dict:
        """获取头像JSON数据"""
        url = f"{self.base_url}/avatar/json"
        params = {
            "size": size,
            "gender": gender
        }
        response = requests.get(url, params=params)
        return response.json()

def main():
    """主函数 - 演示各种用法"""
    print("🎨 AvatarPyCor Python 使用示例")
    print("=" * 50)
    
    # 初始化客户端
    generator = AvatarGenerator()
    
    # 1. 生成单个头像
    print("\n1️⃣ 生成单个头像:")
    result = generator.generate_avatar(300, "1")  # 300x300 男性头像
    if result.get("success"):
        print("✅ 头像生成成功")
        svg_content = result["data"]["svg"]
        print(f"📏 尺寸: {result['data']['size']}")
        print(f"👤 性别: {result['data']['gender']}")
        print(f"📄 SVG长度: {len(svg_content)} 字符")
    else:
        print(f"❌ 生成失败: {result.get('error')}")
    
    # 2. 保存SVG头像
    print("\n2️⃣ 保存SVG头像:")
    generator.save_avatar_svg(280, "2", "female_avatar")  # 女性头像
    
    # 3. 保存PNG头像
    print("\n3️⃣ 保存PNG头像:")
    generator.save_avatar_png(400, "0", "random_avatar")  # 随机头像
    
    # 4. 批量保存SVG头像
    print("\n4️⃣ 批量保存SVG头像:")
    generator.batch_save_avatars(3, 200, "1", "svg")  # 3个男性头像
    
    # 5. 批量保存PNG头像
    print("\n5️⃣ 批量保存PNG头像:")
    generator.batch_save_avatars(2, 300, "2", "png")  # 2个女性头像
    
    # 6. 获取JSON数据
    print("\n6️⃣ 获取头像JSON数据:")
    json_result = generator.get_avatar_json(250, "0")
    if json_result.get("success"):
        print("✅ JSON数据获取成功")
        print(f"📏 尺寸: {json_result['data']['size']}")
        print(f"👤 性别: {json_result['data']['gender']}")
    else:
        print(f"❌ 获取失败: {json_result.get('error')}")
    
    print("\n🎉 示例运行完成！")

if __name__ == "__main__":
    import time
    main() 