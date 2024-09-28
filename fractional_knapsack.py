from typing import List, Tuple


class Item:
    def __init__(self, value: int, weight: int):
        self.value = value
        self.weight = weight


def fractional_knapsack(items: List[Item], capacity: int) -> float:
    items.sort(key=lambda x: x.value/x.weight,reverse=True)
    remaining_capcity = capacity
    total_value = 0
    
    for item in items:
        if remaining_capcity >= item.weight:
            total_value += item.value
            remaining_capcity -= item.weight
        else:
            total_value += (item.value/item.weight) * remaining_capcity
            break
    
    return total_value
    
if __name__ == '__main__':
    items = [
        Item(60, 10),  # value, weight
        Item(100, 20),
        Item(120, 30)
    ]
    capacity = 50  # Total capacity of the knapsack
    
    max_value = fractional_knapsack(items, capacity)
        
    print("Maximum Value:", max_value)