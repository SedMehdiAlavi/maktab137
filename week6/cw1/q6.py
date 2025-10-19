class Student:
    def __init__(self, *scores):
        self.scores = list(scores)

    def add_grade(self,score):
        self.scores.append(score)
        return self.scores

    def average(self):
        return round(sum(self.scores) / len(self.scores), 2)



sed_mehdi = Student(19, 18, 17, 15, 20, 18)
print(sed_mehdi.average())
print(sed_mehdi.add_grade(16))
print(sed_mehdi.average())