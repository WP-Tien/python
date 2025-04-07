class Item:

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

item1 = Item("MyItem", 750)
# Setting an Attribute
item1.name = "OtherItem"

# Getting an Attribute
print(item1.name)