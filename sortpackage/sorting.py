def bubble_sort(items):
    '''
    Returns an array of items, sorted in ascending order.
    Array is sorted using the bubble sort methodology.
    If elements of items are of:
        int or float type:
            order of elements will be in numerical ascending order
        float type:
            order of elements will be in alphabetical ascending order

    Args:
        items (list): list that is to be ordered in ascending order,
            function will fail if:
                items is not of list type
                elements are of not of homogenous data type


    Returns:
        list: items ordered in an ascending order

    Examples:
        >>> bubble_sort(['a','e','h','y','o'])
        ['a', 'e', 'h', 'o', 'y']
        >> bubble_sort([1,3,8,5,3,2])
        [1, 2, 3, 3, 5, 8]
        >> bubble_sort(['hello', 'I', 'am', 'your', 'friend'])
        ['I', 'am', 'friend', 'hello', 'your']
    '''

    out = items.copy()
    for i in range(len(out)):
        for j in range(len(out)-1-i):
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]

    return out

def merge_sort(items):
    '''
    Returns an array of items, sorted in ascending order.
    Array is sorted using the merge sort methodology.
    If elements of items are of:
        int or float type:
            order of elements will be in numerical ascending order
        float type:
            order of elements will be in alphabetical ascending order

    Args:
        items (list): list that is to be ordered in ascending order,
            function will fail if:
                items is not of list type
                elements are of not of homogenous data type


    Returns:
        list: items ordered in an ascending order

    Examples:
        >>> merge_sort(['a','e','h','y','o'])
        ['a', 'e', 'h', 'o', 'y']
        >> merge_sort([1,3,8,5,3,2])
        [1, 2, 3, 3, 5, 8]
        >> merge_sort(['hello', 'I', 'am', 'your', 'friend'])
        ['I', 'am', 'friend', 'hello', 'your']
    '''

    len_i = len(items)
    if len_i == 1:
        return items
    mid_point = int(len_i / 2)
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])
    return merge(i1, i2)

def merge(list1, list2):
    sorted_list = []
    i = j = 0
    length = len(list1) + len(list2)
    while len(sorted_list) != length:
        if len(list1) == i:
            sorted_list += list2[j:]
            break
        elif len(list2) == j:
            sorted_list += list1[i:]
            break
        elif list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1
    return sorted_list

def quick_sort(items):
    '''
    Returns an array of items, sorted in ascending order.
    Array is sorted using the quick sort methodology.
    The last element of the list has been hard-coded as the pivot.
    If elements of items are of:
        int or float type:
            order of elements will be in numerical ascending order
        float type:
            order of elements will be in alphabetical ascending order

    Args:
        items (list): list that is to be ordered in ascending order,
            function will fail if:
                items is not of list type
                elements are of not of homogenous data type

    Returns:
        list: items ordered in an ascending order

    Examples:
        >>> quick_sort(['a','e','h','y','o'])
        ['a', 'e', 'h', 'o', 'y']
        >> quick_sort([1,3,8,5,3,2])
        [1, 2, 3, 3, 5, 8]
        >> quick_sort(['hello', 'I', 'am', 'your', 'friend'])
        ['I', 'am', 'friend', 'hello', 'your']
    '''

    len_i = len(items)

    if len_i <= 1:
        return items

    pivot = items[-1]
    smaller = []
    larger = []
    duplicate = []
    for i in items:
        if i < pivot:
            smaller.append(i)
        elif i > pivot:
            larger.append(i)
        elif i == pivot:
            duplicate.append(i)

    smaller = quick_sort(smaller)
    larger = quick_sort(larger)

    return smaller + duplicate + larger
