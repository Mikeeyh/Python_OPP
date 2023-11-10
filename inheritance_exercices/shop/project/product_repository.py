from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name: str):
        for p in self.products:
            if p.name == product_name:
                self.products.remove(product_name)

    def __repr__(self):
        info = [f"{p.__repr__()}: {p.quantity}" for p in self.products]
        return '\n'.join(info)
