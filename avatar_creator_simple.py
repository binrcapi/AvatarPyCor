#!/usr/bin/env python3
"""
简化版头像生成器 - 不依赖外部图像处理库
"""

import os
import re
import random
from typing import List, Dict, Any, Optional, Callable

# 简化的枚举定义
class RenderType:
    SVG = "0"
    JPEG = "1"
    BASE64 = "2"

class GenderType:
    UNSET = "0"
    MALE = "1"
    FEMALE = "2"

class LayerID:
    BASE = "base"
    EAR = "ear"
    EAR_RING = "earRing"
    EYE_BROWS = "eyeBrows"
    EYES = "eyes"
    FACIAL_HAIR = "facialHair"
    GLASSES = "glasses"
    HAIR = "hair"
    HAT = "hat"
    MOUTH = "mouth"
    NOSE = "nose"
    SHIRT = "shirt"
    BACKGROUND = "background"
    MASK = "mask"
    HEADWEAR = "headwear"

# 简化的数据类
class CreateAvatarDto:
    def __init__(self, renderer=None, amount=1, size=280, gender=None):
        self.renderer = renderer or RenderType.SVG
        self.amount = amount
        self.size = size
        self.gender = gender or GenderType.UNSET

# 如果导入失败，定义简化版本
if 'LayerItemConfig' not in globals():
    class ColorGroup:
        def __init__(self, weight=1, value=None):
            self.weight = weight
            self.value = value or []

    class LayerItemConfig:
        def __init__(self, gender_type=None, weight=1, filename=None, empty=False, 
                     available_color_groups=None, color_same_as=None, remove_layers=None, 
                     color_not_same_as=None, congratulate=False):
            self.gender_type = gender_type or GenderType.UNSET
            self.weight = weight
            self.filename = filename
            self.empty = empty
            self.available_color_groups = available_color_groups or []
            self.color_same_as = color_same_as
            self.remove_layers = remove_layers or []
            self.color_not_same_as = color_not_same_as or []
            self.congratulate = congratulate
            self.color = None
            
        def get(self, key, default=None):
            """兼容字典接口"""
            return getattr(self, key, default)

def get_random_value_in_arr(arr, weight_key='weight'):
    """根据权重从数组中随机选择一个元素"""
    if not arr:
        return None
    
    tmp_arr = []
    for index, el in enumerate(arr):
        weight = getattr(el, weight_key, 1)
        for _ in range(weight):
            tmp_arr.append(index)
    
    if not tmp_arr:
        return arr[0] if arr else None
    
    random.shuffle(tmp_arr)
    len_arr = len(tmp_arr)
    random_index = random.randint(0, len_arr - 1) % len_arr
    return arr[tmp_arr[random_index]]

# 导入完整的配置和模型
try:
    from config.layer_configs import LAYER_LIST, AVAILABLE_COLORS
    from models.dto import LayerItemConfig, ColorGroup
    from models.enums import LayerID, GenderType
