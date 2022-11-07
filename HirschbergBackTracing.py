
keys = ['A', 'C', 'T', 'G', '-']
delta = {}
for i in range(len(keys)):
    delta[keys[i]] = {k : v for (k,v) in zip(keys, [1 if keys[i] == keys[j]  else -1 for j in range(len(keys))])}
delta['-']['-'] = -1

# global variable to store reported points
# report[col_idx] = row_idx
report = {}
path = []

def Hirschberg(i0, j0, i1, j1):
    i_star = argmax()
    report[(j0 + (j1 - j0) / 2)] = i_star
    return

def traceBack(v, w):
    m = len(v)
    n = len(w)
    set = {}
    for value in report:
        set.add(value) 
    for key, value in report:
        set.add(value)
        path.append((value, key))
    prev = 0
    queue = False
    for col in range(n + 1):
        if report[col] in set:
            if queue == True:
                fillRows(v, w, report[prev], prev, report[col], col)
            queue = False
            prev = col
        else:
            queue = True   
    return path

# Find a list of points which represents the alignment path
# input: string w, string v, indexs in w(i0, i1), indexs in v(j0, j1) where j1 = j0 + 1
# output: 
def fillRows(v, w, i0, i1, j0, j1):
    m = i1 - i0 + 1
    n = j1 - j0 + 1
    s = [[0] * (n + 1) for i in range(m + 1)]
    dir = [[] * (n + 1) for i in range(m + 1)]
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            up = s[i - 1][j] + delta[v[i0 + i - 1], '-']
            left = s[i][j - 1] + delta['-', w[j0 + j - 1]]
            upLeft = s[i - 1][j - 1] + delta[v[i0 + i - 1], w[j0 + j - 1]]
            maxScore = max(up, left, upLeft)
            s[i - i0][1] = maxScore
            if maxScore == up:
                dir[i - i0][1] = "UP"
            elif maxScore == left:
                dir[i - i0][1] = "LEFT"
            else:
                dir[i - i0][1] = "UPLEFT"
    curCol = j1
    curRow = i1
    while (curRow >= i0):
        if (report[curCol] != curRow):
            path.append(curRow, curCol)
        if dir[curRow][curCol] == "UP":
            curRow -= 1
        elif dir[i][curCol] == "left":
            curCol -= 1
        else:
            curRow -= 1
            curCol -= 1
    return
