def all_rotations(box):
    (h,w,d) = box
    return [(h,w,d), (w,h,d), (d,h,w)]

def find_max_height(in_boxes):
    boxes = []
    for box in in_boxes:
        boxes.extend(all_rotations(box))

    sb = sorted(boxes, key=lambda x: x[1]*x[2], reverse=True)

    msh = [x[0] for x in sb]

    for i in range(len(sb)):
        for j in range(i + 1):
            if (sb[i][1] < sb[j][1]) and (sb[i][2] < sb[j][2]):
                msh[i] = msh[j] + sb[i][0]
    return max(msh)

print "Max Height", find_max_height([(10, 12, 32), (4, 6, 7), (1, 2, 3), (4, 5, 6),])
