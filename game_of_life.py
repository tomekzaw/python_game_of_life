from itertools import count
from pathlib import Path
from typing import Optional, Iterable, Union

import numpy as np
from scipy.signal import convolve2d
import PIL.Image
import PIL.ImageOps
import imageio


mask = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])


def step(alive: np.array) -> np.array:
    neighbours_counts = convolve2d(alive, mask, mode='same')
    two = (neighbours_counts == 2)
    three = (neighbours_counts == 3)
    return three | (two & alive)


def period(cells: np.array) -> int:
    initial = cells.copy()
    for i in count(1):
        cells = step(cells)
        if equal(cells, initial):
            return i


def iterate(cells: np.array, steps: int) -> Iterable[np.array]:
    for _ in range(steps):
        yield cells
        cells = step(cells)


def empty_cells(rows: int, cols: int):
    return np.zeros((rows, cols), dtype=np.bool)


def random_cells(rows: int, cols: int):
    return np.random.randint(low=0, high=2, size=(rows, cols), dtype=np.bool)


def make_cells(*data: list) -> np.array:
    return np.array(data, dtype=np.bool)


def load_cells(path: Union[Path, str], *, inverted=True) -> np.array:
    img = PIL.Image.open(path).convert('1')
    cells = np.array(img)
    if inverted:
        cells = ~cells
    return cells


def asset(filename: str) -> Path:
    return Path(__file__).parent / 'assets' / filename


def paste(cells: np.array, pattern: np.array, y: int = 0, x: int = 0) -> None:
    h, w = pattern.shape
    cells[y:y+h, x:x+w] = pattern


def equal(cells1: np.array, cells2: np.array) -> bool:
    return np.array_equal(cells1, cells2)


def visualize(cells: np.array, *, invert: bool = True, convert: bool = True, scale: Optional[int] = None) -> PIL.Image:
    if invert:
        cells = ~cells
    img = PIL.Image.fromarray(cells)
    if convert:
        img = img.convert('L')
    if scale is not None:
        img = PIL.ImageOps.scale(img, scale)
    return img


def animate(cells: np.array, path: str, *, steps: int = 100, format: str = 'GIF', fps: int = 10):
    sequence = iterate(cells, steps)
    images = map(visualize, sequence)
    imageio.mimsave(path, images, format=format, fps=fps)
