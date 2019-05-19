import math
import os
from collections import deque
from collections import OrderedDict
from collections import defaultdict




def combination(n,r):
    if n<r:
        return 0
    
def square(x):
    return x*x
def cube(x):
    return x*x*x
def area_circle(x):
    return (math.pi)*x*x
def odd_number(x):
    if x%2!=0:
        return x

    return
def exp_map(a):
    result=[]
    for i in a:
     result.append(list(map(lambda x:x(i),[square,cube,area_circle])))
     result.append(list(map(square,a)))
    print('In map:'+str(result))
def exp_filter(a):
    result=(list(filter(odd_number,a)))
    print('In filter:'+str(result))

def bit_operation():
    x=1024
    y=10
    print('In binary : x - '+bin(x)+ ' y - '+bin(y))
    print('Or - ' + str(x|y))
    print('And - ' + str(x&y))
    print('Xor - ' + str(x^y))
    print('Right Shift - '+ str(x>>2) + ' -> '+ str(bin(x>>2)))
    print('X - ' + str(bin(x)))
    print('Left Shift - ' + str(x<<2)+ ' -> ' + str(bin(x<<2)))
    print('Binary {0} to Dec {1} '.format(bin(x),int(bin(x),2)))
    print('Oct {0} to Dec {1} '.format(oct(x),int(oct(x),8)))
    print('Hex {0} to Dec {1} '.format(hex(x),int(hex(x),16)))

def dir_operation(path):
     #implementation of walk
     for root,dirpath,file in os.walk(path):
         # print ('root'+str(root)+'dirpath-'+str((dirpath))+'file'+str(file))
         print ('file - '+str(dirpath))

def yield_exp():
    for i in range(5):
        y=i*i
        yield y
def return_exp():
    for i in range(5):
        return i
#sorted a array with another array
def activity_time(A,D):
    pass


class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

def dictionaries():
    arr=[1,2,6,4,5]
    sortarr=arr
    sortarr.sort()
    print(sortarr)
    print(arr)

    tdict={'a':[2,3],'b':[4,5],'e':[3,1]}
    sdict=sorted(tdict.items(),key=lambda it:it[1][1])

    # can't change the tuple key or value
    # TypeError: 'tuple' object does not support item assignment
    # sdict[1][0] = 4
    print(sdict)
    print(list(sdict))
    print(dict(sdict))




    pdict={'a':[2,3],'b':[4,5],'e':[3,1]}
    pdict.get('a')[1]=8
    print(pdict.get('a')[1])




    #default
    graph1=defaultdict(list)
    print(graph1[0].append(0))
    graph1['vivek'].append('kumar')
    print(graph1)

    #ordered dictionary
    graph = OrderedDict()
    graph[0]='vivek'
    print(graph)

    #simple see whether it take a list as value or we havet o use default dict
    ndic={}
    ndic[0]=[]
    ndic[0].extend(arr)
    print(ndic)
#for experiment and syntax clarification
def for_syntax_and_python_concept():
    global a, b, arr
    dir_operation(path)
    converer_hex_binary_and_more()
    exp_map(arr)
    exp_filter(arr)
    bit_operation()
    yield_obj()
    arr_exp()
    deque_exp()
    set_exp()
    various_exp()


def various_exp():
    global a, b, arr
    a = 8
    b = a
    a += 1
    print('a=%d b=%d' % (a, b))
    a = 'Vivek'
    b = 'vivej'
    arr = []
    for i in range(5):
        new = Node(i)


def yield_obj():
    for i in yield_exp():
        print(i)


def arr_exp():
    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]
    activity_time(arrival, departure)
    cook = ['aa1', 'aa2', 'bb1', 'cc1']
    print(('aa1' in cook))
    c = [None, None, None]
    print(c)
    print(None in c)


def deque_exp():
    inq = deque()
    inq.extend(['a', 'b', 'c'])
    inq.remove('a')


def set_exp():
    seta = set()
    seta.add('vivek')
    print('vivek' in seta)
    print(seta.add('vivek'))


def converer_hex_binary_and_more():
    a = 12
    b = 'g'
    print('character to integet-' + str(ord(b)))
    print('integer to octal-' + oct(a))
    print('integer to bianry- ' + bin(a))
    print('integer to hex-' + hex(a))
    print('hex to integer-' + str(int(hex(a), 16)))
    print('oct to integer-' + str(int(oct(a), 8)))



def string_op():
    S='abcde'
    ls=list(S)
    S[1]='k'
    print(S[1])
    print(ls)



if __name__=='__main__':

    arr=[2,3,4,5,6]
    path='/media/viv/Seagate Backup Plus Drive/Fun/Audio/2018/' #'/home/viv/PycharmProjects/CompetitiveCoding'
    for_syntax_and_python_concept()
    # dictionaries()
    # bit_operation()
    # string_op()






