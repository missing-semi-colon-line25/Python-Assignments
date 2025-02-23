from datetime import datetime


def main():
    product = {}
    flag = True
    while flag:
        pcode = int(input("Enter product code:"))
        pname = input("Enter product name:")
        qty = int(input("Enter product quantity:"))
        price = float(input("Enter price:"))
        product[pcode] = [pname, qty, price]
        while 1:
            choice = input("Keep inserting ?(y/n)").lower()
            if choice in ("n", "no"):
                flag = False
                break
            elif choice in ("y", "yes"):
                break
            else:
                print("invalid input")
    now = datetime.now()
    with open(f"Product_{now.day}_{now.month}_{now.year}", 'w') as fobj:
        fobj.write("Product code\tProduct name\tQuantity\tPrice\n")
        for pcode in product:
            fobj.write(f"{pcode}\t\t\t\t{product[pcode][0]}\t\t\t{product[pcode][1]}\t\t\t{product[pcode][2]}\n")


main()
