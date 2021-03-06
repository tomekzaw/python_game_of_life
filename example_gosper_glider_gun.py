from pathlib import Path

from game_of_life import asset, load_cells, empty_cells, paste, animate


if __name__ == '__main__':
    cells = empty_cells(64, 80)

    gosper_glider_gun = load_cells(asset('gosper_glider_gun.png'))
    paste(cells, gosper_glider_gun, 2, 2)

    animate(cells, 'output/gosper_glider_gun.gif', steps=200, fps=30)
