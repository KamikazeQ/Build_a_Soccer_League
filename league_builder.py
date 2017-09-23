import csv

# Open and read file.
def read():
    with open('soccer_players.csv', newline='') as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=',')
        players = list(player_reader)
        return players
    
player_list_from_csv = read()

# Find experienced players vs. not experienced players
def find_experienced(player_list_from_csv):
    experienced = []
    new = []
    for the_experienced_player in player_list_from_csv:
        if the_experienced_player['Soccer Experience'] == 'YES':
            experienced.append(the_experienced_player)
    return experienced

def find_new(player_list_from_csv):
    new = []
    for the_new_player in player_list_from_csv:
        if the_new_player['Soccer Experience'] == 'NO':
            new.append(the_new_player)
    return new

experienced_players = find_experienced(player_list_from_csv)
new_players = find_new(player_list_from_csv)

# Distributes experienced and new players
def players_per_team(experienced_players, new_players):
    Dragons = []
    Sharks = []
    Raptors = []
    
    for player in experienced_players:
        if len(experienced_players) in Dragons < 4:
            Dragons.append(experienced_players)
        elif len(experienced_players) in Sharks < 4:
            Sharks.append(experienced_players)
        else:
            Raptors.append(experienced_players)
    for player in new_players:
        if len(new_players) in Dragons < 4:
            Dragons.append(new_players)
        if len(new_players) in Sharks < 4:
            Sharks.append(new_players)
        else:
            Raptors.append(new_players)
    return Dragons, Sharks, Raptors
    print(Dragons, Sharks, Raptors)
        
# Put all logic and function calls inside block
if __name__ == '__main__':        
    read()
    find_experienced(player_list_from_csv)
    players_per_team(experienced_players, new_players)
        
