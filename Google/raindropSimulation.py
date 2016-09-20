# you have 1 meter walkroad, and randomly generate rain,the rain is 1 cm.
# simulate how many rain drops to cover all the 1 meter [-0.01~1]


# 假设一个WALK是由100 个INTERVEL 组成
# 每一个INTERVAL 表示了 0-0.01的区间
# 第I个 INTERVAL 所表示的实际区间就是 I*0.01
class interval(object):

    def __init__(self):
        # LEFT代表在这个区间内从0到LEFT 被COVER的部分
        self.left = 0.0
        # RIGHT代表在这个区间内从RIGHT到0.01 被COVER的部分

        self.right = 0.01

    # 对于一个区间 如果他的左
    def isWet(self):
        return True if self.left >= self.right else False


import random


def rainDropSimulator():
    walk = []
    for i in range(100):
        walk.append(interval())

    wetCnt = 0
    rainCnt = 0

    while wetCnt < 100:
        rainCnt += 1
        drop = random.uniform(0, 1)

        # 随机出来的DROP值表示了 该雨滴的原点
        # 左右表示了这个雨滴的直径范围
        left = drop - 0.005
        right = drop + 0.005

        if left >= 0:
                # 得到左半径所在区间
            LeftIntervalIndex = int(left / 0.01)
            if not walk[LeftIntervalIndex].isWet():
                newRight = left - LeftIntervalIndex * 0.01
                # 判断这个左半径是否有COVER该区间从右往左更多的区域
                walk[LeftIntervalIndex].right = min(walk[LeftIntervalIndex].right, newRight)
                if walk[LeftIntervalIndex].isWet():
                    wetCnt += 1

        if right <= 1:
                # 得到右半径所在的区间
            RightIntervalIndex = int(right / 0.01)
            # print(RightIntervalIndex)
            if not walk[RightIntervalIndex].isWet():
                newlLeft = right - RightIntervalIndex * 0.01
                # 判断这个右半径是否有COVER该区间从左往右更多的区域
                walk[RightIntervalIndex].left = max(walk[RightIntervalIndex].left, newlLeft)
                if walk[RightIntervalIndex].isWet():
                    wetCnt += 1
        # print(wetCnt)
    print(rainCnt)


rainDropSimulator()
