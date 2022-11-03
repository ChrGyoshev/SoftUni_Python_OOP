from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []


    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10


    def add_customer(self,customer:Customer):
        if not len(self.customers) == MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self,dvd:DVD):
        if not len(self.dvds) == MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self,customer_id, dvd_id):
        customer = self.__find_customer(customer_id)
        dvd = self.__find_dvd(dvd_id)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def __find_customer(self,id):
        for customer in self.customers:
            if id == customer.id:
                return customer

    def __find_dvd(self, id):
        for dvd in self.dvds:
            if id == dvd.id:
                return dvd


    def return_dvd(self,customer_id, dvd_id):
        customer = self.__find_customer(customer_id)
        dvd = self.__find_dvd(dvd_id)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"


    def __repr__(self):
        result = '\n'.join([str(customer) for customer in self.customers]) + "\n"
        result += '\n'.join([str(dvd) for dvd in self.dvds])


        return result
