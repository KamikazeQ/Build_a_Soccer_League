import csv

# Open and read file.
def read():
    with open('soccer_players.csv', newline='') as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=',')
        players = list(player_reader)
        return players

# Create team lists
def find_experienced(players):
    experienced = []
    new = []
    for the_player in players:
        if each_player['Soccer Experience'] == 'YES':
            experienced.append(the_player)
        else:
            new.append(the_player)
    print(experienced)
    print(new)

read()
find_experienced(players)
# Put all logic and function calls inside block


