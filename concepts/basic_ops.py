import math
import os
from collections import deque
from collections import OrderedDict
from collections import defaultdict


def combination(n, r):
    if n < r:
        return 0


def square(x):
    return x * x


def cube(x):
    return x * x * x


def area_circle(x):
    return (math.pi) * x * x


def odd_number(x):
    if x % 2 != 0:
        return x

    return


def exp_map(a):
    """
    This function demonstrates the use of map with different functions
    Applies multiple functions to each element in the input list and demonstrates the use of `map`.
    Parameters
    ----------
    a : list
        A list of numeric values to which the functions will be applied.
    Returns
    -------
    None
        This function prints the results of mapping different functions over the input list.
    Notes
    -----
    This function assumes that the functions `square`, `cube`, and `area_circle` are defined elsewhere in the code.
    It prints intermediate results for demonstration purposes.
    """
    
    result = []
    for i in a:
        print("map experiment:\n")
        result.append(list(map(lambda x: x(i), [square, cube, area_circle])))
        result.append(list(map(square, a)))
    print('In map:' + str(result))


def exp_filter(a):
    """
    This function demonstrates the use of filter to extract odd numbers from a list.
    Parameters
    ----------
    a : list
        A list of numeric values from which odd numbers will be filtered.
    Returns
    -------
    None
        This function prints the results of filtering odd numbers from the input list.
    Notes
    -----
    This function assumes that the function `odd_number` is defined elsewhere in the code.
    It prints the filtered results for demonstration purposes.
    """
    print("filter experiment:\n")
    result = (list(filter(odd_number, a)))
    print('In filter:' + str(result))


def bit_operation():
    """
    This function demonstrates various bitwise operations and conversions between binary, octal, and hexadecimal representations.
    It performs operations such as bitwise OR, AND, XOR, right shift, left shift, and conversions.
    Returns
    -------
    None
        This function prints the results of the bitwise operations and conversions.
    Notes
    -----
    This function uses fixed values for `x` and `y` to demonstrate the operations.
    It prints the results for demonstration purposes.
    """
    global a, b, arr
    a = 8
    b = 10
    arr = [1, 2, 3, 4, 5]
    print("Bit operation experiment:\n")
    print('a = ' + str(a) + ' b = ' + str(b))
    print('Or - ' + str(a | b))
    print('And - ' + str(a & b))
    print('Xor - ' + str(a ^ b))
    print('Right Shift - ' + str(a >> 2) + ' -> ' + str(bin(a >> 2)))
    print('X - ' + str(bin(a)))
    print('Left Shift - ' + str(a << 2) + ' -> ' + str(bin(a << 2)))
    print('Binary {0} to Dec {1} '.format(bin(a), int(bin(a), 2)))
    print('Oct {0} to Dec {1} '.format(oct(a), int(oct(a), 8)))                     
    x = 1024
    y = 10
    print("bit operation experiment:\n")

    print('In binary : x - ' + bin(x) + ' y - ' + bin(y))
    print('Or - ' + str(x | y))
    print('And - ' + str(x & y))
    print('Xor - ' + str(x ^ y))
    print('Right Shift - ' + str(x >> 2) + ' -> ' + str(bin(x >> 2)))
    print('X - ' + str(bin(x)))
    print('Left Shift - ' + str(x << 2) + ' -> ' + str(bin(x << 2)))
    print('Binary {0} to Dec {1} '.format(bin(x), int(bin(x), 2)))
    print('Oct {0} to Dec {1} '.format(oct(x), int(oct(x), 8)))
    print('Hex {0} to Dec {1} '.format(hex(x), int(hex(x), 16)))


