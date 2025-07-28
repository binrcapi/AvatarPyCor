#!/usr/bin/env python3
"""
简化版Flask应用 - 不依赖外部图像处理库
"""

import os
import sys
import time

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import io
import zipfile
import base64
from typing import List

# 导入简化版头像生成器
from avatar_creator_simple import SimpleAvatarCreator, CreateAvatarDto, GenderType, RenderType

app = Flask(__name__)
CORS(app)

# 初始化头像生成器
avatar_creator = SimpleAvatarCreator()

@app.route('/avatar')
def index():
    """首页"""
    return send_file('static/index.html')

@app.route('/avatar/one')
def create_avatar():
    """生成单个头像 (GET方式)"""
    try:
        # 获取查询参数
        renderer = request.args.get('renderer', 'svg')
        amount = int(request.args.get('amount', 1))
        size = int(request.args.get('size', 280))
        gender = request.args.get('gender', '0')
        
        # 转换参数
        render_type = RenderType.SVG if renderer == 'svg' else RenderType.JPEG
        gender_type = GenderType.UNSET
        if gender == '1':
            gender_type = GenderType.MALE
        elif gender == '2':
            gender_type = GenderType.FEMALE
        
        # 创建配置
        config = CreateAvatarDto(
            renderer=render_type,
            amount=amount,
            size=size,
            gender=gender_type
        )
        
        # 生成头像
        svg_content = avatar_creator.create_one(config)
        
        if render_type == RenderType.SVG:
            return svg_content, 200, {'Content-Type': 'image/svg+xml'}
        else:
            # 简化版本只返回SVG，不转换为PNG
            return svg_content, 200, {'Content-Type': 'image/svg+xml'}
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/avatar/generate', methods=['POST'])
def generate_avatar():
    """生成单个头像 (POST方式)"""
    try:
        data = request.get_json() or {}
        
        size = int(data.get('size', 280))
        gender = data.get('gender', '0')
        
        # 转换性别参数
        gender_type = GenderType.UNSET
        if gender == '1':
            gender_type = GenderType.MALE
        elif gender == '2':
            gender_type = GenderType.FEMALE
        
        # 创建配置
        config = CreateAvatarDto(
            renderer=RenderType.SVG,
            amount=1,
            size=size,
            gender=gender_type
        )
        
        # 生成头像
        svg_content = avatar_creator.create_one(config)
        
        return jsonify({
            'success': True,
            'data': {
                'svg': svg_content,
                'size': size,
                'gender': gender
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/avatar/batch', methods=['POST'])
def create_batch_avatars():
    """批量生成头像"""
    try:
        data = request.get_json() or {}
        
        amount = int(data.get('amount', 5))
        size = int(data.get('size', 280))
        gender = data.get('gender', '0')
        
        # 限制生成数量
        if amount > 10:
            amount = 10
        if amount < 1:
            amount = 1
        
        # 转换性别参数
        gender_type = GenderType.UNSET
        if gender == '1':
            gender_type = GenderType.MALE
        elif gender == '2':
            gender_type = GenderType.FEMALE
        
        # 创建配置
        config = CreateAvatarDto(
            renderer=RenderType.SVG,
            amount=amount,
            size=size,
            gender=gender_type
        )
        
        # 创建ZIP文件
        zip_buffer = io.BytesIO()
        
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for i in range(amount):
                # 生成头像
                svg_content = avatar_creator.create_one(config)
                
                # 添加SVG文件到ZIP
                zip_file.writestr(f'avatar_{i+1}.svg', svg_content)
        
        zip_buffer.seek(0)
        
        return send_file(
            zip_buffer,
            mimetype='application/zip',
            as_attachment=True,
            download_name='avatars.zip'
        )
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/avatar/json')
def create_avatar_json():
    """生成头像并返回JSON格式"""
    try:
        # 获取查询参数
        size = int(request.args.get('size', 280))
        gender = request.args.get('gender', '0')
        
        # 转换性别参数
        gender_type = GenderType.UNSET
        if gender == '1':
            gender_type = GenderType.MALE
        elif gender == '2':
            gender_type = GenderType.FEMALE
        
        # 创建配置
        config = CreateAvatarDto(
            renderer=RenderType.SVG,
            amount=1,
            size=size,
            gender=gender_type
        )
        
        # 生成头像
        svg_content = avatar_creator.create_one(config)
        
        return jsonify({
            'success': True,
            'data': {
                'svg': svg_content,
                'size': size,
                'gender': gender
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/avatar/save', methods=['POST'])
def save_avatar():
    """保存头像为文件"""
    try:
        data = request.get_json() or {}
        
        size = int(data.get('size', 280))
        gender = data.get('gender', '0')
        format_type = data.get('format', 'svg')  # svg 或 png
        filename = data.get('filename', f'avatar_{int(time.time())}')
        
        # 转换性别参数
        gender_type = GenderType.UNSET
        if gender == '1':
            gender_type = GenderType.MALE
        elif gender == '2':
            gender_type = GenderType.FEMALE
        
        # 创建配置
        config = CreateAvatarDto(
            renderer=RenderType.SVG,
            amount=1,
            size=size,
            gender=gender_type
        )
        
        # 生成头像
        svg_content = avatar_creator.create_one(config)
        
        if format_type.lower() == 'png':
            # 转换为PNG（需要安装cairosvg）
            try:
                import cairosvg
                png_data = cairosvg.svg2png(bytestring=svg_content.encode('utf-8'))
                return send_file(
                    io.BytesIO(png_data),
                    mimetype='image/png',
                    as_attachment=True,
                    download_name=f'{filename}.png'
                )
            except ImportError:
                return jsonify({
                    'success': False,
                    'error': 'PNG conversion requires cairosvg. Please install: pip install cairosvg'
                }), 400
        else:
            # 返回SVG文件
            return send_file(
                io.BytesIO(svg_content.encode('utf-8')),
                mimetype='image/svg+xml',
                as_attachment=True,
                download_name=f'{filename}.svg'
            )
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/avatar/save/batch', methods=['POST'])
def save_batch_avatars():
    """批量保存头像"""
    try:
        data = request.get_json() or {}
        
        amount = int(data.get('amount', 5))
        size = int(data.get('size', 280))
        gender = data.get('gender', '0')
        format_type = data.get('format', 'svg')
        
        # 限制生成数量
        if amount > 10:
            amount = 10
        if amount < 1:
            amount = 1
        
        # 转换性别参数
        gender_type = GenderType.UNSET
        if gender == '1':
            gender_type = GenderType.MALE
        elif gender == '2':
            gender_type = GenderType.FEMALE
        
        # 创建配置
        config = CreateAvatarDto(
            renderer=RenderType.SVG,
            amount=amount,
            size=size,
            gender=gender_type
        )
        
        # 创建ZIP文件
        zip_buffer = io.BytesIO()
        
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for i in range(amount):
                # 生成头像
                svg_content = avatar_creator.create_one(config)
                
                if format_type.lower() == 'png':
                    try:
                        import cairosvg
                        png_data = cairosvg.svg2png(bytestring=svg_content.encode('utf-8'))
                        zip_file.writestr(f'avatar_{i+1}.png', png_data)
                    except ImportError:
                        return jsonify({
                            'success': False,
                            'error': 'PNG conversion requires cairosvg. Please install: pip install cairosvg'
                        }), 400
                else:
                    zip_file.writestr(f'avatar_{i+1}.svg', svg_content)
        
        zip_buffer.seek(0)
        
        return send_file(
            zip_buffer,
            mimetype='application/zip',
            as_attachment=True,
            download_name=f'avatars_{format_type}.zip'
        )
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/test')
def test():
    """测试接口"""
    return jsonify({
        'status': 'success',
        'message': 'AvatarPyCor API is running!',
        'endpoints': [
            'GET /avatar - 生成单个头像',
            'GET /avatar/json - 生成头像JSON',
            'POST /avatar/generate - 生成单个头像(POST)',
            'POST /avatar/batch - 批量生成头像',
            'POST /avatar/save - 保存单个头像文件',
            'POST /avatar/save/batch - 批量保存头像文件',
            'GET /test - 测试接口'
        ]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 