from project.equipment.base_equipment import BaseEquipment
from project.teams.base_team import BaseTeam
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam
from typing import List


class Tournament:
    VALID_EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")

        new_equipment = self.VALID_EQUIPMENT_TYPES[equipment_type]()  # KneePad() or ElbowPad()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAM_TYPES:
            raise Exception("Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        new_team = self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)
        equipment = next((e for e in reversed(self.equipment) if e.__class__.__name__ == equipment_type), None)

        if equipment.price > team.budget:
            raise ValueError("Budget is not enough!")
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)
        if team is None:
            raise ValueError("No such team!")
        if team.wins > 0:
            raise ValueError(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        e_count = 0
        for e in self.equipment:
            if e.__class__.__name__ == equipment_type:
                e.increase_price()
                e_count += 1
        return f"Successfully changed {e_count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next((t for t in self.teams if t.name == team_name1), None)
        team2 = next((t for t in self.teams if t.name == team_name2), None)

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise ValueError("Game cannot start! Team types mismatch!")

        team1_points = self.get_team_points(team1)
        team2_points = self.get_team_points(team2)

        if team1_points > team2_points:
            winner = team1
        elif team2_points > team1_points:
            winner = team2
        else:
            return "No winner in this game."

        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):
        teams = sorted(self.teams, key=lambda t: -t.wins)
        # sorted by number of wins, descending. OR: key=lambda t: t.wins, reverse=True
        result = [f"Tournament: {self.name}",
                  f"Number of Teams: {len(self.teams)}",
                  f"Teams:"]

        [result.append(t.get_statistics()) for t in teams]
        return "\n".join(result)

    @staticmethod
    def get_team_points(team: BaseTeam):
        return team.advantage + sum(e.protection for e in team.equipment)
