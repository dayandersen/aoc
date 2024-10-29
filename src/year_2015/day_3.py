from solver import AdventSolver


class Day3Solver(AdventSolver):
    """
    Moves are always exactly one house to the north (^), south (v), east (>), or west (<).
    After each move, he delivers another present to the house at his new location.
    However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off,
    and Santa ends up visiting some houses more than once. How many houses receive at least one present?

    For example:

        > delivers presents to 2 houses: one at the starting location, and one to the east.
        ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
        ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

    """

    def part_1(self, input_data: list[str]) -> str:
        coords = (0, 0)
        visited = set()
        visited.add(coords)
        dirs = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}
        for direction in input_data[0]:
            change = dirs[direction] if direction in dirs else (0, 0)
            coords = (coords[0] + change[0], coords[1] + change[1])
            visited.add(coords)
        return str(len(visited))

    def part_2(self, input_data: list[str]) -> str:
        coords_1 = (0, 0)
        coords_2 = (0, 0)
        visited = set()
        visited.add(coords_1)
        flip_flop = False
        dirs = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}
        for direction in input_data[0]:
            change = dirs[direction] if direction in dirs else (0, 0)

            if flip_flop == False:
                coords_1 = (coords_1[0] + change[0], coords_1[1] + change[1])
                visited.add(coords_1)
            else:
                coords_2 = (coords_2[0] + change[0], coords_2[1] + change[1])
                visited.add(coords_2)

            flip_flop = not flip_flop

        return str(len(visited))
