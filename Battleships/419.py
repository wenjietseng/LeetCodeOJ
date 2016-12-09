class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # Check the left and upper position of each point
        ship = 0
        if len(board) == 0:
            return 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                        ship += 1
        return ship
