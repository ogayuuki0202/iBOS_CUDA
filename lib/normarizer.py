import numpy as np

def normalize(data):
    """
    Min-Maxスケーリングを使用してデータを正規化します。
    """
    min_val = np.min(data)
    max_val = np.max(data)
    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    return normalized_data, min_val, max_val

def denormalize(normalized_data, min_val, max_val):
    """
    正規化されたデータを元の範囲に逆正規化します。
    """
    denormalized_data = [x * (max_val - min_val) + min_val for x in normalized_data]
    return denormalized_data

def normalize_to_minusone_one(arr):
    """
    numpy_arrayを-1から1に正規化する関数
    """
    max_val = np.max(arr)
    min_val = np.min(arr)
    normalized_arr = (2 * (arr - min_val) / (max_val - min_val)) - 1
    
    return normalized_arr, min_val, max_val

def inverse_normalize_to_minusone_one(normalized_arr, min_val, max_val):
    # 正規化された配列を元の範囲に逆変換
    range_val = max_val - min_val
    arr = (normalized_arr + 0.5) * range_val + min_val
    
    return arr

def inverse_normalize(array, min_val, max_val):
    return array * (max_val - min_val) + min_val
