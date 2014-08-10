import math

def get_dig(l, dig):
    return (l // (10 ** dig)) % 10

def bucket_sort(li, dig):
    buckets = { x : [] for x in range(10)}
    for l in li:
        d = get_dig(l, dig)
        buckets[d].append(l)
    res = []
    for x in range(10):
        res.extend(buckets[x]) 
    return res

def radix_sort(li):
    max_ = max(li)
    num_passes = int(math.ceil(math.log(max_,10)))
    res = li
    for x in range(num_passes):
        res = bucket_sort(res, x)
    return res     

print "Result:", radix_sort([7, 100, 1145, 43, 7, 74, 25, 58, 5, 11, 12, 99, 4, 10, 23, 21])    
