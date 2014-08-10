def inc_sub_seq(li):
    longest_ends_here = [li[0]]
    longest = [li[0]]
    for x in li[1:]:
        if x > longest_ends_here[-1]:
            longest_ends_here.append(x)
        else:
            longest_ends_here = [x]
        if len(longest_ends_here) > len(longest):
            longest = longest_ends_here
    return longest

print "Longest Increasing Sub Sequence:", inc_sub_seq([1, 0, 2, 8, 1, 0, 6, 7, 10, 2, 1])
