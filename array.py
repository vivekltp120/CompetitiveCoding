#find the longest subsequence for the given array
def longest_subarray_of_multiplication(arr,k):
    si=0
    ei=0
    alen=len(arr)
    max_so_far=0
    subarr=[]
    maximum_sum=0
    while ei<alen:
        max_so_far+=arr[ei]
        if max_so_far>=maximum_sum:
            subarr.append(list(arr[si:ei+1]))
            maximum_sum=max_so_far
        ei+=1


#find the number of subarray of given multiplication
def subarry_for_mul(arr,k):
    subarr=[]
    mul=1
    for si in range(len(arr)):
        for ei in range(si,len(arr)):
            mul*=arr[ei]
            if mul==k:
                subarr.append(arr[si:ei+1])
        mul=1
    print(subarr)





if __name__=='__main__':
    arr=[-2, -3, 4, -1, -2, 1, 5, -3]
    # longest_subsequence(arr)
    subarry_for_mul(arr,8)