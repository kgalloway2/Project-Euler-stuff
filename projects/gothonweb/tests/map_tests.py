from nose.tools import *
from gothonweb.map import *

def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""", generic_action_funtion)
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.", generic_action_funtion)
    north = Room("North", "Test room in the north.", generic_action_funtion)
    south = Room("South", "Test room in the south.", generic_action_funtion)

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.", generic_action_funtion)
    west = Room("Trees", "There are trees here, you can go east.", generic_action_funtion)
    down = Room("Dungeon", "It's dark down here, you can go up.", generic_action_funtion)

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]
    assert_in(START.go('shoot!'), [
        ("You try to shoot the Gothon, but it's quicker than you. It shoots you!", quips[0]),
        ("You try to shoot the Gothon, but it's quicker than you. It shoots you!", quips[1]),
        ("You try to shoot the Gothon, but it's quicker than you. It shoots you!", quips[2]),
        ("You try to shoot the Gothon, but it's quicker than you. It shoots you!", quips[3])
    ])
    assert_in(START.go('dodge!'),  [
        ("You try to dodge the Gothon, but it's quicker than you. It shoots you!", quips[0]),
        ("You try to dodge the Gothon, but it's quicker than you. It shoots you!", quips[1]),
        ("You try to dodge the Gothon, but it's quicker than you. It shoots you!", quips[2]),
        ("You try to dodge the Gothon, but it's quicker than you. It shoots you!", quips[3])
    ])
    room = START.go('tell a joke')
    assert_equal(room, laser_weapon_armory)
    assert_equal(room.go(pass_code), the_bridge)
    assert_equal(room.go('0221'), generic_death('armory'))