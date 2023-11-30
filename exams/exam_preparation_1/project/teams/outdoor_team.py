from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=1000.0)

    def win(self):
        self.advantage += 115
        self.wins += 1

    def get_statistics(self):
        total_price_of_team_equipment = sum([protec.price for protec in self.equipment])
        total_protection = sum([protec.protection for protec in self.equipment])
        if len(self.equipment) >= 1:
            avg_team_protection = total_protection / len(self.equipment)
        else:
            avg_team_protection = 0

        result = \
            f"Name: {self.name}\n" \
            f"Country: {self.country}\n" \
            f"Advantage: {int(self.advantage)} points\n" \
            f"Budget: {self.budget:.2f}EUR\n" \
            f"Wins: {self.wins}\n" \
            f"Total Equipment Price: {total_price_of_team_equipment:.2f}\n" \
            f"Average Protection: {avg_team_protection}"
        return result
