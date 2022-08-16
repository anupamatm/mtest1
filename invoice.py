class Invoice:
    part_num = None
    part_des = None
    num_of_items = 0
    price_of_items = 0.0
    amount = 0.0

    def __init__(self):
        self.part_num = "1"
        self.part_des = "hdd"
        self.num_of_items = 0
        self.price_of_items = 1000

    def get_part_num(self):
        self.part_num = input("Enter part number ")
        return self.part_num

    def get_part_des(self):
        self.part_des = input("Enter part description ")
        return self.part_des

    def get_num_of_items(self):
        self.num_of_items = int(input("Enter number of items "))
        return self.num_of_items

    def get_price_of_items(self):
        self.price_of_items = float(input("Enter price of items "))
        return self.price_of_items

    def set_part_num(self, num):
        self.part_num = num
        return self.part_num

    def set_part_des(self, des):
        self.part_des = des
        return self.part_des

    def set_num_of_items(self, numitem):
        self.num_of_items = numitem
        return self.num_of_items

    def set_price_of_items(self, price):
        self.price_of_items = price
        return self.price_of_items

    def Invoice_amount(self):
        self.amount = self.price_of_items * self.num_of_items
        self.amount = self.amount if (self.amount > 0) else 0
        return self.amount

    def displayInfo(self):
        print("part number:\t",self.part_num , "\tpart description:\t" , self.part_des ,
              "\tnum_of_items:\t" + str(self.num_of_items) ,"\tprice_of_items:\t" +str(self.price_of_items))
        print("\n Amount :\t" +str(self.amount))
        print()


class InvoiceTest:

    def main():

        inv1 = Invoice()
        inv2 = Invoice()
        inv1.get_part_num()
        inv1.get_part_des()
        inv1.get_num_of_items()
        inv1.get_price_of_items()
        inv1.Invoice_amount()
        inv1.displayInfo()
        inv2.set_part_num("1")
        inv2.set_part_des("chip")
        inv2.set_num_of_items(12)
        inv2.set_price_of_items(12)
        inv2.Invoice_amount()
        inv2.displayInfo()


InvoiceTest.main()
