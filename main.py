from typing import List, Set, Tuple


def create_intervals(data: Set[int]) -> List[Tuple[int, int]]:
    """
    Create unit intervals from a set of numbers.
    """
    intervals = []
    start = None
    last = None
    for number in sorted(data):
        if not start:
            start = number
            last = number
        elif number == last + 1:
            last = number
        else:
            intervals.append((start, last))
            start = number
            last = number
    if start is not None:
        intervals.append((start, last))
    
    return intervals

def test(data, output):
    assert create_intervals(data) == output

print(create_intervals({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))
print(create_intervals({1, 2, 3, 4, 6, 7, 8, 9}))
print(create_intervals({1, 6, 9, 10, 7, 8}))
print(create_intervals({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 16, 20, 22, 23}))
