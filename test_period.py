import pytest

from game_of_life import load_cells, asset, period


@pytest.mark.parametrize('filename, expected', [
    ('block.png', 1),
    ('beehive.png', 1),
    ('loaf.png', 1),
    ('boat.png', 1),
    ('tub.png', 1),
    ('blinker0.png', 2),
    ('pulsar0.png', 3),
    ('pentadecathlon0.png', 15),
])
def test_period(filename, expected):
    cells = load_cells(asset(filename))
    assert period(cells) == expected
