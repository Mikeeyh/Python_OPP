from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self. equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        for subscription in self.subscriptions:
            if subscription.id == subscription_id:
                customer = next((c for c in self.customers if c.id == subscription.customer_id), None)
                trainer = next((t for t in self.trainers if t.id == subscription.trainer_id), None)
                plan = next((p for p in self.plans if p.id == subscription.exercise_id), None)
                equipment = next((e for e in self.equipment if e.id == plan.equipment_id), None)

                if customer and trainer and plan and equipment:
                    return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