except ImportError:
    # 如果导入失败，使用简化配置作为后备
    AVAILABLE_COLORS = {
        LayerID.BASE: [
            ColorGroup(weight=20, value=['#F9C9B6']),
            ColorGroup(weight=2, value=['#AC6651']),
            ColorGroup(weight=2, value=['#77311D']),
            ColorGroup(weight=1, value=['#FFDACB']),
        ],
        LayerID.HAIR: [
            ColorGroup(weight=1, value=['#000000']),
            ColorGroup(weight=1, value=['#ffffff']),
            ColorGroup(weight=1, value=['#F4D150']),
            ColorGroup(weight=1, value=['#FC909F']),
            ColorGroup(weight=1, value=['#6BD9E9']),
            ColorGroup(weight=1, value=['#9287FF']),
        ],
        LayerID.SHIRT: [
            ColorGroup(weight=1, value=['#000000', '#AFAFAF']),
            ColorGroup(weight=1, value=['#ffffff', '#A1A1A1']),
            ColorGroup(weight=1, value=['#F4D150', '#FFEBA4']),
        ],
        LayerID.BACKGROUND: [
            ColorGroup(weight=1, value=['#E0DDFF']),
            ColorGroup(weight=1, value=['#D2EFF3']),
            ColorGroup(weight=1, value=['#FFEDEF']),
        ],
    }
    
    LAYER_LIST = [
        {
            'id': LayerID.BASE,
            'dir': 'Base',
            'description': '头部',
            'z_index': 100,
            'layers': [
                LayerItemConfig(
                    gender_type=GenderType.UNSET,
                    filename='1',
                    weight=10,
                    available_color_groups=AVAILABLE_COLORS[LayerID.BASE],
                ),
            ],
        },
        {
            'id': LayerID.EYES,
            'dir': 'Eyes',
            'description': '眼睛',
            'z_index': 200,
            'layers': [
                LayerItemConfig(filename='Default', gender_type=GenderType.UNSET, weight=10),
                LayerItemConfig(filename='Happy', gender_type=GenderType.UNSET, weight=10),
                LayerItemConfig(filename='Angry', gender_type=GenderType.UNSET, weight=10),
            ],
        },
        {
            'id': LayerID.HAIR,
            'dir': 'Hair',
            'description': '头发',
            'z_index': 400,
            'layers': [
                LayerItemConfig(
                    filename='Default',
                    gender_type=GenderType.UNSET,
                    available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
                    color_not_same_as=[LayerID.BACKGROUND],
                    weight=10,
                ),
                LayerItemConfig(
                    filename='Short',
                    gender_type=GenderType.FEMALE,
                    available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
                    color_not_same_as=[LayerID.BACKGROUND],
                    weight=10,
                ),
            ],
        },
        {
            'id': LayerID.SHIRT,
            'dir': 'Shirt',
            'description': '衣服',
            'z_index': 200,
            'layers': [
                LayerItemConfig(
                    filename='Crew',
                    gender_type=GenderType.UNSET,
                    available_color_groups=AVAILABLE_COLORS[LayerID.SHIRT],
                    weight=10,
                ),
            ],
        },
        {
            'id': LayerID.BACKGROUND,
            'dir': 'Background',
            'description': '背景图层',
            'z_index': 0,
            'layers': [
                LayerItemConfig(
                    filename='Blue',
                    gender_type=GenderType.UNSET,
                    available_color_groups=AVAILABLE_COLORS[LayerID.BACKGROUND],
                    weight=10,
                ),
            ],
        },
    ]

