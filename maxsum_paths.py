def maxPathScore(board):
    MOD = 10**9 + 7
    n = len(board)

    dp_sum = [[-1] * n for _ in range(n)]
    dp_cnt = [[0] * n for _ in range(n)]

    # locate S and E
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'S':
                sr, sc = r, c
            if board[r][c] == 'E':
                er, ec = r, c

    # starting point has sum = 0, count = 1
    dp_sum[sr][sc] = 0
    dp_cnt[sr][sc] = 1

    # iterate from bottom-right to top-left
    for r in range(n-1, -1, -1):
        for c in range(n-1, -1, -1):

            if board[r][c] == 'X': 
                continue

            if dp_sum[r][c] < 0: 
                continue

            for dr, dc in [(-1, 0), (0, -1), (-1, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 'X':

                    val = 0
                    if board[nr][nc].isdigit():
                        val = int(board[nr][nc])

                    newSum = dp_sum[r][c] + val

                    # update best sum
                    if newSum > dp_sum[nr][nc]:
                        dp_sum[nr][nc] = newSum
                        dp_cnt[nr][nc] = dp_cnt[r][c]
                    elif newSum == dp_sum[nr][nc]:
                        dp_cnt[nr][nc] = (dp_cnt[nr][nc] + dp_cnt[r][c]) % MOD

    if dp_sum[er][ec] < 0:
        return [0, 0]
    return [dp_sum[er][ec], dp_cnt[er][ec] % MOD]

# ---- TEST CASES ----
board1 = ["E23","2X2","12S"]
board2 = ["E12","1X1","21S"]
board3 = ["E11","XXX","11S"]

print(maxPathScore(board1))  # Expected [7, 1]
print(maxPathScore(board2))  # Expected [4, 2]
print(maxPathScore(board3))  # Expected [0, 0]
