# from project.lion import Lion
# from project.tiger import Tiger
# from project.cheetah import Cheetah
# from project.keeper import Keeper
# from project.caretaker import Caretaker
# from project.vet import Vet
from project.worker import Worker
from project.animal import Animal
from typing import List, Union


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return f"Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary_to_pay = 0
        for w in self.workers:
            total_salary_to_pay += w.salary
        if self.__budget < total_salary_to_pay:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salary_to_pay
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_money_for_care = 0
        for a in self.animals:
            total_money_for_care += a.money_for_care
        if self.__budget < total_money_for_care:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    # def animals_status(self):
    #     lions = []
    #     tigers = []
    #     cheetahs = []
    #
    #     for animal in self.animals:
    #         if animal.__class__.__name__ == "Lion":
    #             lions.append(repr(animal))
    #         elif animal.__class__.__name__ == "Tiger":
    #             tigers.append(repr(animal))
    #         else:
    #             cheetahs.append(repr(animal))
    #
    #     result = [f"You have {len(self.animals)} animals", f"----- {len(lions)} Lions:"]
    #     result.extend(lions)  # adding the list of lions
    #     result.append(f"----- {len(tigers)} Tigers:")
    #     result.extend(tigers)
    #     result.append(f"----- {len(cheetahs)} Cheetahs:")
    #     result.extend(cheetahs)
    #
    #     return "\n".join(result)
    #
    # def workers_status(self):
    #     keepers = []
    #     caretakers = []
    #     vets = []
    #
    #     for worker in self.workers:
    #         if worker.__class__.__name__ == "Keeper":
    #             keepers.append(repr(worker))
    #         elif worker.__class__.__name__ == "Caretaker":
    #             caretakers.append(repr(worker))
    #         else:
    #             vets.append(repr(worker))
    #
    #     result = [f"You have {len(self.workers)} workers", f"----- {len(keepers)} Keepers:"]
    #     result.extend(keepers)  # adding the list of keepers
    #     result.append(f"----- {len(caretakers)} Caretakers:")
    #     result.extend(caretakers)
    #     result.append(f"----- {len(vets)} Vets:")
    #     result.extend(vets)
    #
    #     return "\n".join(result)

    """ You can write a private method in order to write the two methods above """

    def animals_status(self) -> str:
        return self.__print_status(self.animals, "Lion", "Tiger", "Cheetah")

    def workers_status(self) -> str:
        return self.__print_status(self.workers, "Keeper", "Caretaker", "Vet")

    @staticmethod
    def __print_status(category: List[Union[Animal, Worker]], *args):
        elements = {arg: [] for arg in args}
        for element in category:
            elements[element.__class__.__name__].append(repr(element))

        result = [f"You have {len(category)} {str(category[0].__class__.__base__.__name__).lower()}s"]
        for key, value in elements.items():
            result.append(f"----- {len(value)} {key}s:")
            result.extend(value)

        return "\n".join(result)


""" You can use isinstance for the two methods below """

    # def animals_status(self):
    #     total_animals_count = len(self.animals)
    #     amount_of_lions = sum(isinstance(animal, Lion) for animal in self.animals)
    #     amount_of_tigers = sum(isinstance(animal, Tiger) for animal in self.animals)
    #     amount_of_cheetahs = sum(isinstance(animal, Cheetah) for animal in self.animals)
    #
    #     lion_info = "\n".join(str(animal) for animal in self.animals if isinstance(animal, Lion))
    #     tiger_info = "\n".join(str(animal) for animal in self.animals if isinstance(animal, Tiger))
    #     cheetah_info = "\n".join(str(animal) for animal in self.animals if isinstance(animal, Cheetah))
    #
    #     return f"You have {total_animals_count} animals "\
    #            f"\n----- {amount_of_lions} Lions:\n{lion_info}" \
    #            f"\n----- {amount_of_tigers} Tigers:\n{tiger_info}" \
    #            f"\n----- {amount_of_cheetahs} Cheetahs:\n{cheetah_info}"
    #
    # def workers_status(self):
    #     total_workers_count = len(self.workers)
    #     amount_of_keepers = sum(isinstance(worker, Keeper) for worker in self.workers)
    #     amount_of_caretakers = sum(isinstance(worker, Caretaker) for worker in self.workers)
    #     amount_of_vets = sum(isinstance(worker, Vet) for worker in self.workers)
    #
    #     keeper_info = "\n".join(str(worker) for worker in self.workers if isinstance(worker, Keeper))
    #     caretaker_info = "\n".join(str(worker) for worker in self.workers if isinstance(worker, Caretaker))
    #     vet_info = "\n".join(str(worker) for worker in self.workers if isinstance(worker, Vet))
    #
    #     return f"You have {total_workers_count} workers " \
    #            f"\n----- {amount_of_keepers} Keepers:\n{keeper_info}" \
    #            f"\n----- {amount_of_caretakers} Caretakers:\n{caretaker_info}" \
    #            f"\n----- {amount_of_vets} Vets:\n{vet_info}"
