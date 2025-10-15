# تابعی بنویسید که لیستی از نمرات را گرفته و
# آن ها را در سه گروه دسته بندی کند :
#
# A : نمره های بالای 17
# B : نمره های 12 تا 17
# C : نمره های کمتر از 12


def grades(lst):
    """
    We just need to iterate the list to append every grade into the
      right lists. Then we update the output and put the lists into
      it.
    """
    A = []
    B = []
    C = []
    output = {}
    for grade in lst:
        if grade > 17:
            A.append(grade)
        elif 12 < grade < 17:
            B.append(grade)
        else:
            C.append(grade)

    output.update({'A': A, 'B': B, 'C': C})
    return output


print(grades([10, 15, 18, 20, 13, 8]))