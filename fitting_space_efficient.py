import global_space_efficient

def find_start(v, w, delta, i1, j1):
    vp = v[0:i1:][::-1]
    wp = w[0:j1:][::-1]
    dp = [[-114514 for j in range(len(wp) + 1)] for i in range(2)]
    curr = 0
    # print(vp, wp)
    for i in range(len(vp) + 1):
        for j in range(len(wp) + 1):
            dp[curr][j] = -114514
            if i == 0 and j == 0:
                dp[curr][j] = 0
            elif i == 0:
                dp[curr][j] = max(dp[curr][j], dp[curr][j - 1] + delta['-'][wp[j - 1]])
            elif j == 0:
                dp[curr][j] = max(dp[curr][j], dp[1 - curr][j] + delta[vp[i - 1]]['-'])
            else:
                dp[curr][j] = max(dp[curr][j], dp[1 - curr][j] + delta[vp[i - 1]]['-'])
                dp[curr][j] = max(dp[curr][j], dp[curr][j - 1] + delta['-'][wp[j - 1]])
                dp[curr][j] = max(dp[curr][j], dp[1 - curr][j - 1] + delta[vp[i - 1]][wp[j - 1]])
        # print(dp[curr])
        curr = 1 - curr
    ret = -1
    big = -1919810
    for j in range(len(wp) + 1):
        if dp[1 - curr][j] >= big:
            big = dp[1 - curr][j]
            ret = j
    return (0, j1 - ret)

def find_end(v, w, delta):
    dp = [[-114514 for j in range(len(w) + 1)] for i in range(2)]
    curr = 0
    for i in range(len(v) + 1):
        for j in range(len(w) + 1):
            dp[curr][j] = -114514
            if i == 0:
                dp[curr][j] = 0
            else:
                dp[curr][j] = max(dp[curr][j], dp[1 - curr][j] + delta[v[i - 1]]['-'])
                if j > 0:
                    dp[curr][j] = max(dp[curr][j], dp[curr][j - 1] + delta['-'][w[j - 1]])
                    dp[curr][j] = max(dp[curr][j], dp[1 - curr][j - 1] + delta[v[i - 1]][w[j - 1]])
        # print(dp[curr])
        curr = 1 - curr
    # print("----------------")
    ret = -1
    big = -1919810
    for j in range(len(w) + 1):
        if dp[1 - curr][j] >= big:
            big = dp[1 - curr][j]
            ret = j
    return (len(v), ret)

def fitting(v, w, delta):
    (i1, j1) = find_end(v, w, delta)
    (i0, j0) = find_start(v, w, delta, i1, j1)
    # print(i0, j0, i1, j1)
    h = global_space_efficient.hirschberg(v[i0:i1:], w[j0:j1:], delta)
    a = global_space_efficient.get_alignment(v[i0:i1:], w[j0:j1:], h)
    return a