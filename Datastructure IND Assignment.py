from collections import deque

# List to manage players
players = []

# Stack to undo team changes 
undo_stack = []

# Queue to schedule matches 
match_schedule = deque()

def add_player(player_name):
    players.append(player_name)
    undo_stack.append(('remove_player', player_name)) 
    print(f"Player '{player_name}' added to the team.")

def remove_player(player_name):
    if player_name in players:
        players.remove(player_name)
        undo_stack.append(('add_player', player_name)) 
        print(f"Player '{player_name}' removed from the team.")
    else:
        print(f"Player '{player_name}' not found in the team.")

# Undo the last team change
def undo_change():
    if undo_stack:
        last_action, player_name = undo_stack.pop()
        if last_action == 'remove_player':
            players.remove(player_name)
            print(f"Undo: Player '{player_name}' removed from the team.")
        elif last_action == 'add_player':
            players.append(player_name)
            print(f"Undo: Player '{player_name}' added back to the team.")
    else:
        print("No changes to undo.")

def schedule_match(opponent):
    match_schedule.append(opponent)
    print(f"Match scheduled against '{opponent}'.")

def play_next_match():
    if match_schedule:
        opponent = match_schedule.popleft() 
        print(f"Playing match against '{opponent}'.")
    else:
        print("No matches scheduled.")

def view_match_schedule():
    if match_schedule:
        print("Upcoming matches:")
        for match in match_schedule:
            print(f"- {match}")
    else:
        print("No matches scheduled.")

def view_team():
    if players:
        print("Current team players:")
        for player in players:
            print(f"- {player}")
    else:
        print("No players in the team.")

add_player("Muhire")
add_player("Emmy")
add_player("Vedaste")
add_player("Gasore")
remove_player("Emmy")
remove_player("Vedaste")
undo_change() 
view_team()

schedule_match("Team A")
schedule_match("Team B")
schedule_match("Team C")
schedule_match("Team D")
view_match_schedule()
play_next_match()
play_next_match()
play_next_match()
play_next_match()
view_match_schedule()
