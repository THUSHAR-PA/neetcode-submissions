class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #Row check 
        for i in range(len(board)):
            seen =set()
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
        

        #Column Check
        for i in range(len(board)):
            seen =set()
            for j in range(len(board[0])):
                if board[j][i] == '.':
                    continue
                if board[j][i] in seen:
                    return False
                else:
                    seen.add(board[j][i])

        #Box Check
        for row in range(0,9,3):
            for col in range(0,9,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        value = board[row+i][col+j]

                        if value =='.':
                            continue
                        if value in seen:
                            return False
                        else:
                            seen.add(value)

        return True