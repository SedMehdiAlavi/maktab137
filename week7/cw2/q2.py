class Config:
    exist = False
    def __new__(cls, language, theme):
        if not Config.exist:
            obj = object.__new__(cls)
            Config.exist = True
            return obj

    def __init__(self, language, theme):
        self.language = language
        self.theme = theme


config1 = Config("en", "eng")
print(config1.language)

config2 = Config("fa", "Per")
print(config2.language)