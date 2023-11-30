from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=500.0)

    def win(self):
        self.advantage += 145
        self.wins += 1

    def get_statistics(self):
        pass
