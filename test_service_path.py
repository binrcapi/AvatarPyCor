#!/usr/bin/env python3
"""
测试服务路径配置
"""

import requests
import json
import os

def test_service_path():
    """测试服务路径配置"""
    # 测试不同的服务路径
    test_urls = [
        "http://localhost:5000/",
        "http://localhost:5000/avatar-pycor/",
        "http://localhost:5000/avatar-pycor/test",
        "http://localhost:5000/avatar-pycor/avatar/json?size=200&gender=0"
    ]
    
    print("🧪 测试服务路径配置")
    print("=" * 50)
    
    for url in test_urls:
        print(f"\n测试 URL: {url}")
        try:
            response = requests.get(url, timeout=10)
            print(f"状态码: {response.status_code}")
            
            if response.status_code == 200:
                if 'application/json' in response.headers.get('content-type', ''):
                    data = response.json()
                    print(f"响应: {json.dumps(data, indent=2, ensure_ascii=False)}")
                else:
                    print(f"响应类型: {response.headers.get('content-type', 'unknown')}")
                    print(f"响应长度: {len(response.content)} 字符")
            else:
                print(f"错误响应: {response.text}")
                
        except Exception as e:
            print(f"❌ 请求失败: {e}")
    
    print("\n🎉 测试完成！")

def test_environment():
    """测试环境变量配置"""
    print("\n🔧 环境变量配置:")
    print(f"SERVICE_PATH: {os.getenv('SERVICE_PATH', '未设置')}")
    print(f"FLASK_APP: {os.getenv('FLASK_APP', '未设置')}")
    print(f"FLASK_ENV: {os.getenv('FLASK_ENV', '未设置')}")

if __name__ == "__main__":
    test_environment()
    test_service_path() 