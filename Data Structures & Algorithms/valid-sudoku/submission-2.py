class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = defaultdict(list)
        c = defaultdict(list)
        rc = defaultdict(list)
        for row in range(0,9):
            for col in range(0,9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in r[row] or board[row][col] in c[col] or board[row][col] in rc[tuple([row//3,col//3])]:
                    return False
                r[row].append(board[row][col])
                c[col].append(board[row][col])
                rc[tuple([row//3,col//3])].append(board[row][col])
        return True
        