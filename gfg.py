#remove common in string and conatenate
def remove_common_concat():
    N = int(input())
    for i in range(N):
        s1 = input()
        s2 = input()

        # print(s2)
        hash=[]
        lists1=list(s1)
        lists2=list(s2)
        # for ch in lists2:
        #    hash.append(ch)
        for ch in lists1:
            if ch in lists2:
                c1=lists1.count(ch)
                c2=lists2.count(ch)
                while c1>0 or c2>0:
                    if c1>0:
                        lists1.remove(ch)
                        c1=c1-1
                    if c2>0:
                        lists2.remove(ch)
                        c2=c2-1

        if lists1 != None or lists2 != None :
            print(str(lists1+lists2))
        else:
            print('-1')


#leetcode-Find indices in a array to a given sum
def sum_of_two():
    k=int(input())
    arr=list(map(lambda x:int(x),[x for x in input().split()]))
    print(arr)
    hashmap={}
    for x in range(len(arr)):
        hashmap[arr[x]]=x

    for i in range(len(arr)):
        complement=k-arr[i]
        com_index=hashmap.get(complement)
        if com_index and com_index!=i:
            print( str(i)+" "+str(com_index))
            return
    return -1



if __name__ == "__main__":
     sum_of_two()
    # remove_common_concat()
