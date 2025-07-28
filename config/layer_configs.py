from models.enums import LayerID, GenderType
from models.dto import LayerItemConfig
from .colors import AVAILABLE_COLORS

# 基础图层配置
BASE_CONFIG = [
    LayerItemConfig(
        gender_type=GenderType.UNSET,
        filename='1',
        weight=10,
        available_color_groups=AVAILABLE_COLORS[LayerID.BASE],
    ),
    LayerItemConfig(
        gender_type=GenderType.UNSET,
        filename='QY-02',
        weight=10,
        available_color_groups=AVAILABLE_COLORS[LayerID.BASE],
    ),
]

# 耳朵图层配置
EAR_CONFIG = [
    LayerItemConfig(
        gender_type=GenderType.UNSET,
        filename='Attached',
        weight=10,
        available_color_groups=AVAILABLE_COLORS[LayerID.EAR],
        color_same_as=LayerID.BASE,
    ),
    LayerItemConfig(
        gender_type=GenderType.UNSET,
        filename='Detached',
        weight=10,
        available_color_groups=AVAILABLE_COLORS[LayerID.EAR],
        color_same_as=LayerID.BASE,
    ),
]

# 耳环图层配置
EAR_RING_CONFIG = [
    LayerItemConfig(
        empty=True,
        gender_type=GenderType.UNSET,
        weight=100,
    ),
    LayerItemConfig(
        gender_type=GenderType.UNSET,
        filename='Hoop',
        weight=10,
    ),
    LayerItemConfig(
        gender_type=GenderType.UNSET,
        filename='Stud',
        weight=10,
    ),
    LayerItemConfig(
        gender_type=GenderType.UNSET,
        filename='Firecrackers',
        weight=10,
    ),
    LayerItemConfig(
        gender_type=GenderType.UNSET,
        filename='lanterns',
        weight=10,
    ),
]

# 眉毛图层配置
EYEBROWS_CONFIG = [
    LayerItemConfig(
        gender_type=GenderType.UNSET,
        filename='dot',
        weight=10,
    ),
    LayerItemConfig(
        gender_type=GenderType.UNSET,
        filename="Doubt",
        weight=10,
    ),
    LayerItemConfig(
        gender_type=GenderType.FEMALE,
        filename="Eyelashes Down-1",
        weight=10,
    ),
    LayerItemConfig(
        gender_type=GenderType.UNSET,
        filename="Eyelashes Down",
        weight=10,
    ),
    LayerItemConfig(
        gender_type=GenderType.UNSET,
        filename="Eyelashes Up",
        weight=10,
    ),
    LayerItemConfig(
        gender_type=GenderType.UNSET,
        filename="Up",
        weight=10,
    ),
]

# 头发图层配置
HAIR_CONFIG = [
    LayerItemConfig(
        filename='Danny Phantom',
        gender_type=GenderType.MALE,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename='Double Ponytail',
        gender_type=GenderType.FEMALE,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=10,
        remove_layers=[LayerID.FACIAL_HAIR],
    ),
    LayerItemConfig(
        filename='Doug Funny',
        gender_type=GenderType.MALE,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename='Fonze',
        gender_type=GenderType.MALE,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename='Full',
        gender_type=GenderType.FEMALE,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND, LayerID.SHIRT],
        weight=10,
        remove_layers=[LayerID.FACIAL_HAIR],
    ),
    LayerItemConfig(
        filename='handsome',
        gender_type=GenderType.MALE,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename='Mr Clean',
        gender_type=GenderType.MALE,
        weight=10,
    ),
    LayerItemConfig(
        filename='Mr T',
        gender_type=GenderType.MALE,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename='Pixie',
        gender_type=GenderType.FEMALE,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=10,
        remove_layers=[LayerID.FACIAL_HAIR],
    ),
    LayerItemConfig(
        filename='QY-03',
        gender_type=GenderType.UNSET,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename='QY-04',
        gender_type=GenderType.FEMALE,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=10,
        remove_layers=[LayerID.FACIAL_HAIR],
    ),
    LayerItemConfig(
        filename='QY-05',
        gender_type=GenderType.MALE,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename='Turban',
        gender_type=GenderType.UNSET,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename="爆炸头",
        gender_type=GenderType.UNSET,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename="大波浪",
        gender_type=GenderType.FEMALE,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename="齐刘海",
        gender_type=GenderType.FEMALE,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename="秃头",
        gender_type=GenderType.MALE,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=5,
    ),
    LayerItemConfig(
        filename="Short",
        gender_type=GenderType.FEMALE,
        available_color_groups=AVAILABLE_COLORS[LayerID.HAIR],
        color_not_same_as=[LayerID.BACKGROUND],
        weight=10,
    ),
]

