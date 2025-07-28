from models.enums import LayerID
from models.dto import ColorGroup

# 可用颜色配置
AVAILABLE_COLORS = {
    # 皮肤的可用色 - 贴近黄种人
    LayerID.BASE: [
        ColorGroup(weight=35, value=['#F9C9B6']),  # 浅黄肤色
        ColorGroup(weight=30, value=['#E8B4A0']),  # 中等黄肤色
        ColorGroup(weight=20, value=['#D4A08C']),  # 深黄肤色
        ColorGroup(weight=10, value=['#C08B78']),  # 较深黄肤色
        ColorGroup(weight=5, value=['#FFDACB']),   # 很浅的肤色
    ],

    # 头发的可用色 - 避免纯白色
    LayerID.HAIR: [
        ColorGroup(weight=15, value=['#000000']),  # 黑色
        ColorGroup(weight=10, value=['#F4D150']),  # 金黄色
        ColorGroup(weight=10, value=['#FC909F']),  # 粉红色
        ColorGroup(weight=10, value=['#6BD9E9']),  # 天蓝色
        ColorGroup(weight=10, value=['#9287FF']),  # 紫色
        ColorGroup(weight=8, value=['#362100']),   # 深棕色
        ColorGroup(weight=8, value=['#562400']),   # 棕色
        ColorGroup(weight=8, value=['#5B3800']),   # 深褐色
        ColorGroup(weight=8, value=['#FF4D6B']),   # 红色
        ColorGroup(weight=8, value=['#000056']),   # 深蓝色
        ColorGroup(weight=8, value=['#CB7F50']),   # 橙色
        ColorGroup(weight=8, value=['#F6CF45']),   # 黄色
        ColorGroup(weight=8, value=['#876565']),   # 灰色
    ],

    # 服装可用颜色
    LayerID.SHIRT: [
        ColorGroup(weight=1, value=['#000000', '#AFAFAF']),
        ColorGroup(weight=1, value=['#ffffff', '#A1A1A1']),
        ColorGroup(weight=1, value=['#F4D150', '#FFEBA4']),
        ColorGroup(weight=1, value=['#FC909F', '#FFEDEF']),
        ColorGroup(weight=1, value=['#6BD9E9', '#D2EFF3']),
        ColorGroup(weight=1, value=['#9287FF', '#E0DDFF']),
        ColorGroup(weight=1, value=["#E97C17", "#d4975e"]),
        ColorGroup(weight=1, value=["#B4B0CD", "#e4e2f1"]),
        ColorGroup(weight=1, value=["#878787", "#b6b6b6"]),
        ColorGroup(weight=1, value=["#CA475A", "#d86072"]),
        ColorGroup(weight=1, value=["#0C4F2F", "#3d8160"]),
        ColorGroup(weight=1, value=["#354161", "#579b7a"]),
    ],

    # 胡子可用色
    LayerID.FACIAL_HAIR: [
        ColorGroup(weight=1, value=['#222F37']),
        ColorGroup(weight=1, value=['#612507']),
        ColorGroup(weight=1, value=['#F3D010']),
    ],

    # 背景可用色 - 避免纯白色
    LayerID.BACKGROUND: [
        ColorGroup(weight=15, value=['#E0DDFF']),  # 浅紫色
        ColorGroup(weight=15, value=['#D2EFF3']),  # 浅蓝色
        ColorGroup(weight=15, value=['#FFEDEF']),  # 浅粉色
        ColorGroup(weight=15, value=['#FFEBA4']),  # 浅黄色
        ColorGroup(weight=10, value=['#F4D150']),  # 金黄色
        ColorGroup(weight=10, value=['#FC909F']),  # 粉红色
        ColorGroup(weight=10, value=['#6BD9E9']),  # 天蓝色
        ColorGroup(weight=10, value=['#9287FF']),  # 紫色
    ],

    # 耳朵可用色（与头部相同）
    LayerID.EAR: [
        ColorGroup(weight=35, value=['#F9C9B6']),  # 浅黄肤色
        ColorGroup(weight=30, value=['#E8B4A0']),  # 中等黄肤色
        ColorGroup(weight=20, value=['#D4A08C']),  # 深黄肤色
        ColorGroup(weight=10, value=['#C08B78']),  # 较深黄肤色
        ColorGroup(weight=5, value=['#FFDACB']),   # 很浅的肤色
    ],
    LayerID.EAR_RING: [],
    LayerID.EYES: [],
    LayerID.EYE_BROWS: [],
    LayerID.GLASSES: [],
    LayerID.HAT: [],
    LayerID.MOUTH: [],
    LayerID.NOSE: [],
    LayerID.MASK: [],
    LayerID.HEADWEAR: [],
} 