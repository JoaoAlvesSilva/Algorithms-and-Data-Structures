// https://leetcode.com/problems/valid-parentheses

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_parking_spaces = big
        self.medium_parking_spaces = medium
        self.small_parking_spaces = small

        self.available_big_parking_spaces = big
        self.available_medium_parking_spaces = medium
        self.available_small_parking_spaces = small

    def addCar(self, carType: int) -> bool:
        if (carType == 1) and (self.available_big_parking_spaces > 0):
            self.available_big_parking_spaces -= 1
            return True
        
        if (carType == 2) and (self.available_medium_parking_spaces > 0):
            self.available_medium_parking_spaces -= 1
            return True
        
        if (carType == 3) and (self.available_small_parking_spaces > 0):
            self.available_small_parking_spaces -= 1
            return True
        
        return False
                   
        