a = 8


def func():
    global a;
    a += 2
    print(a)


def format_demo(n):
    for nf in ['x', 'E', 'b', 'o', 'g', 'd', 'f', 'n', ',', '_', '^', '=', '+', '-']:
        print(format(n, nf))
        print("{0} in format {0:1}".format(n, nf))


def reverse_bits(n):
    n = format(n, 'b')
    print(n)
    n = n.zfill(32)
    return int(n[::-1], 2)


def split_integer(n):
    # first method
    print(list(map(int, str(n))))
    # second method
    digits = [int(x) for x in list(str(n))]
    print(digits)
    digits.clear()
    # third method

    quotient = n
    while quotient != 0:
        quotient, mod = divmod(quotient, 10)
        digits.append(mod)
        print(quotient, mod)
    print(digits)
def split_string(str="geeksforgeeks"):
    splitstr=list(str)
    print(splitstr)
def last_char(str="vivek"):
    print(str[-1])
def access_string(str):
    new_str=str[0:3]+str[5:len(str)]
    print(new_str)

if __name__ == "__main__":
    n = 101011010101010101010
    # split_integer(n)
    n = 64573867
    str="vivekkumarchaursia"
    # reverse_bits(n)
    format_demo(n)
    # split_string(str)
    # last_char(str)
    # access_string(str)