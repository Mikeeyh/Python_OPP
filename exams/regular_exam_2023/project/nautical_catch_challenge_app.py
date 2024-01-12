from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.divers.base_diver import BaseDiver
from typing import List


class NauticalCatchChallengeApp:
    VALID_DIVERS_TYPE = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISHES_TYPE = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVERS_TYPE:
            return f"{diver_type} is not allowed in our competition."

        diver = next((d for d in self.divers if d.name == diver_name), None)
        if diver:
            return f"{diver_name} is already a participant."

        if diver_type == "FreeDiver":
            new_diver = FreeDiver(diver_name)
        else:
            new_diver = ScubaDiver(diver_name)

        self.divers.append(new_diver)

        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISHES_TYPE:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if fish:
            return f"{fish_name} is already permitted."

        if fish_type == "PredatoryFish":
            new_fish = PredatoryFish(fish_name, points)
        else:
            new_fish = DeepSeaFish(fish_name, points)

        self.fish_list.append(new_fish)

        return f" {fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        if not diver:
            return f"{diver_name} is not registered for the competition."

        fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            result = f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                result = f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                result = f"{diver_name} missed a good {fish_name}."

        else:
            diver.hit(fish)
            result = f"{diver_name} hits a {fish.points}pt. {fish_name}."

        if diver.oxygen_level == 0:
            diver.has_health_issue = True

        return result

    def health_recovery(self):
        count = 0
        for current_diver in self.divers:
            if current_diver.has_health_issue:
                current_diver.update_health_status()
                current_diver.renew_oxy()
                count += 1
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        if diver:
            diver_fish_details = "\n".join([fish.fish_details() for fish in diver.catch])
            final_result = f"**{diver_name} Catch Report**\n{diver_fish_details}"
            return final_result

    def competition_statistics(self):
        divers_in_good_health_list = [found_diver for found_diver in self.divers if not found_diver.has_health_issue]
        sorted_divers_list = sorted(
            divers_in_good_health_list,
            key=lambda diver: (-diver.competition_points, -len(diver.catch), diver.name))
        divers_catch_statistics = [str(diver) for diver in sorted_divers_list]
        final_divers_statistics_result = "\n".join(divers_catch_statistics)
        return f"**Nautical Catch Challenge Statistics**\n{final_divers_statistics_result}"
