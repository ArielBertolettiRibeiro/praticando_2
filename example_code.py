
"""
class Produto:

    def __init__(self, name: str, price: float, quantity: int)-> None:

        name = (name or "").strip()
        if not name:
            raise ValueError("Nome não pode ser nulo.")
        
        if price <= 0:
            raise ValueError("Preço deve ser maior que 0.")
        
        if quantity < 0:
            raise ValueError("Quantidade deve ser maior que 0.")
     
        self.__name = name
        self.__price = float(price)
        self.__quantity = int(quantity)

    @property
    def name(self)-> str:
        return self.__name
    
    @property
    def price(self)-> float:
        return self.__price
    
    @property
    def quantity(self)-> int:
        return self.__quantity
    
    def __str__(self)-> str:
        return f"Product(name={self.__name!r}, price={self.__price:.2f}, quantity={self.__quantity})"

    @classmethod
    def from_dict(cls, data: dict)-> "Produto":
        return cls(
            name=data["name"],
            price=data["price"],
            quantity=data.get("quantity", 0)
        )   
    
    def add_stock(self, quantity: int) -> None:

        if quantity <= 0:
            raise ValueError("Quantidade deve ser maior que zero.")
        
        self.__quantity += quantity
    
    def sell(self, quantity: int) -> None:
         
         if quantity <= 0:
             raise ValueError("Quantidade dever ser maior que zero.")

         if quantity > self.__quantity:
             raise ValueError("Estoque insuficiente!")
         
         self.__quantity -= quantity

    def stock_value(self) -> float:
        return self.__quantity * self.__price
        """