def fun(A, K):
    # Your code goes here
    A = list(A)
    n = len(A)
    sslist = []
    # find the subset for the array
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(1 << n):
        res = ''
        for j in range(n):
            if (i & (1 << j)) != 0:
               res =res + str(A[j])
        print('res-{0}'.format(res))


T = int(input())
for _ in range(T):
    N = int(input())
    K = int(input())
    A = map(int, input().split(' '))

    out_ = fun(A, K)
    print(out_)