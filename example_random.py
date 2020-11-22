from game_of_life import random_cells, animate


if __name__ == '__main__':
    cells = random_cells(128, 128)
    animate(cells, 'output/random.gif', steps=1000, fps=30)
