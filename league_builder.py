import csv

# Create team lists
Dragons = []
Sharks = []
Raptors = []
def each_player(players):
    experienced = []
    new = []
    for each_player in players:
        if each_player['Soccer Experience'] == 'YES':
            experienced.append(each_player)
        else:
            new.append(each_player)
    print(experienced)
    print(new)
# Open and read file.
def read():
    with open('soccer_players.csv', newline='') as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=',')
        players = list(player_reader)

# Put all logic and function calls inside block
if __name__ == "__main__":

