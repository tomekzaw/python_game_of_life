import pytest

from game_of_life import load_cells, asset, step, equal


@pytest.mark.parametrize('filename', [
    'block.png',
    'beehive.png',
    'loaf.png',
    'boat.png',
    'tub.png',
])
def test_still(filename):
    cells = load_cells(asset(filename))
    assert equal(step(cells), cells)
