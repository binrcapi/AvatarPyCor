#!/usr/bin/env python3
"""
AvatarPyCor 启动脚本
"""

import os
import sys

def main():
    """主函数"""
    print("=" * 50)
    print("🎨 AvatarPyCor 头像生成器")
    print("=" * 50)
    
    # 检查资源目录
    if not os.path.exists('resource'):
        print("⚠️  警告: resource目录不存在")
        print("将使用默认SVG进行测试")
    else:
        print("✅ 找到resource目录")
    
    # 检查依赖
    try:
        import flask
        import flask_cors
        print("✅ Flask依赖已安装")
    except ImportError as e:
        print(f"❌ 缺少依赖: {e}")
        print("请运行: pip install flask flask-cors")
        sys.exit(1)
    
    print("\n🚀 启动服务器...")
    print("📱 访问地址: http://localhost:5000")
    print("🔧 API文档: http://localhost:5000/")
    print("🧪 测试接口: http://localhost:5000/test")
    print("\n按 Ctrl+C 停止服务器")
    print("=" * 50)
    
    # 启动Flask应用
    from app import app
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main() 