# 眼睛图层配置
EYES_CONFIG = [
    LayerItemConfig(
        filename='stare',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Disdain',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Eyes',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Eyeshadow',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Large and small eyes',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Round',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Smiling',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
]

# 胡子图层配置
FACIAL_HAIR_CONFIG = [
    LayerItemConfig(
        filename='Scruff',
        gender_type=GenderType.MALE,
        weight=10,
        available_color_groups=AVAILABLE_COLORS[LayerID.FACIAL_HAIR],
    ),
    LayerItemConfig(
        filename='Default',
        gender_type=GenderType.UNSET,
        weight=100,
    ),
]

# 嘴巴图层配置
MOUTH_CONFIG = [
    LayerItemConfig(
        filename='Frown',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='indifferent',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Laughing',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Nervous',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='open',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Pucker',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='QY-01',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Sad',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Smile-1',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Smile-2',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Smile',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
]

# 背景图层配置
BACKGROUND_CONFIG = [
    LayerItemConfig(
        filename='Blue',
        gender_type=GenderType.UNSET,
        available_color_groups=AVAILABLE_COLORS[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename='Dark Blue',
        gender_type=GenderType.UNSET,
        available_color_groups=AVAILABLE_COLORS[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename='Green',
        gender_type=GenderType.UNSET,
        available_color_groups=AVAILABLE_COLORS[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename='Grey',
        gender_type=GenderType.UNSET,
        available_color_groups=AVAILABLE_COLORS[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename='Red',
        gender_type=GenderType.UNSET,
        available_color_groups=AVAILABLE_COLORS[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename='Yellow',
        gender_type=GenderType.UNSET,
        available_color_groups=AVAILABLE_COLORS[LayerID.BACKGROUND],
        weight=10,
    ),
    LayerItemConfig(
        filename='clean',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='pattern1',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='pattern2',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='pattern3',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='pattern4',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='pattern5',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='pattern6',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='pattern7',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='pattern8',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='pattern9',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Firecrackers',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='fu',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='lanterns',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
]

# 衣服图层配置 - 添加所有可用的衣服
SHIRT_CONFIG = [
    LayerItemConfig(
        filename='Collared',
        gender_type=GenderType.UNSET,
        available_color_groups=AVAILABLE_COLORS[LayerID.SHIRT],
        weight=10,
    ),
    LayerItemConfig(
        filename='Crew',
        gender_type=GenderType.UNSET,
        available_color_groups=AVAILABLE_COLORS[LayerID.SHIRT],
        weight=10,
    ),
    LayerItemConfig(
        filename='Leisure',
        gender_type=GenderType.UNSET,
        available_color_groups=AVAILABLE_COLORS[LayerID.SHIRT],
        weight=10,
    ),
    LayerItemConfig(
        filename='Open',
        gender_type=GenderType.UNSET,
        available_color_groups=AVAILABLE_COLORS[LayerID.SHIRT],
        weight=10,
    ),
    LayerItemConfig(
        filename='chocker',
        gender_type=GenderType.UNSET,
        available_color_groups=AVAILABLE_COLORS[LayerID.SHIRT],
        weight=10,
    ),
]

# 眼镜图层配置
GLASSES_CONFIG = [
    LayerItemConfig(
        filename='Default',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Round',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Round-1',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='egg',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='star',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
]

# 帽子图层配置
HAT_CONFIG = [
    LayerItemConfig(
        filename='Default',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Christmas',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
]

# 头戴饰物图层配置
HEADWEAR_CONFIG = [
    LayerItemConfig(
        empty=True,
        gender_type=GenderType.UNSET,
        weight=30,
    ),
    LayerItemConfig(
        filename='cowHorn',
        gender_type=GenderType.UNSET,
        weight=2,
        congratulate=True,
    ),
]

# 口罩图层配置
MASK_CONFIG = [
    LayerItemConfig(
        filename='Default',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='3M',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='Cyberpunk',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
    LayerItemConfig(
        filename='General',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
]

NOSE_CONFIG = [
    LayerItemConfig(
        filename='Default',
        gender_type=GenderType.UNSET,
        weight=10,
    ),
]

# 图层列表配置
LAYER_LIST = [
    {
        'id': LayerID.BASE,
        'dir': 'Base',
        'description': '头部',
        'z_index': 100,
        'layers': BASE_CONFIG,
    },
    {
        'id': LayerID.EAR,
        'dir': 'Ear',
        'description': '耳朵',
        'z_index': 500,
        'layers': EAR_CONFIG,
    },
    {
        'id': LayerID.EAR_RING,
        'dir': 'Ear Ring',
        'description': '耳环',
        'z_index': 501,
        'layers': EAR_RING_CONFIG,
    },
    {
        'id': LayerID.EYE_BROWS,
        'dir': 'Eyebrows',
        'description': '眉毛',
        'z_index': 200,
        'layers': EYEBROWS_CONFIG,
    },
    {
        'id': LayerID.EYES,
        'dir': 'Eyes',
        'description': '眼睛',
        'z_index': 200,
        'layers': EYES_CONFIG,
    },
    {
        'id': LayerID.FACIAL_HAIR,
        'dir': 'Facial Hair',
        'description': '胡子',
        'z_index': 201,
        'layers': FACIAL_HAIR_CONFIG,
    },
    {
        'id': LayerID.GLASSES,
        'dir': 'Glasses',
        'description': '眼镜',
        'z_index': 600,
        'layers': GLASSES_CONFIG,
    },
    {
        'id': LayerID.HAIR,
        'dir': 'Hair',
        'description': '头发',
        'z_index': 400,
        'layers': HAIR_CONFIG,
    },
    {
        'id': LayerID.HEADWEAR,
        'dir': 'Headwear',
        'description': '头戴饰物',
        'z_index': 450,
        'layers': HEADWEAR_CONFIG,
    },
    {
        'id': LayerID.HAT,
        'dir': 'Hat',
        'description': '帽子',
        'z_index': 401,
        'layers': HAT_CONFIG,
    },
    {
        'id': LayerID.MOUTH,
        'dir': 'Mouth',
        'description': '嘴巴',
        'z_index': 202,
        'layers': MOUTH_CONFIG,
    },
    {
        'id': LayerID.NOSE,
        'dir': 'Nose',
        'description': '鼻子',
        'z_index': 203,
        'layers': NOSE_CONFIG,
    },
    {
        'id': LayerID.SHIRT,
        'dir': 'Shirt',
        'description': '衣服',
        'z_index': 200,
        'layers': SHIRT_CONFIG,
    },
    {
        'id': LayerID.BACKGROUND,
        'dir': 'Background',
        'description': '背景图层',
        'z_index': 0,
        'layers': BACKGROUND_CONFIG,
    },
    {
        'id': LayerID.MASK,
        'dir': 'Mask',
        'description': '口罩',
        'z_index': 501,
        'layers': MASK_CONFIG,
    },
] 