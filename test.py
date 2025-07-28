#!/usr/bin/env python3
"""
独立的简化测试脚本 - 不依赖任何外部包
"""

import os
import sys

# 导入简化版头像生成器
from avatar_creator_simple import SimpleAvatarCreator, CreateAvatarDto, GenderType

def test_avatar_creation():
    """测试头像生成"""
    print("开始测试头像生成...")
    
    # 创建tmp目录
    tmp_dir = 'tmp'
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    
    # 初始化头像生成器
    creator = SimpleAvatarCreator()
    
    # 测试配置
    config = CreateAvatarDto(
        renderer="0",  # SVG
        amount=1,
        size=280,
        gender=GenderType.UNSET
    )
    
    try:
        # 生成头像
        svg_content = creator.create_one(config)
        
        # 保存到tmp文件夹
        file_path = os.path.join(tmp_dir, 'test_avatar_simple.svg')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        print("✅ 头像生成成功！")
        print(f"SVG内容长度: {len(svg_content)} 字符")
        print(f"文件已保存为: {file_path}")
        
        # 显示SVG内容的前100个字符
        print(f"SVG预览: {svg_content[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ 头像生成失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_different_genders():
    """测试不同性别"""
    print("\n测试不同性别...")
    
    # 创建tmp目录
    tmp_dir = 'tmp'
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    
    creator = SimpleAvatarCreator()
    
    genders = [
        (GenderType.UNSET, "随机"),
        (GenderType.MALE, "男性"),
        (GenderType.FEMALE, "女性")
    ]
    
    for gender, name in genders:
        try:
            config = CreateAvatarDto(
                renderer="0",
                amount=1,
                size=280,
                gender=gender
            )
            
            svg_content = creator.create_one(config)
            
            filename = f'test_avatar_{name}_simple.svg'
            file_path = os.path.join(tmp_dir, filename)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            
            print(f"✅ {name}头像生成成功: {file_path}")
            
        except Exception as e:
            print(f"❌ {name}头像生成失败: {e}")

def test_different_sizes():
    """测试不同尺寸"""
    print("\n测试不同尺寸...")
    
    # 创建tmp目录
    tmp_dir = 'tmp'
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    
    creator = SimpleAvatarCreator()
    sizes = [100, 200, 400]
    
    for size in sizes:
        try:
            config = CreateAvatarDto(
                renderer="0",
                amount=1,
                size=size,
                gender=GenderType.UNSET
            )
            
            svg_content = creator.create_one(config)
            
            filename = f'test_avatar_{size}x{size}_simple.svg'
            file_path = os.path.join(tmp_dir, filename)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            
            print(f"✅ {size}x{size} 头像生成成功: {file_path}")
            
        except Exception as e:
            print(f"❌ {size}x{size} 头像生成失败: {e}")

def test_multiple_avatars():
    """测试生成多个头像"""
    print("\n测试生成多个头像...")
    
    # 创建tmp目录
    tmp_dir = 'tmp'
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    
    creator = SimpleAvatarCreator()
    
    try:
        for i in range(5):
            config = CreateAvatarDto(
                renderer="0",
                amount=1,
                size=280,
                gender=GenderType.UNSET
            )
            
            svg_content = creator.create_one(config)
            
            filename = f'multiple_avatar_{i+1}_simple.svg'
            file_path = os.path.join(tmp_dir, filename)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            
            print(f"✅ 头像 {i+1} 生成成功: {file_path}")
        
        print("✅ 批量生成测试完成！")
        
    except Exception as e:
        print(f"❌ 批量生成失败: {e}")

def main():
    """主函数"""
    print("=" * 50)
    print("AvatarPyCor 独立简化测试脚本")
    print("=" * 50)
    
    # 检查资源目录
    if not os.path.exists('resource'):
        print("⚠️  警告: resource目录不存在，将使用默认SVG")
        print("请将Vue项目的resource目录复制到当前目录")
    else:
        print("✅ 找到resource目录")
    
    # 创建tmp目录
    tmp_dir = 'tmp'
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
        print(f"✅ 创建tmp目录: {tmp_dir}")
    else:
        print(f"✅ 找到tmp目录: {tmp_dir}")
    
    # 运行测试
    success = test_avatar_creation()
    
    if success:
        test_different_genders()
        test_different_sizes()
        test_multiple_avatars()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ 所有测试完成！")
        print(f"📁 生成的文件在 {tmp_dir} 目录:")
        for file in os.listdir(tmp_dir):
            if file.endswith('_simple.svg'):
                print(f"  - {file}")
    else:
        print("❌ 测试失败！")
    print("=" * 50)

if __name__ == '__main__':
    main() 