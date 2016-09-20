class SnakeGame(object):

    def __init__(self, width, height, food):
        self.food = food
        self.width = width
        self.height = height
        self.snakeQueue = [[0, 0]]
        self.foodI = 0

    def move(self, direction):
        nextPo = self.snakeQueue[-1][::]

        if direction == "U":
            nextPo[0] -= 1
        if direction == "R":
            nextPo[1] += 1
        if direction == "L":
            nextPo[1] -= 1
        if direction == "D":
            nextPo[0] += 1

        # print(nextPo)
        if nextPo[0] < 0 or nextPo[0] == self.height or nextPo[1] < 0 or nextPo[1] ==self.width:
            return -1

        if self.foodI < len(self.food) and nextPo == self.food[self.foodI]:

            self.snakeQueue.append(nextPo)
            self.foodI += 1
            return self.foodI

        self.snakeQueue.pop(0)

        if nextPo in self.snakeQueue:
            return -1
        else:
            self.snakeQueue.append(nextPo)

        return self.foodI


width = 2
height = 1
food = [[0,1]]

testClass = SnakeGame(width, height, food)

print(testClass.move("R"))
# print(testClass.move("D"))
print(testClass.move("R"))
# print(testClass.move("U"))
# print(testClass.move("L"))
# print(testClass.move("U"))


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
