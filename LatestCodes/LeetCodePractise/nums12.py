def mergeSortArray(nums1,m,nums2,n):
    nums1 = nums1[0:m]
    nums1.extend(nums2)
    nums1.sort()
    return nums1

print (mergeSortArray([1,2,3,0,0,0],3,[2,5,6],3))