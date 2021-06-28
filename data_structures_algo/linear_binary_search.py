# Linear search algorithm

def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(target):
    if target is not None:
        print("Target found at index", target)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)


# type 1 Binary Search  - LIST NEEDS TO BE SORTED IN ASCENDING

def binary_search(list, target):
# first/last refers to indices of the list
    first, last = 0, len(list) - 1

    while (first <= last):
        midpoint = (first+last)//2 # // is floor division operator

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

# type 2 RECURSIVE binary search

def binary_search_recursive(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return binary_search_recursive(list[midpoint+1:],target)
            else:
                return binary_search_recursive(list[:midpoint],target)

def verify(result):
    print("Target found:",result)

result = binary_search_recursive(numbers,12)
verify(result)
result = binary_search_recursive(numbers,6)
verify(result)
