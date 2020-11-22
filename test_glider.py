import pytest

from game_of_life import load_cells, asset, step, equal


gliders = [load_cells(asset(f'glider{i}.png')) for i in range(4+1)]


@pytest.mark.parametrize('before, after', zip(gliders, gliders[1:]))
def test_glider(before, after):
    assert equal(step(before), after)