class SimpleAvatarCreator:
    """简化版头像生成器"""
    
    def __init__(self, resource_path: str = "resource"):
        self.resource_path = resource_path
        
    def create_one(self, config: CreateAvatarDto, congratulate_action: Optional[Callable] = None) -> str:
        """生成一个随机头像"""
        size = config.size or 280
        gender = config.gender or GenderType.UNSET
        
        # 1. 获取图层列表并排序
        layer_list = LAYER_LIST.copy()
        layer_list.sort(key=lambda x: x['z_index'])
        
        # 2. 获取随机的图层组合
        random_layer_list = self._get_random_layers(layer_list, gender)
        
        # 3. 检查需要删除的图层
        random_layer_list = self._remove_conflicting_layers(random_layer_list)
        
        # 4. 选取颜色
        self._assign_colors(random_layer_list)
        
        # 5. 检查颜色冲突
        self._resolve_color_conflicts(random_layer_list)
        
        # 6. 检查颜色跟随
        self._apply_color_following(random_layer_list)
        
        # 7. 清理冗余信息
        self._clean_layer_data(random_layer_list)
        
        # 8. 绘制SVG
        congratulate = False
        groups = []
        
        # 按z_index排序图层，确保背景在最底层
        sorted_layers = sorted(random_layer_list, key=lambda x: self._get_z_index(x['id']))
        
        # 检查是否有背景图层
        has_background_layer = any(layer_data['id'] == LayerID.BACKGROUND for layer_data in sorted_layers)
        
        # 如果没有背景图层，添加默认背景颜色
        if not has_background_layer:
            # 生成默认背景颜色
            background_color = self._get_default_background_color()
            groups.append(f'\n<g id="gaoxia-avatar-Background">\n<rect width="100%" height="100%" fill="{background_color}" />\n</g>\n')
        
        for layer_data in sorted_layers:
            layer = layer_data['layer']
            dir_name = layer_data['dir']
            
            try:
                if getattr(layer, 'congratulate', False):
                    congratulate = True
            except (AttributeError, TypeError):
                pass
                
            # 读取SVG文件
            svg_raw = self._load_svg_file(dir_name, layer.filename)
            
            # 如果SVG内容为空，跳过这个图层
            if not svg_raw.strip():
                continue
                
            # 替换颜色
            item_color = layer_data.get('color')
            svg_raw = self._replace_colors(svg_raw, layer, item_color)
            
            # 提取SVG内容
            svg_content = self._extract_svg_content(svg_raw)
            groups.append(f'\n<g id="gaoxia-avatar-{dir_name}">\n{svg_content}\n</g>\n')
            
            # 如果是背景图层，确保背景颜色在背景图片下面
            if layer_data['id'] == LayerID.BACKGROUND:
                # 在背景图片下面添加背景颜色
                background_color = self._get_default_background_color()
                groups.insert(-1, f'\n<g id="gaoxia-avatar-BackgroundColor">\n<rect width="100%" height="100%" fill="{background_color}" />\n</g>\n')
        
        if congratulate and congratulate_action:
            congratulate_action()
            
        # 生成最终SVG
        svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 380 380" fill="none" xmlns="http://www.w3.org/2000/svg">
{''.join(groups)}
</svg>'''.strip().replace('\n', '').replace('\t', '')
        
        return svg
    
    def _get_random_layers(self, layer_list, gender):
        """获取随机的图层组合"""
        random_layers = []
        
        for layer_item in layer_list:
            # 性别过滤
            filtered_layers = []
            for layer in layer_item['layers']:
                try:
                    gender_type = getattr(layer, 'gender_type', GenderType.UNSET)
                    if (gender == GenderType.UNSET or 
                        gender_type == gender or 
                        gender_type == GenderType.UNSET):
                        filtered_layers.append(layer)
                except (AttributeError, TypeError):
                    # 如果属性访问失败，默认包含
                    filtered_layers.append(layer)
            
            if filtered_layers:
                selected_layer = get_random_value_in_arr(filtered_layers)
                try:
                    empty = getattr(selected_layer, 'empty', False)
                    if not empty:
                        # 检查文件是否存在，如果不存在则跳过
                        file_path = os.path.join(self.resource_path, layer_item['dir'], f"{selected_layer.filename}.svg")
                        if os.path.exists(file_path):
                            random_layers.append({
                                'id': layer_item['id'],
                                'dir': layer_item['dir'],
                                'layer': selected_layer
                            })
                except (AttributeError, TypeError):
                    # 如果属性访问失败，检查文件是否存在
                    try:
                        file_path = os.path.join(self.resource_path, layer_item['dir'], f"{selected_layer.filename}.svg")
                        if os.path.exists(file_path):
                            random_layers.append({
                                'id': layer_item['id'],
                                'dir': layer_item['dir'],
                                'layer': selected_layer
                            })
                    except (AttributeError, TypeError):
                        # 如果连filename属性都没有，跳过这个图层
                        continue
        
        # 确保背景总是存在
        background_exists = any(item['id'] == LayerID.BACKGROUND for item in random_layers)
        if not background_exists:
            # 找到背景配置
            background_item = next((item for item in layer_list if item['id'] == LayerID.BACKGROUND), None)
            if background_item and background_item['layers']:
                # 选择一个背景
                selected_background = get_random_value_in_arr(background_item['layers'])
                if selected_background and not getattr(selected_background, 'empty', False):
                    file_path = os.path.join(self.resource_path, background_item['dir'], f"{selected_background.filename}.svg")
                    if os.path.exists(file_path):
                        random_layers.append({
                            'id': background_item['id'],
                            'dir': background_item['dir'],
                            'layer': selected_background
                        })
        
        return random_layers
    
    def _remove_conflicting_layers(self, layer_list):
        """删除冲突的图层"""
        remove_id_list = []
        
        for item in layer_list:
            layer = item['layer']
            try:
                # 使用getattr安全地获取属性
                remove_layers = getattr(layer, 'remove_layers', None)
                if remove_layers:
                    remove_id_list.extend(remove_layers)
            except (AttributeError, TypeError):
                # 如果属性不存在或访问失败，跳过
                continue
        
        return [item for item in layer_list if item['id'] not in remove_id_list]
    
    def _assign_colors(self, layer_list):
        """为图层分配颜色"""
        for item in layer_list:
            layer = item['layer']
            try:
                available_color_groups = getattr(layer, 'available_color_groups', None)
                if available_color_groups:
                    # 获取可用的颜色组
                    color_groups = available_color_groups
                    if color_groups:
                        # 随机选择一个颜色组
                        color_group = get_random_value_in_arr(color_groups)
                        if color_group:
                            value = getattr(color_group, 'value', None)
                            if value:
                                # 使用整个颜色数组，保持与原始逻辑一致
                                item['color'] = value
            except (AttributeError, TypeError):
                # 如果属性不存在或访问失败，跳过
                continue
        
        # 应用颜色跟随规则
        self._apply_color_following(layer_list)

    def _resolve_color_conflicts(self, layer_list):
        """解决颜色冲突"""
        for item in layer_list:
            layer = item['layer']
            try:
                color_not_same_as = getattr(layer, 'color_not_same_as', None)
                if color_not_same_as and 'color' in item:
                    current_colors = item['color']
                    for target_id in color_not_same_as:
                        target_item = next((x for x in layer_list if x['id'] == target_id), None)
                        if target_item and 'color' in target_item:
                            tried = 0
                            max_try = 10
                            # 只判断第一个颜色相同为冲突
                            while (target_item['color'] and 
                                   len(target_item['color']) > 0 and 
                                   len(current_colors) > 0 and 
                                   target_item['color'][0] == current_colors[0]):
                                tried += 1
                                if tried > max_try:
                                    break
                                # 重新取色
                                available_color_groups = getattr(layer, 'available_color_groups', None)
                                if available_color_groups:
                                    color_group = get_random_value_in_arr(available_color_groups)
                                    if color_group and hasattr(color_group, 'value') and color_group.value:
                                        target_item['color'] = get_random_value_in_arr(color_group.value)
            except (AttributeError, TypeError):
                # 如果属性不存在或访问失败，跳过
                continue

    def _apply_color_following(self, layer_list):
        """应用颜色跟随规则"""
        for item in layer_list:
            layer = item['layer']
            try:
                color_same_as = getattr(layer, 'color_same_as', None)
                if color_same_as:
                    same_id = color_same_as
                    # 找到要跟随的图层
                    for other_item in layer_list:
                        if other_item['id'] == same_id and 'color' in other_item:
                            item['color'] = other_item['color']
                            break
            except (AttributeError, TypeError):
                # 如果属性不存在或访问失败，跳过
                continue
    
    def _clean_layer_data(self, layer_list):
        """清理图层数据"""
        for item in layer_list:
            layer = item['layer']
            # 删除不需要的属性，但保留颜色相关属性
            try:
                if hasattr(layer, 'gender_type'):
                    delattr(layer, 'gender_type')
                if hasattr(layer, 'weight'):
                    delattr(layer, 'weight')
                if hasattr(layer, 'remove_layers'):
                    delattr(layer, 'remove_layers')
            except (AttributeError, TypeError):
                # 如果属性访问失败，跳过
                pass
    
    def _load_svg_file(self, dir_name: str, filename: str) -> str:
        """加载SVG文件"""
        file_path = os.path.join(self.resource_path, dir_name, f"{filename}.svg")
        
        # 如果文件不存在，返回空字符串
        if not os.path.exists(file_path):
            return ""
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                svg_content = f.read()
                
            # 如果是背景图层，确保尺寸正确
            if dir_name == 'Background':
                # 标准化背景SVG的尺寸为380x380
                svg_content = self._normalize_background_svg(svg_content)
                
            return svg_content
        except:
            return ""
    
    def _generate_default_svg(self, dir_name: str, filename: str) -> str:
        """生成默认SVG"""
        # 根据图层类型生成不同的默认SVG
        if dir_name == 'Background':
            return '<svg><rect width="380" height="380" fill="#E0DDFF"/></svg>'
        elif dir_name == 'Base':
            return '<svg><circle cx="190" cy="190" r="80" fill="#F9C9B6"/></svg>'
        elif dir_name == 'Eyes':
            return '<svg><circle cx="170" cy="180" r="8" fill="#000"/><circle cx="210" cy="180" r="8" fill="#000"/></svg>'
        elif dir_name == 'Hair':
            return '<svg><path d="M110 120 Q190 80 270 120 Q250 200 190 180 Q130 200 110 120" fill="#000000"/></svg>'
        elif dir_name == 'Shirt':
            return '<svg><rect x="140" y="220" width="100" height="80" fill="#000000"/></svg>'
        else:
            return '<svg><rect width="100" height="100" fill="#ccc"/></svg>'
    
    def _replace_colors(self, svg_raw: str, layer, item_color=None) -> str:
        """替换SVG中的颜色占位符"""
        if not item_color:
            return svg_raw
            
        # 匹配颜色占位符 {{color[0]}}, {{color[1]}} 等
        color_pattern = r'\{\{color\[(\d+)\]\}\}'
        
        def replace_color(match):
            index = int(match.group(1))
            if isinstance(item_color, list) and len(item_color) > index:
                return item_color[index]
            elif index == 0 and item_color:
                # 如果item_color不是数组，直接使用
                return item_color
            return match.group(0)
        
        return re.sub(color_pattern, replace_color, svg_raw)
    
    def _get_z_index(self, layer_id: str) -> int:
        """获取图层的z_index"""
        z_index_map = {
            LayerID.BACKGROUND: 0,
            LayerID.BASE: 100,
            LayerID.EYES: 200,
            LayerID.EYE_BROWS: 200,
            LayerID.FACIAL_HAIR: 201,
            LayerID.MOUTH: 202,
            LayerID.NOSE: 203,
            LayerID.SHIRT: 200,
            LayerID.HAIR: 400,
            LayerID.HAT: 401,
            LayerID.HEADWEAR: 450,
            LayerID.EAR: 500,
            LayerID.EAR_RING: 501,
            LayerID.MASK: 501,
            LayerID.GLASSES: 600,
        }
        return z_index_map.get(layer_id, 100)

    def _normalize_background_svg(self, svg_content: str) -> str:
        """标准化背景SVG的尺寸为380x380"""
        # 替换width和height属性
        svg_content = re.sub(r'width="[^"]*"', 'width="380"', svg_content)
        svg_content = re.sub(r'height="[^"]*"', 'height="380"', svg_content)
        
        # 替换viewBox属性
        svg_content = re.sub(r'viewBox="[^"]*"', 'viewBox="0 0 380 380"', svg_content)
        
        # 确保背景有正确的rect元素填充整个区域
        if '<rect' not in svg_content or 'width="100%"' not in svg_content:
            # 如果没有合适的背景rect，添加一个
            svg_content = re.sub(
                r'(<svg[^>]*>)',
                r'\1<rect width="100%" height="100%" fill="{{color[0]}}" />',
                svg_content
            )
        
        return svg_content

    def _get_default_background_color(self) -> str:
        """获取默认背景颜色"""
        # 从背景颜色配置中随机选择一个
        background_colors = AVAILABLE_COLORS.get(LayerID.BACKGROUND, [])
        if background_colors:
            color_group = get_random_value_in_arr(background_colors)
            if color_group and hasattr(color_group, 'value') and color_group.value:
                return color_group.value[0]  # 返回第一个颜色
        # 默认颜色
        return '#E0DDFF'
    
    def _extract_svg_content(self, svg_raw: str) -> str:
        """提取SVG内容，去除svg标签"""
        # 移除开头的svg标签
        content = re.sub(r'<svg[^>]*>', '', svg_raw)
        # 移除结尾的svg标签
        content = re.sub(r'</svg>', '', content)
        return content.strip() 