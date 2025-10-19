class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old. I live in {self.address}.")

    def change_address(self, new_address: str):
        self.address = new_address

sed_mehdi = Person('SedMehdi', 28, 'fars')

sed_mehdi.introduce()
sed_mehdi.change_address('My new address')
sed_mehdi.introduce()
