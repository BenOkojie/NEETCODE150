class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(len(board)):
            s = set()
            for y in range(len(board)):
                if board[x][y] != ".":
                    if board[x][y] in s:
                        return False
                    else:
                        s.add(board[x][y])
        for x in range(len(board)):
            s = set()
            for y in range(len(board)):
                if board[y][x] != ".":
                    if board[y][x] in s:
                        return False
                    else:
                        s.add(board[y][x])
        xincrement = 0
        yincrement = 0
        for i in range(len(board)):
            s= set()
            if i%3==0:
                yincrement = i
                xincrement=(i%3)*3
            else:
                xincrement = (i%3)*3
            for y in range(3):
                for x in range(3):
                    if board[y+yincrement][x+xincrement] != ".":
                        if board[y+yincrement][x+xincrement] in s:
                            return False
                        else:
                            s.add(board[y+yincrement][x+xincrement])
        return True


