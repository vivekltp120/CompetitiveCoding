# LCS by dynamic programming

t = None


def getlcs(a, x):
    """
    This function retrieves the longest common subsequence from the matrix 'a' and string 'x'.
    Args:
       a (list): 2D list representing the direction of the longest common subsequence
       x (str): The original string from which the longest common subsequence is derived.
    Returns:
       None: This function prints the longest common subsequence.
    """
    print('Get LCS:')
    if not a or not x:
        print('No common subsequence found.')
        return
    if len(a) == 0 or len(x) == 0:
        print('No common subsequence found.')
        return
    if len(a) != len(x):
        print('Invalid input: Length of direction matrix and string do not match.')
        return
    if not isinstance(a, list) or not all(isinstance(row, list) for row in a):
        print('Invalid input: Direction matrix must be a 2D list.')
        return
    if not isinstance(x, str):
        print('Invalid input: String must be of type str.')
        return
    if not all(isinstance(item, str) for item in x):
        print('Invalid input: String must contain only characters.')
        return
    lcs = ''
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 'diagonal':
                lcs += x[i]
    print('Longest Common Subsequence - ' + lcs)


def longest_common_subsequence(x, y):
    """
    This function finds the longest common subsequence (LCS) of two strings using dynamic programming.
    Args:
       x (str): The first string.
       y (str): The second string.
    Returns:
       None: This function prints the longest common subsequence.
    """
    len_x = len(x)
    len_y = len(y)
    s = [[0 for i in range(len_y + 1)] for j in range(len_x + 1)]
    a = [[0 for i in range(len_y + 1)] for j in range(len_x + 1)]
    x = ' ' + x
    y = ' ' + y

    for i in range(1, len_x + 1):
        for j in range(1, len_y + 1):
            if x[i] == y[j]:
                s[i][j] = s[i - 1][j - 1] + 1
                a[i][j] = 'diagonal'

            elif s[i - 1][j] > s[i][j - 1]:
                s[i][j] = s[i - 1][j]
                a[i][j] = 'horizontal'
            else:
                s[i][j] = s[i][j - 1]
                a[i][j] = 'vertical'

    getlcs(a, x)


# find the maximum profit for given weight
def createDictAndMaximumWeight():
    """
    This function creates a dictionary of items with their profits and weights,
    and returns the dictionary along with a maximum weight for which items will be selected.
    Returns:
       tuple: A tuple containing the dictionary of items and the maximum weight.
    """
    
    print('Knapsack Problem:')
    wdict = []
    infile = open('knapsack.txt', 'r')
    for line in infile.readlines():
        p, w = [int(x) for x in line.split()]
        wdict.append((p, w))
    wdict.append((0, 0))
    wdict.sort()
    print(wdict)
    for i in range(len(wdict)):
        print(wdict[i][1], end=' ')
    print('Give the max weight for which object will be selected')
    m = 8  # int(input())
    return wdict, m


def knapsack_problem():
    """
    This function solves the knapsack problem using dynamic programming.
    It creates a profit matrix based on the items' profits and weights,
    and calculates the maximum profit for a given weight limit.
    Returns_______
       None: This function prints the profit matrix.
    """
    global t
    print('Knapsack Problem:')
    t = None
    wdict, m = createDictAndMaximumWeight()
    n = len(wdict)
    profitmatrix = [[0 for x in range(m + 1)] for y in range(n)]
    for i in range(1, n):
        for w in range(1, m + 1):
            if i - 1 >= 0:
                p = profitmatrix[i - 1][w]
            else:
                p = 0

            if w - wdict[i][1] >= 0 and i - 1 >= 0:
                q = profitmatrix[i - 1][w - wdict[i][1]] + wdict[i][0]
            else:
                q = 0

            profitmatrix[i][w] = max(p, q)

    print(profitmatrix)


# Matrix chain multiplication
def matrix_chain_multiplication():
    print('Matrix Chain Multiplication:')
    mat = ['5*4', '4*6', '6*2', '2*7']
    d = []
    mlen = len(mat)
    m = [[0 for x in range(mlen + 1)] for y in range(mlen + 1)]
    s = [[0 for x in range(mlen + 1)] for y in range(mlen + 1)]
    for x in mat:
        d.extend([int(y) for y in x.split('*') if int(y) not in d])
    print('dimension-' + str(d))

    for i in range(1, mlen + 1):
        for j in range(1, mlen + 1):
            temp = {}
            for k in range(i, j):
                temp[m[i][k] + m[k + 1][j] + d[i - 1] * d[j] * d[k]] = k

            if temp:
                m[i][j] = min(temp)
                s[i][j] = temp[min(temp)]
    print('Order of matrix is:', end='')
    getMatrix(s, 1, 4)


def getMatrix(s, i, j):
    if i == j:
        return
    getMatrix(s, i, s[i][j])
    getMatrix(s, s[i][j] + 1, j)
    print('A%d*' % (s[i][j]), end='')


