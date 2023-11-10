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
        products_to_remove = [p for p in self.products if p.name == product_name]
        for p in products_to_remove:
            self.products.remove(p)
            # we should create products_to_remove in order to add a matching products and remove them after that
            # if we remove directly using for cycle on the self.products it will put a ValueError

    def __repr__(self):
        info = [f"{p.__repr__()}: {p.quantity}" for p in self.products]
        return '\n'.join(info)