def dir_operation(path):
    """
    This function walks through the directory structure starting from the given path and prints the directories.
    Parameters
    ----------
    path : str
        The path to the directory to be traversed.
    Returns
    -------
    None
        This function prints the directories found during the traversal.
    Notes
    -----
    This function uses `os.walk` to traverse the directory structure.
    It prints the directories found at each level of the traversal.
    """
    print("Directory operation experiment:\n")
    if not os.path.exists(path):
        print("Path does not exist: " + path)
        return
    if not os.path.isdir(path):
        print("Path is not a directory: " + path)
        return
    print('Traversing directory: ' + path)
    print('Directories and files in the path:\n')
    # os.walk returns a generator that yields a tuple of (root, dirnames, filenames)
    # where root is the current directory path, dirnames is a list of directories in that path,
    # and filenames is a list of files in that path.
    # Here we are only printing the directories (dirnames) found in the path.
    # If you want to print files as well, you can modify the print statement accordingly.
    # Note: dirpath is the list of directories in the current root, not the files.
    # If you want to print files, you can use file in the for loop.
    # os.walk(path) will traverse the directory tree starting from the given path
    # and yield tuples of (root, dirnames, filenames) for each directory it visits.
    # The root is the current directory path, dirpath is a list of directories in that path,        
    for root, dirnames, filenames in os.walk(path):
        # print ('root'+str(root)+'dirnames-'+str((dirnames))+'filenames'+str(filenames))
        print('Directories - ' + str(dirnames))
        print('Files - ' + str(filenames))


def yield_exp():
    """
    This function is a generator that yields the square of numbers from 0 to 4.
    It demonstrates the use of a generator to produce a sequence of values.
    Yields
    ------
    int
        The square of the current number in the range from 0 to 4.
    Notes
    -----
    This function uses a for loop to iterate through the range and yields the square of each number.
    """
    print("Yield experiment:\n")
    print('In yield:')
    # Using a generator to yield squares of numbers from 0 to 4
    # This is a simple generator function that yields the square of each number in the range.
    # The yield statement allows the function to return a value and pause its execution,
    # so that it can be resumed later to yield the next value.
    # This is useful for generating a sequence of values without storing them all in memory at once.
    # This is a simple generator function that yields the square of each number in the range.           
    for i in range(5):
        y = i * i
        yield y


def return_exp():
    """
    This function demonstrates the use of a return statement to return the current index in a loop.
    It iterates through a range of numbers and returns the current index.
    Returns
    -------
    int
        The current index in the range from 0 to 4.
    Notes
    -----
    This function uses a for loop to iterate through the range and returns the current index.
    """
    print("Return experiment:\n")
    print('In return:')
    # Using a return statement to return the current index in a loop
    # This is a simple function that returns the current index in the range.
    # The return statement exits the function and returns the value to the caller.
    # This is a simple function that returns the current index in the range.
    # The return statement exits the function and returns the value to the caller.
    # This is a simple function that returns the current index in the range.
    # The return statement exits the function and returns the value to the caller.      
    for i in range(5):
        return i


