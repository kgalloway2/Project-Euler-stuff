from nose.tools import *
from player import Player


def test_add_item():
    player = Player([100, 5, 0], [])

    assert_equal(player.add_item('Salve'), None)