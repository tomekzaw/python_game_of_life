from game_of_life import empty_cells, make_cells, paste, animate


if __name__ == '__main__':
    cells = empty_cells(32, 32)
    glider = make_cells(
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
    )
    paste(cells, glider)
    animate(cells, 'output/glider.gif')
