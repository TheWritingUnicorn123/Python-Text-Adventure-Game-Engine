from text_adventure.engine import Engine
from text_adventure.room import Room

entrance = Room("Entrance thing", "A glorious mansion")
other_room = Room("Other room", "A boring place to be")

entrance.connect(other_room, "left", "right")

engine = Engine()
engine.run(entrance)