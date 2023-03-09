#Animal Shelter
class animalShelter():
    def __init__(self):
        self.cat = []
        self.dog = []

    def enqueue(self, item ,type):
        if type == "Cat":
            self.cat.append(item)
        else:
            self.dog.append(item)
    
    def dequeueCat(self):
        if len(self.cat) == 0:
            return None
        return self.cat.pop(0)
    
    def dequeueDog(self):
        if len(self.dog) == 0:
            return None
        return self.dog.pop(0)
    
    def dequeueAny(self):
        if len(self.cat) == 0:
            return self.dog.pop(0)
        else:
            return self.cat.pop(0)

aS = animalShelter()
aS.enqueue("Cat1","Cat")
aS.enqueue("Cat2","Cat")
aS.enqueue("Dog1", "Dog")
aS.enqueue("Cat3","Cat")
aS.enqueue("Dog2", "Dog")

print(aS.dequeueAny())