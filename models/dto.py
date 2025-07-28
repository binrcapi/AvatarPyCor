from dataclasses import dataclass
from typing import Optional
from .enums import RenderType, GenderType, LayerID

@dataclass
class CreateAvatarDto:
    """创建头像的数据传输对象"""
    renderer: Optional[RenderType] = RenderType.SVG
    amount: Optional[int] = 1
    size: Optional[int] = 280
    gender: Optional[GenderType] = GenderType.UNSET

@dataclass
class Color:
    """颜色对象"""
    weight: int
    value: str

@dataclass
class ColorGroup:
    """颜色组对象"""
    weight: int
    value: list[str]

@dataclass
class LayerItemConfig:
    """图层项配置"""
    gender_type: GenderType
    weight: int
    filename: Optional[str] = None
    empty: bool = False
    available_color_groups: Optional[list[ColorGroup]] = None
    color_same_as: Optional[LayerID] = None
    remove_layers: Optional[list[LayerID]] = None
    color_not_same_as: Optional[list[LayerID]] = None
    congratulate: bool = False

@dataclass
class LayerListItem:
    """图层列表项"""
    id: LayerID
    dir: str
    z_index: int
    layers: list[LayerItemConfig]
    description: Optional[str] = None 