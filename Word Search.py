from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r: int, c: int, index: int) -> bool:
            # Base case: All characters matched
            if index == len(word):
                return True
            
            # Check boundaries and character match
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                board[r][c] != word[index]):
                return False

            # Mark the cell as visited temporarily
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all four directions
            found = (backtrack(r + 1, c, index + 1) or
                     backtrack(r - 1, c, index + 1) or
                     backtrack(r, c + 1, index + 1) or
                     backtrack(r, c - 1, index + 1))

            # Restore the cell value
            board[r][c] = temp
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:  # Start search if first letter matches
                    if backtrack(i, j, 0):
                        return True

        return False
