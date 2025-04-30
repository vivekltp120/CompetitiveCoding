def sumtriangle(triangle):
    tlen = len(triangle)
    for i in range(len(triangle)):
        triangle[i] = [int(i) for i in triangle[i].split()]
    tsum = 0
    tsum = triangle[0][0]
    prev_i = 0
    prev_j = 0
    while True:
        curr_i = prev_i + 1
        curr_jv = prev_j
        curr_jd = prev_j + 1
        if curr_i < tlen:
            if curr_jv < curr_i + 1 and curr_jd < curr_i + 1:
                if triangle[curr_i][curr_jd] <= triangle[curr_i][curr_jv]:
                    tsum += triangle[curr_i][curr_jv]
                    prev_j = curr_jv
                else:
                    tsum += triangle[curr_i][curr_jd]
                    prev_j = curr_jd
            elif curr_jv < curr_i + 1:
                tsum += triangle[curr_i][curr_jv]
                prev_j = curr_jv
            prev_i = curr_i
        else:
            break
    return tsum


# sum  triangle for recursive approach
def visited(prev_i, prev_j):
    pass


# altemetrices
def stemming_sentence(text):
    words = text.split()
    for i in range(len(words)):
        if len(words[i]) > 8:
            words[i] = list(words[i])[:8:]
        if words[i].endswith("ly"):
            words[i] = words[i].rstrip("ly")
        if words[i].endswith("ed"):
            words[i] = words[i].rstrip("ed")
        if words[i].endswith("ing"):
            words[i] = words[i].rstrip("ing")
        print(words[i])
    print(" ".join(words))

if __name__ == '__main__':
    # triangle=['1','1 2','4 5 6','5 6 7 8']
    # triangle = ['1', '2 3', '4 5 6', '8 9 12 10', '5 8 7 6 10']
    # res = sumtriangle(triangle)
    # print(res)

    stemming_sentence("a boyrr isly jumping only the boxed")
