from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []


    def add(self,product: Product):
        self.products.append(product)

    def find(self, product_name):
        for data in self.products:
            if data.name == product_name:
                return data

    def remove(self, product_name):
        temp = self.find(product_name)
        if temp != None:
            self.products.remove(temp)

    def __repr__(self):
        result = ''
        for data in self.products:
            result += f"{data.name}: {data.quantity}\n"
        return result.strip()



