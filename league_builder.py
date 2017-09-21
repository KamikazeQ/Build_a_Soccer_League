import csv

# Open and read file.
def read():
    with open('soccer_players.csv', newline='') as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=',')
        players = list(player_reader)
        return players

player_list_from_csv = read()
    
# Create team lists
def find_experienced(player_list_from_csv):
    experienced = []
    new = []
    for the_player in player_list_from_csv:
        if the_player['Soccer Experience'] == 'YES':
            experienced.append(the_player)
        else:
            new.append(the_player)
    return experienced
    return new

# Put all logic and function calls inside block
if __name__ == '__main__':
    Dragons = []
    Sharks = []
    Monsters = []
    while True:
        find_experienced(player_list_from_csv)
        if len(experienced) in Dragons < 4:
            Dragons.append(experienced)
        elif len(experienced) in Sharks < 4:
            Sharks.append(experienced)
        else:
            Monsters.append(experienced)
    print(Dragons)
    print(Sharks)
    print(Monsters)

