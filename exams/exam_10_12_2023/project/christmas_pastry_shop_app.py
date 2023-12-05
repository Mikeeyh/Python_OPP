from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from typing import List


class ChristmasPastryShopApp:
    VALID_DELICACIES_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTHS_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy = next((d for d in self.delicacies if d.name == name), None)
        if delicacy:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in self.VALID_DELICACIES_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = self.VALID_DELICACIES_TYPES[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.VALID_BOOTHS_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = self.VALID_BOOTHS_TYPES[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = next((b for b in self.booths if b.capacity >= number_of_people and not b.is_reserved), None)
        if booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)
        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next(b for b in self.booths if b.booth_number == booth_number)
        bills_for_booth_reservation = booth.price_for_reservation
        bills_for_delicacy = sum(d.price for d in booth.delicacy_orders)
        total_bill = bills_for_booth_reservation + bills_for_delicacy
        self.income += total_bill

        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False

        return f"Booth {booth_number}:\nBill: {total_bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
