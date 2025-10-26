class Student:
    def __init__(self, name, garde: list):
        self.name = name
        self.garde = garde


    def __len__(self):
        return len(self.garde)

    def __add__(self, other):
        if isinstance(other, Student):
            k = []
            for i, j in zip(self.garde, other.garde):
                k.append((i + j) // 2)

            return Student(self.name, k)

    def __str__(self):
        return f'{self.name}: {self.garde}'

    def __del__(self):
        print(f'{self.name} deleted!')


parsa = Student('Parsa', [17, 18, 15, 20])
alirza = Student('Alirza', [14, 19, 18, 15])
print(parsa + alirza)