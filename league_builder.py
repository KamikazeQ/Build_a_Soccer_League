import csv

# Open and read file.
def read():
    with open('path\to\soccer_players.csv', newline='') as cvsfile:
        player_reader = csv.DictReader(csvfile, delimeter=',')
        players = list(player_reader)

# Put all logic and function calls inside block
if __name__ == "__main__":
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
