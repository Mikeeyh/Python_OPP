from abc import ABC, abstractmethod


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self. advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @abstractmethod
    def get_statistics(self):
        total_price_of_team_equipment = sum([protec.price for protec in self.equipment])
        total_protection = sum([protec.protection for protec in self.equipment])
        avg_team_protection = total_protection / len(self.equipment)

        result = \
            f"Name: {self.name}\n" \
            f"Country: {self.country}\n" \
            f"Advantage: {self.advantage} points\n" \
            f"Budget: {self.budget:.2f}EUR\n" \
            f"Wins: {self.wins}\n" \
            f"Total Equipment Price: {total_price_of_team_equipment:.2f}\n" \
            f"Average Protection: {avg_team_protection}"
        return result
