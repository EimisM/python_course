from typing import Tuple

def sum_list(numbers: int) -> int:
    return sum(numbers)

def average_list(numbers: int) -> float:
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)
        
def max_list(numbers: int) -> int:
    if len(numbers) == 0:
        return None
    else:
        return max(numbers)

def min_list(numbers: int) -> int:
    if len(numbers) == 0:
        return None
    else:
        return min(numbers)
    
def remove_duplicates(numbers: int) -> Tuple[int]:
    seen = set()
    unique_items = []
    for item in numbers:
        if item not in seen:
            unique_items.add(item)
            seen.add(item)
        return unique_items