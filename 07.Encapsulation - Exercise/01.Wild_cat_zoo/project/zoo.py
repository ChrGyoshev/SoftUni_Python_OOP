class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []


    def add_animal(self,animal,price):
        if self.__budget < price:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self,worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self,worker_name):
        if any([True for worker in self.workers if worker.name == worker_name]):
            [self.workers.remove(x) for x in self.workers if x.name == worker_name]
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salary = 0
        for workers in self.workers:
            salary += workers.salary
        if self.__budget >= salary:
            self.__budget -= salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        price_for_tend_animals = 0
        for animals in self.animals:
            price_for_tend_animals += animals.money_for_care
        if self.__budget >= price_for_tend_animals:
            self.__budget -= price_for_tend_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self,amount):
        self.__budget += amount


    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.build_str(self.animals,'Lion')
        result += self.build_str(self.animals,"Tiger")
        result += self.build_str(self.animals,"Cheetah")
        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += self.build_str(self.workers,"Keeper")
        result += self.build_str(self.workers,"Caretaker")
        result += self.build_str(self.workers,"Vet")
        return  result.strip()


    def build_str(self,entities,entity_type):
        counter = 0
        result = ''
        for entity in entities:
            if entity.__class__.__name__ == entity_type:
                counter += 1
                result += repr(entity) + '\n'
        return f'----- {counter} {entity_type}s:\n' + result