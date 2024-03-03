delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

direction = [[2, 0, 3, 1],
             [1, 2, 3, 0],
             [1, 3, 0, 2],
             [3, 0, 1, 2],
             [1, 0, 3, 2]]

def findnew(x, y, block, k):
    global score
    # 블록이라면 방향바꾸고 점수 추가
    if 1 <= block <= 5:
        k = direction[block - 1][k]
        score += 1
    # 웜홀이라면 위치 이동
    elif block >= 6:
        for i, j in hole[block]:
            if i != x and j != y:
                x, y = i, j
                break




# k = delta index
def move(x, y, k):
    score = 0
    nx, ny = x + delta[k][0], y + delta[k][1]
    while True:
        # print(nx, ny)
        # 종료 조건
        if nx == x and ny == y:
            return score
        if (nx, ny) in black:
            return score

        # if k == 0:
        #     # 해당 방향으로 빈 공간이 아닌게 존재하다면
        #     # 방향 옮겨주고 for문 끝냄
        #     for i in range(x, n):
        #         if board[i][y] != 0:



        # 벽 부딪히면 점수 추가
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            score += 1
            k = direction[4][k]

        # 블록 부딪히면 점수 추가
        elif 1 <= board[nx][ny] <= 5:
            score += 1
            k = direction[board[nx][ny] - 1][k]

        # 웜홀 빠지면 위치 변경
        elif board[nx][ny] >= 6:
            idx_list = hole[board[nx][ny]]
            for i, j in idx_list:
                if i != nx or j != ny:
                    nx, ny = i, j
                    break

        nx += delta[k][0]
        ny += delta[k][1]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # -1 = 블랙홀, 1~5 = 블록, 6~10 = 웜홀
    board = [list(map(int,input().split())) for _ in range(n)]

    # 웜홀과 블랙홀 위치 받아놓기
    hole = {}
    black = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 6:
                if board[i][j] in hole:
                    hole[board[i][j]].append((i,j))
                else:
                    hole[board[i][j]] = [(i, j)]
            elif board[i][j] == -1:
                black.append((i, j))
    # print(black, hole)
    res = 0
    # i, j = 시작 위치
    # k = 이동 방향
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                for k in range(4):
                    score = move(i,j,k)
                    # print(score)
                    res = max(res, score)
    print(f'#{tc}',res)