# recursive
def count_coin_sum(coins, coin_sum, n):
    if coin_sum == 0:
        return 1
    if coin_sum <= 0:
        return 0
    if n <= 0:
        return 0
    return count_coin_sum(coins, coin_sum - coins[n - 1], n) + count_coin_sum(coins, coin_sum, n - 1)


# coin sum dynamic bottom up approach

def coin_sum(a, s):
    t = [[-1 for x in range(s + 1)] for y in range(len(a))]

    for j in range(s + 1):
        t[0][j] = 1
    for i in range(len(a)):
        t[i][0] = 1
    for i in range(1, len(a)):
        for j in range(s + 1):
            if j < a[i]:
                t[i][j] = t[i - 1][j]

            else:
                if (j - a[i]) >= 0:
                    t[i][j] = t[i - 1][j] + t[i][j - a[i]]
                else:
                    t[i][j] = t[i - 1][j]
            print(t)

    return t[len(a) - 1][s]


def input_coin_sum():
    N = int(input())
    for i in range(N):
        alen = int(input())
        arr = [int(x) for x in input().split()]
        s = int(input())
        print(count_coin_sum(arr, s))


# top down recursive count the subsequence
def count_subsequence(x, y, m, n):
    if n == 0 or (m == 0 and n == 0):
        return 1
    if m == 0:
        return 0
    if x[m] == y[n]:
        return count_subsequence(x, y, m - 1, n - 1) + count_subsequence(x, y, m - 1, n)
    else:
        return count_subsequence(x, y, m - 1, n)


# top down memoization
def count_sequence_util(x, y, m, n):
    print(t)


def count_subsequence_memoization(x, y, m, n, t):
    if n == 0 or (m == 0 and n == 0):
        return 1
    if m == 0:
        return 0

    if t[m][n] != -1:
        return t[m][n]

    if x[m - 1] == y[n - 1]:
        t[m][n] = count_subsequence_memoization(x, y, m - 1, n - 1, t) + count_subsequence_memoization(x, y, m - 1, n,
                                                                                                       t)
    else:
        t[m][n] = count_subsequence_memoization(x, y, m - 1, n, t)

    return t[m][n]


# recursive
def count_coin_sum(coins, coin_sum, n):
    if coin_sum == 0:
        return 1
    if coin_sum <= 0:
        return 0
    if n <= 0:
        return 0
    return count_coin_sum(coins, coin_sum - coins[n - 1], n) + count_coin_sum(coins, coin_sum, n - 1)


# recursive permutation
per_result = []


def util_recursive_perm(per_str, temp_result):
    global per_result
    if len(per_str) == 0:
        return "Invalid String"
    if len(per_str) == 1:
        temp_result = temp_result + per_str
        per_result.append(temp_result)
        # print(per_result)
        return
    for i in range(len(per_str)):
        temp_str = per_str[0:i] + per_str[i + 1:len(per_str)]
        util_recursive_perm(per_str=temp_str, temp_result=temp_result + per_str[i])


def tostring(arr):
    return "".join(arr)


def backtrack_permutation(arr, l, r):
    if l == r:
        back_result.append(tostring(arr))

    for i in range(l, r):
        arr[i], arr[l] = arr[l], arr[i]
        backtrack_permutation(arr, l + 1, r)
        arr[i], arr[l] = arr[l], arr[i]


def sub_string_without_repeating(arr):
    """
            :type s: str
            :rtype: int
            """
    seen = dict()
    l = 0
    output = 0
    for i in range(len(s)):
        if s[i] not in seen:
            output = max(output, i - l + 1)
            seen[s[i]] = i
        else:
            if seen[s[i]] < l:
                output = max(output, i - l + 1)
            else:
                l = seen[s[i]] + 1
        seen[s[i]] = i

    print(seen)
    return output

if __name__ == '__main__':

    # code = input("\nWhich dynamic code you want to be executed ")
    code = "lcs"

    match code:
        case "lcs":
            longest_common_subsequence('abcde', 'bd')
        case "knapsack":
            knapsack_problem()
        case "mcm":
            matrix_chain_multiplication()
        case "coinsum":
            # coin sum
            a = [1, 2, 3, 4, 6]
            s = 7
            print(count_coin_sum(a, s, 5))
            input_coin_sum()
        case "lcs_count":
            # count subsequence in a string
            print(count_subsequence("geeksforgeeks", "gks", 12, 2))
            m = 13
            n = 3
            t = [[-1 for x in range(n + 1)] for y in range(m + 1)]
            print(count_subsequence_memoization("geeksforgeeks", "gks", 13, 3, t))

        case "Perm":
            per_str = "abc"
            util_recursive_perm(per_str=per_str, temp_result='')
            print(per_result)
            back_result = []
            str_arr = list(per_str)
            n = len(per_str)
            backtrack_permutation(str_arr, 0, n)
            print("backtrack per result", back_result)

        case "substring":
            arr="abc"
            sub_string_without_repeating(arr)


        case _:
            print("No code need to be executed")
