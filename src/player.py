# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room):
        self.current_room = current_room
        self.name = name
    def change_location(self, current_location):
        self.current_location = current_location

    def __str__(self):
        return f"{self.name} is in the {self.current_room} room"

    def move(self, new_room):
        self.current_room = new_room
        

