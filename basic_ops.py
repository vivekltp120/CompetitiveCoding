import math
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

def bit_operation(x,y):
    print('In binary : x - '+bin(x)+ ' y - '+bin(y))
    print('Or - ' + str(x|y))
    print('And - ' + str(x&y))
    print('Xor - ' + str(x^y))
    print('Right shift - '+ str(x>>2) + ' -> '+ str(bin(x>>2)))
    print('X - ' + str(bin(x)))
    print('Left Shift - ' + str(x<<2)+ ' -> ' + str(bin(x<<2)))

if __name__=='__main__':
    a=12
    b='g'
    arr=[2,3,4,5,6]
    print('character to integet-'+str(ord(b)))
    print('integer to octal-'+oct(a))
    print('integer to hex-'+hex(a))
    print('hex to integer-'+str(int(hex(a),16)))
    print('oct to integer-'+str(int(oct(a),8)))
    exp_map(arr)
    exp_filter(arr)
    x=60
    y=13
    bit_operation(x,y)

