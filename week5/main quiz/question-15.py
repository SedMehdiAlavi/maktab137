# لیستی از دیکشنری ها داریم که اطلاعات دانش آموزان را نگه میدارد .
#تابعی بنویسید که لیست را به گونه ای مرتب کند که :
# 1 . ابتدا بر اساس grade از بیشترین به کمترین
# 2. در صورت تساوی نمره ، بر اساس نام به ترتیب حروف الفبا

students = [
    {"name": "Reza", "grade": 17},
    {"name": "Sara", "grade": 19},
    {"name": "Ali", "grade": 17},
    {"name": "Mina", "grade": 20}
]

def sort_students(lst):
    """
    We want to sort descending students by their grade and if
      they were equal, sort them ascending by name. So I use a lambda
      to sort by grade and name. I use "-" before student(x) to sort
      them descending. The lambda when find two equal students,
      check the second parameter and sorts them by name
    """
    result = sorted(lst, key= lambda x: (-x["grade"], x["name"]))
    return result

print(sort_students(students))