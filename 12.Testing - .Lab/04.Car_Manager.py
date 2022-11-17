class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed



from unittest import TestCase,main

class CarManagerTests(TestCase):

    def setUp(self):
        self.car = Car("Ford", "Mondeo", 10, 50)

    # test refuel method
    def test_car_refuel__if_amount_to_add_less_than_0__expect_exception(self):
        amount_to_add = -4
        with self.assertRaises(Exception):
            self.car.refuel(amount_to_add)

    def test_car_refuel__if_amount_to_add_above_0_and_total_amount_within_capacity__expect_correct_result(self):
        amount_to_add = 10
        self.car.refuel(amount_to_add)
        self.assertEqual(10, self.car.fuel_amount)

    def test_car_refuel__if_amount_to_add_above_0_and_total_amount_greater_than_capacity__expect_correct_result(self):
        amount_to_add = 56
        self.car.refuel(amount_to_add)
        self.assertEqual(50, self.car.fuel_amount)

    #test drive method
    def test_car_drive__if_needed_fuel_greater_than_total_fuel__expect_exception(self):
        distance = 600
        self.car.refuel(30)
        with self.assertRaises(Exception):
            self.car.drive(distance)

    def test_car_drive__if_needed_fuel_less_or_equal_to_total_fuel__expect_correct_result(self):
        distance = 150
        self.car.refuel(30)
        self.car.drive(distance)
        self.assertEqual(15, self.car.fuel_amount)

    # test the properties
    def test_car_make_property__if_empty_string_expect_exception(self):
        with self.assertRaises(Exception):
            self.car.make = ""

    def test_car_model_property__if_empty_string_expect_exception(self):
        with self.assertRaises(Exception):
            self.car.model = ""

    def test_car_fuel_consumption__if_negative_number_or_0__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = -8

    def test_car_fuel_capacity__if_negative_number_or_0__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = 0

if __name__ == "__main__":
    main()