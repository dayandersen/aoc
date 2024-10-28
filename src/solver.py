from abc import ABC, abstractmethod


class AdventSolver(ABC):
    @abstractmethod
    def part_1(self, input_data: list[str]) -> str:
        """
        Solve day 1 puzzles
        Args:
            input_data: The puzzle input as a string
        Returns:
            tuple containing answers for part 1 and part 2
        """
        pass

    @abstractmethod
    def part_2(self, input_data: list[str]) -> str:
        """
        Solve day 2 puzzles
        Args:
            input_data: The puzzle input as a string
        Returns:
            tuple containing answers for part 1 and part 2
        """
        pass
