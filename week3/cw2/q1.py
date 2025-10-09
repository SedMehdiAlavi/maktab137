import itertools
# import datetime
import datetime

premier_league_teams: list[str] = [
"Arsenal",
"ston Villa",
"Bournemouth",
"Brentford",
"Brighton & Hove Albion",
"Chelsea",
"Crystal Palace",
"Everton",
"Fulham",
"Liverpool",
"Luton Town",
"Manchester City",
"Manchester United",
"Newcastle United",
"Nottingham Forest",
"Sheffield United",
"Tottenham Hotspur",
"West Ham United",
"Wolverhampton Wanderers",
"Burnley"
]

scores = [5 , 8, 6 , 20 , 19 , 18 , 15 , 16 ,17 , 14 , 11 , 9 ,1 ,2 , 3 ,4 , 10, 12 ,13 ,7]

#part1
teams = premier_league_teams
matches = list(itertools.permutations(premier_league_teams, 2))
games = 0

for match in matches:
    print(match)
    matches.remove(match[::-1])
    games += 1

print(games)

team_list = []


#part2
sort_team = sorted(premier_league_teams)
print(sort_team)

premier_league_teams.sort(key = lambda item: item[0])
print(premier_league_teams)

#part3
def date_match(teams):
    today = datetime.date.today()
    matches = []
    for team in teams:
        today += datetime.timedelta(days= 3)

        matches.append((today.strftime('%Y/%m/%d'), team))

    return matches
match_list = date_match(team_list)

print(match_list)
#part4
result = [(a, b) for a, b in zip(premier_league_teams, scores)]
print(result)
premier_league_teams.sort(key = lambda item: item[0])
print(premier_league_teams)
