# 3 * 3 棋盘井字棋游戏，X先行。判断给出棋盘是否可能出现
from typing import List
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        countX, countO = 0, 0

        # check count
        for i in board:
            if i == '   ':
                continue
            for j in i:
                if j == 'X':
                    countX += 1
                elif j == 'O':
                    countO += 1
        # X 数目小 或者 X比O多1个以上 则不符合 
        if countX - countO < 0 or countX - countO > 1:
            return False
        
        # 当O数目到达3时，X & O都会到达3个 - 判定输赢情况
        if countO >=3:
            X = self.check(board,'X')
            O = self.check(board,'O')

            # xo 同赢
            if  X and O:
                return False
            # X赢 X必须比O多1
            if X and countX != countO + 1:
                return False
            # O赢 O 必须和X数目一样
            if O and countX != countO:
                return False

        return True

    def check(self, board, n):
        for i in range(3):

            if board[i][0] == board[i][1] == board[i][2] == n:
                return True
            if board[0][i] == board[1][i] == board[2][i] == n:
                return True
            
        if board[0][0] == board[1][1] == board[2][2] == n:
            return True
        if board[0][2] == board[1][1] == board[2][0] == n:
            return True
        
        return False