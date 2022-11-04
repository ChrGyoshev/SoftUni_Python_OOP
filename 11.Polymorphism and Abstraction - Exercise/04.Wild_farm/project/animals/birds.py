from project.animals.animal import Bird


class Owl(Bird):
    FOOD_DICT = ['Meat']
    WEIGHT = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    FOOD_DICT = ['Meat', 'Vegetable', 'Fruit', 'Seed']
    WEIGHT = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"
