#!/usr/bin/env python3
"""
测试SERVICE_PATH变量注入功能
"""

import os
import requests
import json

def test_service_path_injection():
    """测试SERVICE_PATH变量注入"""
    print("🧪 测试SERVICE_PATH变量注入")
    print("=" * 50)
    
    # 测试不同的SERVICE_PATH配置
    test_configs = [
        {'SERVICE_PATH': '', 'description': '无服务路径'},
        {'SERVICE_PATH': '/avatar-pycor', 'description': '有服务路径'},
        {'SERVICE_PATH': '/test-service', 'description': '自定义服务路径'}
    ]
    
    for config in test_configs:
        print(f"\n📋 测试配置: {config['description']}")
        print(f"SERVICE_PATH: '{config['SERVICE_PATH']}'")
        
        # 设置环境变量
        os.environ['SERVICE_PATH'] = config['SERVICE_PATH']
        
        try:
            # 启动服务（这里只是模拟，实际需要启动Flask服务）
            print("🌐 访问主页...")
            
            # 模拟HTML内容注入
            html_template = '''
            <!DOCTYPE html>
            <html>
            <head><title>Test</title></head>
            <body>
            <script>
                // 注入的服务路径
                window.SERVICE_PATH = "{service_path}";
                
                // 测试函数
                function getServicePrefix() {{
                    if (window.SERVICE_PATH) {{
                        console.log(`从环境变量获取服务前缀: "${{window.SERVICE_PATH}}"`);
                        return window.SERVICE_PATH;
                    }}
                    return '';
                }}
                
                function buildApiUrl(endpoint) {{
                    const prefix = getServicePrefix();
                    const fullUrl = `${{prefix}}${{endpoint}}`;
                    console.log(`构建API URL: "${{fullUrl}}"`);
                    return fullUrl;
                }}
                
                // 测试
                console.log('=== 测试结果 ===');
                console.log('window.SERVICE_PATH:', window.SERVICE_PATH);
                console.log('getServicePrefix():', getServicePrefix());
                console.log('buildApiUrl("/test"):', buildApiUrl('/test'));
                console.log('buildApiUrl("/avatar/json"):', buildApiUrl('/avatar/json'));
            </script>
            </body>
            </html>
            '''
            
            # 注入SERVICE_PATH
            html_content = html_template.format(service_path=config['SERVICE_PATH'])
            
            print("✅ HTML内容已注入SERVICE_PATH变量")
            print(f"注入的变量: window.SERVICE_PATH = '{config['SERVICE_PATH']}'")
            
            # 模拟JavaScript执行结果
            if config['SERVICE_PATH']:
                expected_url = f"{config['SERVICE_PATH']}/avatar/json"
                print(f"预期API URL: '{expected_url}'")
            else:
                expected_url = "/avatar/json"
                print(f"预期API URL: '{expected_url}'")
                
        except Exception as e:
            print(f"❌ 测试失败: {e}")
    
    print("\n🎉 测试完成！")

def test_environment_variables():
    """测试环境变量读取"""
    print("\n🔧 环境变量测试:")
    print(f"当前SERVICE_PATH: '{os.getenv('SERVICE_PATH', '未设置')}'")
    
    # 设置测试环境变量
    test_paths = ['', '/avatar-pycor', '/test-service']
    
    for path in test_paths:
        os.environ['SERVICE_PATH'] = path
        print(f"设置SERVICE_PATH='{path}' -> 读取结果: '{os.getenv('SERVICE_PATH', '未设置')}'")

if __name__ == "__main__":
    test_environment_variables()
    test_service_path_injection() 