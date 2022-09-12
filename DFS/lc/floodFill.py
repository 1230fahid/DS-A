class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if ((sr < 0) or (sr >= len(image)) or (sc < 0) or (sc >= len(image[sr])) or (image[sr][sc] == color)):
            return image
        num = image[sr][sc]
        
        self.flood(image,sr,sc,color,num)
        return image
    
    def flood(self, image, sr, sc, color, num):
        if ((sr < 0) or (sr >= len(image)) or (sc < 0) or (sc >= len(image[sr])) or (image[sr][sc] != num)):
            return
        image[sr][sc] = color
        self.flood(image, sr+1, sc, color, num)
        self.flood(image, sr, sc+1, color, num)
        self.flood(image, sr-1, sc, color, num)
        self.flood(image, sr, sc-1, color, num)
