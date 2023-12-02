games = open('../test/day_01.txt', 'r').read().split('\n')

game_nos = [i for i in range(1, len(games)+1)]

game_count = 0

red_values = []
blue_values = []
green_values = []

valid_games = []
power_games = []

for i in range(len(game_nos)):
    games[i] = games[i].replace('Game ' + str(game_nos[i]) + ':', '')
    games[i] = games[i].split(';')

for game in games:
    for i in game:
        for j in i.split(','):
            if j.strip().split(' ')[1] == 'red':
                red_values.append(int(j.strip().split(' ')[0]))
            if j.strip().split(' ')[1] == 'green':
                green_values.append(int(j.strip().split(' ')[0]))
            if j.strip().split(' ')[1] == 'blue':
                blue_values.append(int(j.strip().split(' ')[0]))

    #part 1 answer logic
    if max(red_values) <= 12 and max(green_values) <= 13 and max(blue_values) <= 14:
        valid_games.append(game_count+1)

    #part 2 answer logic
    power_games.append(max(red_values)*max(green_values)*max(blue_values))

    game_count += 1

    red_values = []
    green_values = []
    blue_values = []

print(sum(valid_games)) # print part 1
print(sum(power_games)) # print part 2