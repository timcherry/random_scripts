def top_down_split_merge(li):
    if len(li) == 1:
        return li
    midpoint = len(li)/2
    left = top_down_split_merge(li[:midpoint])
    right = top_down_split_merge(li[midpoint:])
    merged = merge_sides(left, right)
    return merged

def merge_sides(left, right): 
    merged = list()
    li, ri = 0, 0
    while True:
        if li == len(left) and ri == len(right):
            break    
        if (li < len(left)) and (ri ==  len(right) or left[li] <= right[ri]):
            merged.append(left[li])
            li += 1
        else:
            merged.append(right[ri])
            ri += 1
    return merged

print top_down_split_merge([5,6,20,324,56,21,1, 99])
