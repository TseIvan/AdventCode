from IntCode import IntCode, parseFile
def run():
    program = IntCode(parseFile('day13.txt'))
    # every three output instructions specify the x position (distance from the left), y position (distance from the top), and tile id. The tile id is
    # 0 is an empty tile. No game object appears in this tile.
    # 1 is a wall tile. Walls are indestructible barriers.
    # 2 is a block tile. Blocks can be broken by the ball.
    # 3 is a horizontal paddle tile. The paddle is indestructible.
    # 4 is a ball tile. The ball moves diagonally and bounces off objects


    # while not program.terminate:
    #     break
    program.compile()

    return

run()
