class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flipped_img = [row[::-1] for row in image]

        for i in range(len(image)):
            for j in range(len(image[0])):
                flipped_img[i][j] += -1 if flipped_img[i][j] else 1

        return flipped_img
