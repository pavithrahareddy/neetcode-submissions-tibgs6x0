class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = defaultdict(list)
        c = defaultdict(list)
        rc = defaultdict(list)
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in r[i] or board[i][j] in c[j] or board[i][j] in rc[tuple([i//3,j//3])]:
                    return False
                r[i].append(board[i][j])
                c[j].append(board[i][j])
                rc[tuple([i//3,j//3])].append(board[i][j])
        return True
        