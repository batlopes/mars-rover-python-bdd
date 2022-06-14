class Plateau:
    def __init__(self, dimension_x, dimension_y):
        self.__x = dimension_x
        self.__y = dimension_y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def is_valid_position(self, position_x, position_y):
        return 0 <= position_x <= self.x and 0 <= position_y <= self.y
