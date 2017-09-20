import csv

# Open and read file.
def read():
    with open('soccer_players.csv', newline='') as cvsfile:
        player_reader = csv.DictReader(csvfile, delimeter=',')
        players = list(player_reader)

# Put all logic and function calls inside block
if __name__ == "__main__":
    # Create team lists
    Dragons = []
    Sharks = []
    Raptors = []
    def experienced_player(players):
        experienced = []
        new = []
        for each_experienced in players:
            if experienced_player['Soccer Experience'] == 'YES':
                experienced.append(each_experienced)
            else:
                new.append(each_experienced)
        print(experienced)
        print(new)
