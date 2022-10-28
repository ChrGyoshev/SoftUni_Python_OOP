class Account:
    def __init__(self,id, balance, pin):
        self.__pin = pin
        self.__id = id
        self.balance = balance

    def get_id(self,pin):
        if pin == self.__pin:
            return self.__id
        return f"Wrong pin"

    def change_pin(self,old_pin,new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"





