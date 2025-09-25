class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        original_image = image[sr][sc]
        if(original_image==color):
            return image
        def dfs(r,c):
            if r<0 or c<0 or r>=len(image) or c>=len(image[0]) or image[r][c] != original_image:
                return
            image[r][c]=color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        dfs(sr,sc)
        return image

            
        
