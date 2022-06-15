from src.Plateau import Plateau


class Rover:
    def __init__(
        self, position_x: int, position_y: int, direction: str, plateau: Plateau
    ):
        self.__position_x = position_x
        self.__position_y = position_y
        self.__direction = direction
        self.__plateau = plateau

    @property
    def direction(self):
        return self.__direction

    @property
    def position_x(self):
        return self.__position_x

    @property
    def position_y(self):
        return self.__position_y

    def __turn_right(self):
        directions = {"N": "E", "E": "S", "S": "W", "W": "N"}
        self.__direction = directions[self.__direction]

    def __turn_left(self):
        directions = {"N": "W", "W": "S", "S": "E", "E": "N"}
        self.__direction = directions[self.__direction]

    def __move(self):
        future_position = [self.__position_x, self.__position_y]
        if self.__direction == "N":
            future_position[1] += 1
        elif self.__direction == "S":
            future_position[1] -= 1
        elif self.__direction == "E":
            future_position[0] += 1
        elif self.__direction == "W":
            future_position[0] -= 1

        if self.__plateau.is_valid_position(future_position[0], future_position[1]):
            self.__position_x = future_position[0]
            self.__position_y = future_position[1]

    def navigate(self, commands: str):
        for command in commands:
            if command == "L":
                self.__turn_left()
            elif command == "R":
                self.__turn_right()
            elif command == "M":
                self.__move()
