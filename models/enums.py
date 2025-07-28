from enum import Enum

class RenderType(Enum):
    """渲染类型"""
    SVG = "0"
    JPEG = "1"
    BASE64 = "2"

class GenderType(Enum):
    """性别类型"""
    UNSET = "0"
    MALE = "1"
    FEMALE = "2"

class LayerID(Enum):
    """图层ID"""
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