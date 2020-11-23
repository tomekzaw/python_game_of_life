from pathlib import Path

from game_of_life import asset, load_cells, empty_cells, paste, animate


if __name__ == '__main__':
    puffer_train = load_cells(asset('puffer_train.png'))
    cells = empty_cells(puffer_train.shape[0], 300)
    paste(cells, puffer_train)
    animate(cells, 'output/puffer_train.gif', steps=600, fps=30)
