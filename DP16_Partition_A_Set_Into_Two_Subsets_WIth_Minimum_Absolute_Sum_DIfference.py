"""
Coding Monk - https://www.codingninjas.com/studio/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494?source=youtube&campaign=striver_dp_videos&leftPanelTab=1
Level - Hard 
"""

from typing import List

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    # write your code here
    # calculate sum of all the elements of array
    target = sum(arr)
    min_diff = float('inf')
    # create DP Array
    dp = [[False for i in range(target+1)] for j in range(n)]

    # Initialize dp[i][0] to True
    for i in range(n):
        dp[i][0] = 0
    # print(target, n, len(dp), len(dp[0]))
    if arr[0]<=target:
        dp[0][arr[0]] = True

    for i in range(1, n):
        for j in range(1, target+1):
            not_take = dp[i-1][j]
            take = False
            if j>=arr[i]:
                take = dp[i-1][j-arr[i]]
            dp[i][j] = take or not_take
        #     print(dp[i][j], end =" ")
        # print()
    min_diff = float('inf')
    for i in range(target+1):
        if dp[n-1][i] == True:
            sum1 = i
            sum2 = target - i
            min_diff = min(min_diff, abs(sum1-sum2))
    return min_diff

    