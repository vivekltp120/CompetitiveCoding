#find pair for sum
def find_pair():
    T = int(input())
    for t in range(T):
        a,x= list(map(lambda x:int(x), input().split()))
        a=list(map(lambda x:int(x),input().split()))
        a.sort()
        l=0
        h=len(a)-1
        sum=0
        while l<h:
            sum=a[l] + a[h]
            if sum==x:
                break
            elif sum<x:
                l+=1
            else:
                h-=1
        if sum==x:
          print ('Yes')
        else:
          print('No')
# given binary number is multiple of 3
#Method 1
def get_decimal_from_binary(str):
    binary_num = [int(x) for x in str]
    binary_num.reverse()
    deci=0
    for i in range(len(binary_num)):
        deci+=binary_num[i]*(2**i)
    return deci



def multiple_of_3():
    T = int(input())
    for t in range(T):
        str=input()
        deci=get_decimal_from_binary(str)
        if deci%3==0:
            print (1)
        else:
            print (0)

#Find the maximum contigous subarray Kadane's Algorithm
def contiguous_maximum_sum(arr):
    T = int(input())
    for t in range(T):
        n = list(map(lambda x: int(x), input().split()))
        arr = list(map(lambda x: int(x), input().split()))


        max_so_far=max_end_here=0
        for i in arr:
            max_end_here=max_end_here+i

            if max_so_far<max_end_here:
                max_so_far=max_end_here

            if max_end_here<0:
                max_end_here=0


        print( max_so_far )

#tiny urls problem(from a string of url we have to find a tiny url)

def convert_custom_mapping(url_id,url_map):
    mstack=[]
    while url_id:
        mstack.append(url_map[int(url_id%62)])
        url_id=int(url_id/62)
    mstack.reverse()
    mstack=''.join(mstack)
    return mstack


def id_to_tinyurl():
    url_map='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    #map the url id in short url
    url_id=15264777
    tiny_url=convert_custom_mapping(url_id,url_map)
    print('url form id -> '+tiny_url)
    tiny_url_to_id(tiny_url,url_map)

def tiny_url_to_id(tiny_url,url_map):
    url_map=list(url_map)
    tiny_url=list(tiny_url)[::-1]
    id=0
    for i in range(len(tiny_url)):
        ind=url_map.index(tiny_url[i])
        id+= ind*(62**i)
    print('id from url -> '+str(id))


#major element in array

def major_element():
    T = int(input())
    for t in range(T):
        n = int(input())
        arr = list(map(lambda x: int(x), input().split()))
        major_so_far=0
        current_major=0
        pmc=0
        cmc=1
        arr.sort()
        for i in range(len(arr)):
            if i<len(arr)-1 and arr[i]==arr[i+1]:
               cmc+=1
            elif pmc<cmc:
                pmc=cmc
                cmc=1 
#Ease of array
def ease_of_array():
    T = int(input())
    for t in range(T):
        n = list(map(lambda x: int(x), input().split()))
        arr = list(map(lambda x: int(x), input().split()))
        for i in range(len(arr)):
            if (i+1)<len(arr) and arr[i+1]!=0 and arr[i]==arr[i+1]:
                arr[i]*=2
                arr[i+1]=0
        print(arr)
        arr=rearrange(arr)
        arr=''.join(str(x) for x in arr)
        print(str(arr))
def rearrange(arr):
    n=len(arr)
    i=0
    for j in range(n):
        if arr[j]!=0:
            arr[i]=arr[j]
            if i!=j:
             arr[j]=0
            i += 1
    return arr
#Nearest multiple of 10
def nearest_multiple_10():
    T = int(input())
    for t in range(T):
        num= int(input())
        quotient=int(num/10)
        remainder=int(num%10)
        if remainder<=5:
            result=num-remainder
        else:
            result=num+(10-remainder)
        print(result)
#Remove leading zeros from an IP address
def remove_leading_zero():
    T = int(input())
    for t in range(T):
        ip=input()
        split_ip=ip.split('.')
        for i in range(len(split_ip)):
            print(split_ip[i])
            #find tthe quotien and reminder
            x=int(split_ip[i])
            q=x//10
            r=x%10
            split_ip[i]= q*10+r
        split_ip='.'.join(str(x) for x in split_ip)
        print(split_ip)





if __name__=="__main__":
      # find_pair()
      # multiple_of_3()
      # id_to_tinyurl()
      # major_element()
      # ease_of_array()
      # nearest_multiple_10()
      remove_leading_zero()