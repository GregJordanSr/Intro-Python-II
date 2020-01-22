# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, current_room):
        self.current_room = starting_room
    def change_location(self, current_location):
        self.current_location = current_location
    def __str__(self):
        return f"Player is in the {self.current_room} room"

