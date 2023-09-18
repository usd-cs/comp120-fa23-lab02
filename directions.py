class Player:
    x: int
    y: int


    def __init__(self, initial_x: int, initial_y: int) -> None:
        self.x = initial_x
        self.y = initial_y


    def location(self) -> tuple[int, int]:
        """ Returns the player's location, as a tuple. """
        return (self.x, self.y)


    def move(self, direction: str) -> None:
        """ Moves the player based on the given direction.

        Note that North and East are considered positive directions while
        South and West are considered negative directions.
        """
        if direction == "north":
            self.y += 1
        elif direction == "east":
            self.x += 1
        elif direction == "south":
            self.y -= 1
        else: # west
            self.x -= 1


def main() -> None:
    """ Creates a player and moves them around in a few different directions. """

    # create a player starting at x = 10, y = 5
    player1 = Player(10, 5)
    print(f"Player is located at {player1.location()}")

    # move the player north
    player1.move("north")
    print(f"Player moved to {player1.location()}")

    # move the player east
    player1.move("east")
    print(f"Player moved to {player1.location()}")

    # move the player south
    player1.move("south")
    print(f"Player moved to {player1.location()}")


if __name__ == "__main__":
    # This is "application" code that only executes when we run this file,
    # NOT when we import it.
    main()
