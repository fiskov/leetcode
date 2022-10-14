# 1603. Design Parking System
# https://leetcode.com/problems/design-parking-system/
# leet_1603
class ParkingSystem:
    __slots__ = ["_garage"]

    def __init__(self, big: int, medium: int, small: int):
        self._garage = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self._garage[carType]:
            self._garage[carType] -= 1
            return True
        return False


obj = ParkingSystem(371, 483, 536)
print(obj.addCar(2))
print(obj.addCar(1))
print(obj.addCar(3))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(2))
print(obj.addCar(2))
print(obj.addCar(1))
print(obj.addCar(3))
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(1))
print(obj.addCar(3))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(3))
print(obj.addCar(1))