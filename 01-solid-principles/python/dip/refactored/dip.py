from abc import ABC, abstractmethod

class BaseService(ABC):
    @abstractmethod
    def filter(self, product_name): pass

    @abstractmethod
    def reset_status(self, status): pass


class TikiService(BaseService):
    def filter(self, product_name):
        print(f"Filter logic with tiki service {product_name}")

    def reset_status(self, status):
        print(f"reset status logic with tiki service {status}")


class ShopeeService(BaseService):
    def filter(self, product_name):
        print(f"Filter logic with shopee service {product_name}")

    def reset_status(self, status):
        print(f"reset status logic with shopee service {status}")


class LazadaService(BaseService):
    def filter(self, product_name):
        print(f"Filter logic with lazada service {product_name}")

    def reset_status(self, status):
        print(f"reset status logic with lazada service {status}")


class OrderDetail:
    def __init__(self, service: BaseService) -> None:
        self.service = service

    def get_orders(self, product_name):
        self.service.filter(product_name=product_name)

    def clear_orders(self, status):
        self.service.reset_status(status=status)


if __name__ == "__main__":
    
    shopee_sv = ShopeeService()
    lazada_sv = LazadaService()

    orders = OrderDetail(shopee_sv)
    orders1 = OrderDetail(lazada_sv)
    book_name = "Python"

    orders.get_orders(book_name)
    orders1.get_orders(book_name)
