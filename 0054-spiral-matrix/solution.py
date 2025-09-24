class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        result = []
        
        # Define boundaries
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        while top <= bottom and left <= right:
            # Traverse right along top row
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            
            # Traverse down along right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # Traverse left along bottom row (if we still have rows)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
            
            # Traverse up along left column (if we still have columns)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result
