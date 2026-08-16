import math


class HandRotation:

    @staticmethod
    def get_rotation(lmList):

        baseX = lmList[5][1]
        baseY = lmList[5][2]

        tipX = lmList[8][1]
        tipY = lmList[8][2]

        dx = tipX - baseX
        dy = tipY - baseY

        return math.atan2(dy, dx)