class HandPosition:

    @staticmethod
    def get_palm_center(lmList):

        points = [0, 5, 9, 13, 17]

        palmX = 0
        palmY = 0

        for p in points:

            palmX += lmList[p][1]
            palmY += lmList[p][2]

        palmX //= len(points)
        palmY //= len(points)

        return palmX, palmY