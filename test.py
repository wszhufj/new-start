# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n = 19
price = [0, 1, 5 ,8 ,9, 10, 17, 17, 20, 24, 30, 33]
dp = [0 for i in range(n + 1)]
dp[:len(price)] = price
cut = [[0, 0] for i in range(n + 1)]
res = []

for i in range(2, n + 1):
    for j in range(1, i):
        if dp[j] + dp[i - j] > dp[i]:
            dp[i] = dp[j] + dp[i - j]
            cut[i].pop()
            cut[i].pop()
            cut[i].append(j)
            cut[i].append(i - j)
             
def cutrod(i):
    if i == 0:
        return
    if cut[i] == [0, 0]:
        res.append(i)
    cutrod(cut[i][0])
    cutrod(cut[i][1])

cutrod(n)