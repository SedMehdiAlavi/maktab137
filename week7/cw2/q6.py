class CustomDict :

    def __new__ (cls, dictionary ) :
        if not dictionary.keys() :
            raise ValueError("key not found")
        obj = object.__new__ (cls)
        return obj

    def __init__(self, dictionary):

        self.dictionary = dictionary



    def __setitem__(self, value):
        if isinstance(value, int) :
            self.dictionary.values *= 2
        else :
            self.dictionary.values = value

    def __add__(self, other):
        if isinstance(other, CustomDict):
            if other.dictionary.values() != self.dictionary.values() :
                return CustomDict(self.dictionary | other.dictionary)
            else :
                values = self.dictionary.values + other.dictionary.values
                return CustomDict(self.dictionary | values)
                return CustomDict({self.dictionary.keys() : values})

custom1 = CustomDict ({"A": 4})
custom2 = CustomDict ({"B": 4})
c1 = custom1.dictionary.values
print(c1)
result = custom1 + custom2
print(result.dictionary)

# dic1 = {"A": 4, "B": 5}
# print(dic1.keys())