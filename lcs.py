def lcs(X: str,Y: str,m:int,n: int)-> int:
    if m == 0 or n == 0:
        return 0
    if X[m-1] == Y[n-1]:
        return 1+ lcs(X,Y,m-1,n-1)

    return max(lcs(X,Y,m-1,n),lcs(X,Y,m,n-1))
    
def lcs_dp(X: str,Y: str,m:int,n: int) -> int:
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]
    
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS (Recursive):", lcs_dp(X, Y, len(X), len(Y)))