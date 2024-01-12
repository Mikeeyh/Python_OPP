from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, oxygen_level=120)

    def miss(self, time_to_catch: int):
        reduction = 0.6 * time_to_catch
        rounded_reduction = round(reduction) if isinstance(reduction, float) else int(reduction)

        if self.oxygen_level - rounded_reduction < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= rounded_reduction

    def renew_oxy(self):
        self.oxygen_level = 120
