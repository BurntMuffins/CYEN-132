class Shape:
    def __init__(self, l:int, w:int):
        '''
        This inits the rectangle with a specific length and width

        l = length
        w = width

        '''
        # Self is referred to as the current instance
        self.length = l
        self.width = w

    def draw(self):
        for i in range(self.width):
            print('* '*self.length)
        print()

        # count = 0
        # while count <= self.length:
        #     print('*'*self.width)
        #     count += 1

class Rectangle(Shape):
    def __init__(self, l: int, w: int):
        super().__init__(l, w)

class Square(Shape):
    def __init__(self, l: int):
        super().__init__(l, l)

class Triangle(Shape):
    def __init__(self, l: int):
        super().__init__(l, l)

    def draw(self):
        for i in range(self.length):
            print('* ' * (self.width - i))
        print()

        # count = self.length
        # while count > 0:
        #     print('* '*count)
        #     count -= 1
        # print()



    


r1 = Rectangle(10, 4)
r1.draw()

s1 = Square(5)
s1.draw()

t1 = Triangle(5)
t1.draw()
