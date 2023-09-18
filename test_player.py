import pytest

from directions import Player

def test_init() -> None:
    """ Tests the __init__ correctly sets instance vars. """
    p = Player(0, 0)
    assert p.x == 0
    assert p.y == 0

    # tests another initial location to make sure that whoever wrote the code
    # didn't just set the initial location to (0,0) all the time.
    p2 = Player(2, 3)
    assert p2.x == 2
    assert p2.y == 3


def test_location() -> None:
    """ Test that location correctly returns a tuple of the player's x and y
    coordinates. """

    p = Player(0, 0)

    # manually set the x and y, in case the __init__ method didn't set them
    # correctly...
    p.x = 7
    p.y = 3
    loc = p.location()
    assert loc == (7, 3)
