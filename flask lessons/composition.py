from typing import List

class Mammal:
    def __init__(self, name: str, *humans: List['Human']):
        self.name = name
        self.humans = humans

    def __str__(self):
        return f" Mammal: {self.name}"


    def get_humans(self) -> int:
        return len(self.humans)

class Human:
    def __init__(self,shape, color):
        self.shape= shape
        self.color = color

    def __str__(self) ->str:
        return f"name: {self.color}, and shape: {self.shape}\n"



human = Human('thin body',"black")
human2 = Human('curvy body', 'White')

humans = Mammal('humans', human, human2)
print(humans.get_humans())