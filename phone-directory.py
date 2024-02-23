// https://leetcode.com/problems/phone-directory

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.slots = [i for i in range(maxNumbers)]
        

    def get(self) -> int:
        if self.slots == []:
            return -1
        else:
            return self.slots.pop()
        

    def check(self, number: int) -> bool:
        return number in self.slots
        

    def release(self, number: int) -> None:
        if number not in self.slots:
            self.slots.append(number)


        