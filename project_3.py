EMPTY = 1
PLAYERX = 2
PLAYERO = 3 
DRAW = 4
STRMAP = {EMPTY: "",PLAYERX: "X",PLAYER0:"0"}  
class TTTBoard:
    """
    Class to represent a Tic-Tac-Toe board.
    """

    def __init__(self, dim, reverse = False, board = None):
        """
        Initialize the TTTBoard object with the given dimension and 
        whether or not the game should be reversed.
        """
        self.dim = dim
        self._reverse = reverse
        if self.board == None:
             self._board = [[EMPTY for row in self.dim]for col in self.dim] 
        else:
             self._board =[[board[row][col] for row in range(dim)]for col in range(dim)]   
        return self._board
    
    def __str__(self):
        """
        Human readable representation of the board.
        """
        rep =""
        for row in range(self.dim):
           for col in range(self.dim):
               rep += STRMAP(self.board[row][col])
               if col == self.dim-1:
                   rep += "\n"
               else:
                   rep += "|"
           if row == self.dim-1:
              rep += "-"*(4*self.dim - 3)
              rep += "\n"  

    def get_dim(self):
        """
        Return the dimension of the board.
         """
        return self.dim          
    
    def square(self, row, col):
        """
        Returns one of the three constants EMPTY, PLAYERX, or PLAYERO 
        that correspond to the contents of the board at position (row, col).
          """
        return self._board[row][col]

    def get_empty_squares(self):
        """
        Return a list of (row, col) tuples for all empty squares
        """
        empty =[]
        for row in range(self.dim):
            for col in range(self.dim): 
                if self._board[row][col] == EMPTY:
                      empty.append(self._board[row][col])             
        return empty 
    def move(self, row, col, player):
        """
        Place player on the board at position (row, col).
        player should be either the constant PLAYERX or PLAYERO.
        Does nothing if board square is not empty.
        """
        if self._board[row][col] == EMPTY
               self._board[row][col] == player 

    def check_win(self):
        """
        Returns a constant associated with the state of the game
            If PLAYERX wins, returns PLAYERX.
            If PLAYERO wins, returns PLAYERO.
            If game is drawn, returns DRAW.
            If game is in progress, returns None.
        """
        line =[]
        line.append(self._board)
      
        cols = [[self._board[rowidx][colidx] for rowidx in range(self.dim)] for colidx in range(self.dim)] 
        line.append(col)         
        
        dia1 = [self._board [idx][idx] for idx in range(self.dim)]
        dia2 = [self.board [idx][self.dim-idx-1] for idx in range(self.dim)]   
        line.append(dia1)
        line.append(dia2)
        
        for l in line:
           if len(set(l)) == 1 and l[0] != EMPTY:
                if self._reverse :
                   return switch_player(l[0]) 
                else:
                   return l[0]    
        if  len(self.get_empty_squrare) == 0:
               return draw  
                                         
    def clone(self):
        """
        Return a copy of the board.
        """

