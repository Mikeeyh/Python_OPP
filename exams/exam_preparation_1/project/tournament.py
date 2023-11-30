from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in ["KneePad", "ElbowPad"]:
            raise Exception("Invalid equipment type!")
        new_equipment = None

        if equipment_type == "KneePad":
            new_equipment = KneePad()
        elif equipment_type == "ElbowPad":
            new_equipment = ElbowPad()

        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in ["OutdoorTeam", "IndoorTeam"]:
            raise Exception("Invalid team type!")
        new_team = None

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        if team_type == "OutdoorTeam":
            new_team = OutdoorTeam(team_name, country, advantage)
        elif team_type == "IndoorTeam":
            new_team = IndoorTeam(team_name, country, advantage)

        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = next((equip for equip in self.equipment if type(equip).__name__ == equipment_type), None)
        if not equipment:
            raise ValueError("Invalid equipment type!")

        team = next((t for t in self.teams if t.name == team_name), None)
        if not team:
            raise ValueError("Team not found!")

        if equipment.price > team.budget:
            raise ValueError("Budget is not enough!")

        team.equipment.append(equipment)
        team.budget -= equipment.price
        self.equipment.remove(equipment)

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)
        if not team:
            raise ValueError("No such team!")

        if team.wins > 0:
            raise ValueError(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipment_count = 0
        for equip in self.equipment:
            if type(equip).__name__ == equipment_type:
                equip.increase_price()
                equipment_count += 1

        return f"Successfully changed {equipment_count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next((t for t in self.teams if t.name == team_name1), None)
        team2 = next((t for t in self.teams if t.name == team_name2), None)

        if not team1 or not team2:
            raise ValueError("One or both teams not found!")

        if type(team1).__name__ != type(team2).__name__:
            raise ValueError("Game cannot start! Team types mismatch!")

        points_team1 = team1.advantage + sum(equip.protection for equip in team1.equipment)
        points_team2 = team2.advantage + sum(equip.protection for equip in team2.equipment)

        if points_team1 > points_team2:
            winner = team1
        elif points_team2 > points_team1:
            winner = team2
        else:
            return "No winner in this game."

        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):
        result = [t.get_statistics() for t in self.teams]
        return '\n'.join(result)

