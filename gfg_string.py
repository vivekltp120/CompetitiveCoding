# code for input

#Parenthesis balancing
def parenthesis_balancing(exp):

    temp = []
    for b in exp:
        if b in ['(', '{', '[']:
            temp.append(b)
            continue

        if len(temp) == 0:
            print('not balanced')
            return
        elif b in [')', '}', ']']:
            stb = temp.pop()

        if b == ')' and stb == '(':
            continue
        elif b == ']' and stb == '[':
            continue
        elif b == '}' and stb == '{':
            continue
        else:
            print('not balanced')
            return

    if len(temp) == 0:
        print('balanced')
    else:
        print('not balanced')


def input_parenthesis():
    n=int(input())
    for i in range(n):
        exp = input()
        parenthesis_balancing(exp)

#reverse a string

def reverse_string(a):
    a = a[::-1]
    print('.'.join(a))


def reverse_string_two(a):
    left = 0
    right = len(a) - 1
    while left < right:
        temp = a[left]
        a[left] = a[right]
        a[right] = temp
        left += 1
        right -= 1
    print('.'.join(a))


def input_reverse_string():
    N = int(input())
    for i in range(N):
        arr = [x for x in input().split('.')]
        reverse_string_two(arr)


#convert a roman into decimal
def getvalue(c):
    if c=='I':
        return 1
    if c=='V':
        return 5
    if c=='X':
        return 10
    if c=='L':
        return 50
    if c=='C':
        return 100
    if c=='D':
        return 500
    if c=='M':
        return 1000
    return -1

def roman_to_decimal(roman):
    num=0
    n=len(roman)
    i=0
    while i<n:
        if i+1<n:
          if getvalue(roman[i])<getvalue(roman[i+1]):
             num=num+getvalue(roman[i+1])-getvalue(roman[i])
             i+=1
          else:
             num+=getvalue(roman[i])
        else:
             num+=getvalue(roman[i])
        i+=1
    print(num)
def inputRoman():
    N=int(input())
    for i in range(N):
        roman=input()
        roman_to_decimal(roman)

#Permutation of string
def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def permutation(a, l, r):
    if l == r:
        print("".join(a), end=" ")
    for i in range(l, r):
            swap(a, l, i)
            permutation(a, l+1, r)
            swap(a, l, i)


def input_permutation():
    N = int(input())
    for i in range(N):
        arr = [x for x in input()]
        permutation(arr, 0, len(arr))
        print()


# remove consecuively duplicate do later

def rem_rec_util(mystr):
    if len(mystr)==1:
        return mystr
    i=1
    while i<len(mystr):
        if mystr[i-1]==mystr[i]:
           i+=1
        else:
            break
    mystr=mystr[i-1:]
    curr=mystr.pop(0)
    if len(mystr)!=0:
        res=rem_rec_util(mystr)
        if res[0]!=curr:
            res.insert(0,curr)
        return res
    else:
        return mystr
def rec_remo(mystr):
    n = len(mystr)
    if mystr==None:
        return 'Empty String'
    if n<=1:
        return mystr
    res=rem_rec_util(mystr)
    print(''.join(res))


def input_duplicate_removal():
    N = int(input())
    for i in range(N):
        sta = list(input())
        rec_remo(sta)



input_duplicate_removal()

if __name__=='__main__':

     #Parenthesis Balancing
     # input_parenthesis()
     #reverse string
     # input_reverse_string()
     #roman input
     # inputRoman()
     # input_permutation()
     # input_duplicate_removal()









