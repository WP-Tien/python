class Car:
    def __init__(self, brand: str, colour: str, horsepower: int) -> None:
        self.brand = brand
        self.colour = colour
        self.horsepower = horsepower

    def drive(self) -> None:
        print(f'{self.brand} is driving!')

    def get_info(self, var: int) -> None:
        print( var )

        print(f'{self.brand} with {self.horsepower} horsepower')


volvo: Car = Car('Volvo', 'red', 20)
print( volvo.colour )
print( volvo.horsepower )
volvo.drive()
volvo.get_info(29)


bmw: Car = Car('BMW', 'dark blue', 200)
print( bmw.colour )
print( bmw.horsepower )