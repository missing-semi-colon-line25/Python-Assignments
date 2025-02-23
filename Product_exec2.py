class OverflowException(Exception):
    def show_msg(self):
        return "Exceeded maximum capacity"


class MinValException(Exception):
    def show_msg(self):
        return "Quantity must be positive"


class ProdNotFound(Exception):
    def show_msg(self):
        return "Product not found"


class Product:
    products = {101: 50, 102: 10}

    def __init__(self, pcode, qty):
        self.pcode = pcode
        self.qty = qty

    def get_data(self):
        return f"Product code: {self.pcode} quantity={self.qty}"
        # def validate_qty(self, qty):
        #     pass
        # s
        # def add_prod(self):
        #     pass


def main():
    flag = True
    while flag:
        try:
            pcode = int(input("Enter product code:"))
            if pcode not in Product.products.keys():
                raise ProdNotFound
            qty = int(input("Product Quantity:"))
            if qty < 0:
                raise MinValException
            if qty > Product.products[pcode]:
                raise OverflowException
            # price = float(input("Price:"))
            product_obj = Product(pcode, qty)
            print(product_obj.get_data())
            choice = input("Keep inserting ?(y/n)").lower()
            if choice in ("n", "no"):
                break
        except ProdNotFound as nf:
            print(nf.show_msg())
        except OverflowException as ov:
            print(ov.show_msg())
        except MinValException as mv:
            print(mv.show_msg())


main()
