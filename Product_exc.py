class OverflowException(Exception):
    def show_msg(self):
        return "Exceeded maximum capacity"


class MinValException(Exception):
    def show_msg(self):
        return "Minimum capacity not fulfilled"


class ProdNotFound(Exception):
    def show_msg(self):
        return "Product not found"


class Product:
    products = {101: {"min_qty": 10, "max_qty": 50}}

    def __init__(self, pcode, qty):
        self.pcode = pcode
        self.qty = qty

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
            if qty < Product.products[pcode]["min_qty"]:
                raise MinValException
            if qty > Product.products[pcode]["max_qty"]:
                raise OverflowException
            # price = float(input("Price:"))
            product_obj = Product(pcode, qty)
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
