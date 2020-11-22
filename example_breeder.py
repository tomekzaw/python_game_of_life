from game_of_life import asset, load_cells, animate


if __name__ == '__main__':
    cells = load_cells(asset('breeder.png'))
    animate(cells, 'output/breeder.gif', steps=1200, fps=60)
