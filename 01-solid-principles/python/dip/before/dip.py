"""
What is dependency inversion?
    High level module/ class should not depend directly on low level module/ class, 
    intead they should depend on abstraction
"""

class TikiService:
    def filter(self, product_name):
        print(f"filter by {product_name}")

    def reset_status(self, status):
        print(f"reset status by {status}")


class OrderDetail:
    def __init__(self, tiki_sv):
        self.tiki_sv =  tiki_sv

    def get_orders(self, product_name):
        self.tiki_sv.filter(product_name=product_name)

    def clear_orders(self, status):
        self.tiki_sv.reset_status(status=status)

if __name__ == "__main__":
    tiki_sv = TikiService()

    orders = OrderDetail(tiki_sv)
    book_name = "Python"
    orders.get_orders(book_name)
    
    """
    Everything is oke, but when client want to change all logic of filter and reset_status of TikiService,
    How do you solve this?
    And anytime in future, client come up with another business and need to change again?
    How to solve this?
    """

