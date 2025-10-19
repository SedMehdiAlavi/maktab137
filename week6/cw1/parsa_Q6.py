class Student :
    def __init__(self , name : str , mark : int):
        self.name = name
        self.mark = mark

    def add_grade(self , score11 : int , score22 : int ) :
        # marks = []
        # mark1 = input("enter mark  : ")
        # marks.append(mark1)
        print(f"your grades are {score11} and {score22} and added")

    def avarege (self , score1 : int , score2 : int ) :
        # self.avarege = avarege
        avaregegir = score1 + score2
        print(f"your avarege is {avaregegir}")

amir = Student("amir" , 10)
amir.add_grade(10 , 2)
amir.avarege(10 , 2)