# sorted a array with another array
def activity_time(arr,dep):
    """
    This function sorts two lists, `arr` and `dep`, based on the values in `arr`.
    It uses the `zip` function to pair elements from both lists, sorts them based on the first list,
    and then unzips them back into two separate lists.
    Parameters
    ----------
    arr : list
        A list of arrival times.
    dep : list
        A list of departure times corresponding to the arrival times in `arr`.
    Returns
    -------
    None
        This function prints the sorted lists and the zipped list.
    Notes
    -----
    This function assumes that `arr` and `dep` are of the same length.
    It uses the `zip` function to pair elements from both lists, sorts them based on the first list,
    and then unzips them back into two separate lists using `map` and `zip`.
    """
    print("Activity time experiment:\n")
    print('Arrival times: ' + str(arr))
    print('Departure times: ' + str(dep))
    if len(arr) != len(dep):
        print("Error: Arrival and departure lists must be of the same length.")
        return
    if not arr or not dep:
        print("Error: Arrival and departure lists cannot be empty.")
        return
    if len(arr) == 1:
        print("Single element in both lists, no sorting needed.")
        return
    if len(arr) == 0:
        print("Both lists are empty, nothing to sort.")
        return
    if len(arr) != len(dep):
        print("Error: Arrival and departure lists must be of the same length.")
        return
    print("Sorting the arrays based on arrival times:\n")
    print("Before sorting:\n")
    print("Arrival: ", arr)
    print("Departure: ", dep)
    # Using zip to pair elements from both lists, sorting based on the first list (arrival times)
    sorted_array = sorted(zip(arr, dep), key=lambda x: x[0])
    # Unzipping the sorted pairs back into two separate lists
    arr, dep = map(list, zip(*sorted_array))
    print("After sorting:\n")
    print("Arrival: ", arr)
    print("Departure: ", dep)
    print("Sorted pairs (arrival, departure): ", sorted_array)          
    print("Array sorting experiment with zip and unzip:\n")
    sorted_array=sorted(zip(arr,dep),key=lambda x:x[0])
    arr,dep=map(list,zip(*sorted_array))
    print(arr,dep)
    print(sorted_array)
    pass


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def dictionaries():
    """
    This functions demonstrates various operations on dictionaries in Python.
    It includes sorting a list, creating a dictionary, modifying values in a dictionary,
    using a defaultdict, and an OrderedDict.
    Parameters
    ----------
    None
    Returns
    -------
        None
    Notes
    -----
    This function assumes that the input list and dictionaries are defined within the function.
    It prints the results of the operations for demonstration purposes.
    It also demonstrates the use of a defaultdict and an OrderedDict.
    It shows how to create a dictionary, sort it, and modify its values.
 
    """
    arr = [1, 2, 6, 4, 5]
    print("dict experiment:\n")

    sortarr = arr
    sortarr.sort()
    print(sortarr)
    print(arr)

    tdict = {'a': [2, 3], 'b': [4, 5], 'e': [3, 1]}
    sdict = sorted(tdict.items(), key=lambda it: it[1][1])

    # can't change the tuple key or value
    # TypeError: 'tuple' object does not support item assignment
    # sdict[1][0] = 4
    print(sdict)
    print(list(sdict))
    print(dict(sdict))

    pdict = {'a': [2, 3], 'b': [4, 5], 'e': [3, 1]}
    pdict.get('a')[1] = 8

    print(pdict.get('a')[1])

    # default
    graph1 = defaultdict(list)
    print(graph1[0].append(0))
    graph1['vivek'].append('kumar')
    print(graph1)

    # ordered dictionary
    graph = OrderedDict()
    graph[0] = 'vivek'
    print(graph)

    # simple see whether it takes a list as a value or if we have to use the default dict
    ndic = {}
    ndic[0] = []
    ndic[0].extend(arr)
    print(ndic)


# for experiment and syntax clarification
def for_syntax_and_python_concept():
    """
    This function demonstrates various Python concepts and operations including directory traversal,
    bitwise operations, string manipulation, and the use of generators.
    It includes operations such as converting between different number bases, filtering and mapping lists,
    and using deque, set, and dictionary operations.
    Parameters
    ----------
    None
    Returns
    -------
        None
    Notes
    -----
    This function assumes that the input path and array are defined within the function.
    It prints the results of the operations for demonstration purposes.
    It also demonstrates the use of a generator to yield values, and the use of a return statement to return values.
    It also demonstrates the use of a generator to yield values, and the use of a return statement to return values.
    """
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
    arrival = [900, 940, 1100, 950 , 1500, 1800]
    departure = [910, 1200,1130, 1120, 1900, 2000]
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
    S = 'abcde'
    ls = list(S)
    S[1] = 'k'
    print(S[1])
    print(ls)


if __name__ == '__main__':
    arr = [2, 3, 4, 5, 6]
    path = '/media/viv/Seagate Backup Plus Drive/Fun/Audio/2018/'  # '/home/viv/PycharmProjects/CompetitiveCoding'
    for_syntax_and_python_concept()
    # dictionaries()
    # bit_operation()
    # string_op()
