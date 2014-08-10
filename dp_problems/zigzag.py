def longest_zig_zag(li):
    if len(li) <= 2:
        return True
    inc = li[0] < li[1]
    longest = 2
    ends_here = 2
    for i in range(2, len(li)):
        if inc == (li[i] < li[i-1]):
            inc = not inc 
            ends_here += 1
        longest = max(longest, ends_here) 
    return longest

print "Longest Zig Zag:", longest_zig_zag([1, 17, 5, 10, 13, 15, 10, 5, 16, 8])
