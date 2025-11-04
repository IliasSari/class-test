class Dog:
    def __init__(self, name, ):
        self.name = name #instance attribute
    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")

class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name}Guides the way")

class friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, friendly):
    def sound(self):
        print("Golden Retriever Barks")

lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()

lab1 = friendly()
lab1.greet()