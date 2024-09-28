from typing import Tuple,List


def min_max(arr: List[int]) -> Tuple[int,int]:
    if len(arr) == 1:
        return arr[0],arr[0]
    
    if len(arr) == 2:
        return min(arr[0],arr[1]),max(arr[0],arr[1])
    
    mid = len(arr)//2
    min1,max1 = min_max(arr[:mid])
    min2,max2 = min_max(arr[mid:])
    
    
    return min(min1,min2),max(max1,max2)
    # Test cases
test_cases = [
    ([3, 1, 4, 1, 5, 9, 2, 6], (1, 9)),    # General case with multiple elements
    ([7], (7, 7)),                          # Single element array
    ([1, 10], (1, 10)),                     # Two elements in increasing order
    ([10, 1], (1, 10)),                     # Two elements in decreasing order
    ([2, 2, 2, 2], (2, 2)),                 # All elements the same
    ([-3, -1, -4, -2], (-4, -1)),           # Negative numbers
    ([], None),                             # Empty array (could be handled if necessary)
]
    
    # Running test cases
for i, (arr, expected) in enumerate(test_cases):
    if len(arr) == 0:
        print(f"Test Case {i+1}: Skipped (Empty array)")
    else:
        result = min_max(arr)
        print(f"Test Case {i+1}: {arr} => min_max = {result}, Expected = {expected}, Pass = {result == expected}")