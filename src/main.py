from src.Rover import Rover
from src.Plateau import Plateau


if __name__ == "__main__":
    plateau_dimensions = input("Digite as dimensões do plateau: ").split(" ")
    plateau_x = int(plateau_dimensions[0])
    plateau_y = int(plateau_dimensions[1])
    plateau = Plateau(plateau_x, plateau_y)
    while True:
        rover_position = input(
            "Digite a posição e a direção iniciais do rover: "
        ).split(" ")
        if rover_position[0].lower() == "exit":
            break
        rover_x = int(rover_position[0])
        rover_y = int(rover_position[1])
        rover_direction = rover_position[2].upper()
        rover = Rover(rover_x, rover_y, rover_direction, plateau)
        rover_commands = input("Digite os comandos do rover: ")
        rover.navigate(rover_commands)
        print(f"Posição final: {rover.position_x} {rover.position_y} {rover.direction}")
        print("-----------------------------------------------------")
