from solver import AdventSolver


class Day3Solver(AdventSolver):
    def part_1(self, input_data: list[str]) -> str:
        # Implement day 1 solution
        return "(42, 123)"

    """
    The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. 
    Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to 
    the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

    For example:
        1. A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present 
        plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.

        2. A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present 
        plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

    """

    def part_2(self, input_data: list[str]) -> str:
        total = 0
        for dimensions_str in input_data:
            dimensions = [
                int(dimension) if dimension.isdigit() else 0
                for dimension in dimensions_str.split("x")
            ]
            if len(dimensions) == 3:
                total += dimensions[0] * dimensions[1] * dimensions[2]
                dimensions_sorted = sorted(dimensions)
                total += dimensions_sorted[0] * 2 + dimensions_sorted[1] * 2

        return str(total)
