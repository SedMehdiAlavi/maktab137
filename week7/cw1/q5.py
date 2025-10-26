class Team:
    def __init__(self, name, *players):
        self.names = name
        self.players = players

    def __len__(self):
        return len(self.names)

    def __add__(self, other):
        return Team(self.names, self.players + other.players)

    def __str__(self):
        return f'{self.names}\n{self.players}'

    def __del__(self):
        print('Team deleted!')

team1 = Team('Barcelona', 'a','b', 'c', 'd')
team2 = Team('Man ct', 'e', 'f', 'g', 'h')
