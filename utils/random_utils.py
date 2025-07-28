import random
from typing import List, Dict, Any

def get_random_value_in_arr(
    arr: List[Any], 
    weight_key: str = 'weight'
) -> Any:
    """
    根据权重从数组中随机选择一个元素
    
    Args:
        arr: 数组
        weight_key: 权重字段名
        
    Returns:
        随机选择的元素
    """
    tmp_arr: List[int] = []
    
    for index, el in enumerate(arr):
        # 支持字典和对象两种方式获取权重
        if hasattr(el, 'get') and callable(getattr(el, 'get')):
            # 字典对象
            weight = el.get(weight_key, 1)
        elif hasattr(el, weight_key):
            # 对象属性
            weight = getattr(el, weight_key, 1)
        else:
            weight = 1
            
        for _ in range(weight):
            tmp_arr.append(index)
    
    # 随机打乱数组
    random.shuffle(tmp_arr)
    
    if not tmp_arr:
        return arr[0] if arr else None
    
    len_arr = len(tmp_arr)
    random_index = random.randint(0, len_arr - 1) % len_arr
    return arr[tmp_arr[random_index]] 