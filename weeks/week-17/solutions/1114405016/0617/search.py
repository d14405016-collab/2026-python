def linear_search(data: list, target) -> int:
    for i, val in enumerate(data):
        if val == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """Binary search on sorted list.

    Assumes data is already sorted in ascending order.
    If data is not sorted, behavior is undefined.
    Returns index of target if found, otherwise -1.
    """
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
