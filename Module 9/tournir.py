first_tour = open('first_tour.txt', 'r')
second_tour = open('second_tour.txt', 'w')

list_of_players = [players.split() for players in first_tour]
limit = list_of_players.pop(0)

winnners = list()

for players in list_of_players:
    if players[2] > limit[0]:
        winnners.append(players)

second_tour.write(str(len(winnners)) + '\n')
winnners.sort()

for i in range(len(winnners)):
    name = winnners[i][1][0] + '.'
    surn = winnners[i][0]
    scores = winnners[i][2]
    second_tour.write(str(i + 1) + ') ')
    second_tour.write(name + ' ')
    second_tour.write(surn + ' ')
    second_tour.write(scores + '\n')
