from unittest import TestCase,main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100,150)

    def test_vehicle_init(self):
        fuel = 100
        horse_power = 200
        vehicle = Vehicle(fuel,horse_power)

        self.assertEqual(fuel,vehicle.fuel)
        self.assertEqual(fuel,vehicle.capacity)
        self.assertEqual(horse_power,vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION,vehicle.fuel_consumption)

    def test_vehicle_str(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        actual_result = str(self.vehicle)

        self.assertEqual(actual_result,expected)

    def test_drive_raises_when_distance_is_not_reachable(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(self.vehicle.fuel)

        self.assertEqual('Not enough fuel',str(ex.exception))


    def test_drive_reduces_fuel_when_destination_is_reached(self):

        distance = 10
        fuel_burned = distance * self.vehicle.fuel_consumption
        expected = self.vehicle.fuel - fuel_burned
        self.vehicle.drive(distance)
        self.assertEqual(expected,self.vehicle.fuel)

    def test_refuel_raises_when_tank_is_full(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_refuel_recharges(self):
        self.vehicle.fuel = 80
        self.vehicle.refuel(20)
        self.assertEqual(100,self.vehicle.fuel)

if __name__ == "__main__":
    main()