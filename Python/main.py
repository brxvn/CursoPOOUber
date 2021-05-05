from car import Car
from account import Account

if __name__ == '__main__':
    print("hola mundo")
    
    car = Car("AMS123", Account("Andres Mercado", "AND123"))

    print(vars(car))
    print(vars(car.driver))