def max_sub_seq(li):
    max_so_far = 0
    max_ending_here = 0
    for (val) in li:
        max_ending_here = max(max_ending_here + val, val)
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far    

print max_sub_seq([11, -9, 20, -100, 5])
