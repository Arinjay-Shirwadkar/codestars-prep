class Solution:
                  def solveNQueens(self, n: int) -> List[List[str]]:
                      #Instead of checking every combination of placing a queen, which would be ridiculous, we will pl
              #mm, maybe I could add all indices of the 4 diagonals when a valid queen was found. However, removing th

                      sol=[]
                      board=[]
                      cols={}
                      placed=[]

                      for i in range(0,n):
                          board.append(['.']*n)

                      def dfs(i,j):

                          if len(placed)==n:
                              sol.append(["".join(row) for row in board])
                              return

                          if i>=n or j>=n:
                              return

                          flag = True
                          #check if i,j is valid
                          if j not in cols:
                              for x,y in placed:
                                  diff = abs(i-x),abs(j-y)
                                  if diff[0]==diff[1]:
                                      flag = False
                                      break
                          else:
                              flag = False

                          if flag:
                              #valid index found
                              cols[j]=1
                              placed.append((i,j))
                              board[i][j]='Q'
                              dfs(i+1,0)
                              cols.pop(j)
                              placed.pop()
                              board[i][j]='.'

                          if j<n-1 and i<n:
                              dfs(i,j+1)

                      dfs(0,0)
                      return sol
