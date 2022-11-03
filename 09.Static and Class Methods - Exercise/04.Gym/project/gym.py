from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self,customer:Customer):
        result = self.__add_entity(self.customers,customer)
        if result != None:
            self.customers.append(result)


    def add_trainer(self,trainer:Trainer):
        result = self.__add_entity(self.trainers, trainer)
        if result != None:
            self.trainers.append(result)

    def add_equipment(self,equipment:Equipment):
        result = self.__add_entity(self.equipment,equipment)
        if result != None:
            self.equipment.append(result)

    def add_plan(self,plans:ExercisePlan):
        result = self.__add_entity(self.plans,plans)
        if result != None:
            self.plans.append(result)

    def add_subscription(self,subscription:Subscription):
        result = self.__add_entity(self.subscriptions,subscription)
        if result != None:
            self.subscriptions.append(result)




    def __add_entity(self,collection,entity):
        if entity in collection:
            return
        return entity

    def subscription_info(self,subscription_id):
        subscription = self.__find_entity_id(self.subscriptions, subscription_id)
        customer = self.__find_entity_id(self.customers,subscription.customer_id)
        trainer = self.__find_entity_id(self.trainers, subscription.trainer_id)
        plan = self.__find_entity_id(self.plans, subscription.exercise_id)
        equipment = self.__find_entity_id(self.equipment, plan.equipment_id)

        return repr(subscription) + '\n' + repr(customer) + '\n' + repr(trainer) + '\n' + repr(equipment) + '\n' + repr(plan)

    def __find_entity_id(self, collection, entity_id):
        for entity in collection:
            if entity.id == entity_id:
                return entity







