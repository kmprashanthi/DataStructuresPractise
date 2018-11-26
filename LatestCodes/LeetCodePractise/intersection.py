def intersect(nums1,nums2):
    nums1.sort()
    nums2.sort()
    result = []
    i=0
    j=0
    while (i < len(nums1) and j < len(nums2)):
        if (nums1[i] == nums2[j]) and (nums1[i] not in result):
            result.append(nums1[i])
            i+=1
            j+=1
        elif nums1[i] > nums2[j]:
            j+=1
        elif nums1[i] < nums2[j]:
            i+=1
    return result

print (intersect([4,9,5],[9,4,9,8,4]))