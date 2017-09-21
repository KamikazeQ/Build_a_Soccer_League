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
    for the_player in player_list_from_csv:
        if the_player['Soccer Experience'] == 'YES':
            experienced.append(the_player)
        else:
            new.append(the_player)
    return experienced, new

experienced_and_new_players = find_experienced(player_list_from_csv)

# Distributes experienced and new players
def players_per_team(experienced_and_new_players):
        Dragons = []
        Sharks = []
        Raptors = []
        
        for player in experienced:
            if len(experienced) in Dragons < 4:
                Dragons.append(experienced)
            elif len(experienced) in Sharks < 4:
                Sharks.append(experienced)
            else:
                Raptors.append(experienced)
        for player in new:
            if len(new) in Dragons < 4:
                Dragons.append(new)
            if len(new) in Sharks < 4:
                Sharks.append(new)
            else:
                Raptors.append(new)
        return Dragons, Sharks, Raptors
        print(Dragons, Sharks, Raptors)
        
if __name__ == '__main__':        
    read()
    find_experienced(player_list_from_csv)
    players_per_team(experienced_and_new_players)

# Put all logic and function calls inside block    

        
