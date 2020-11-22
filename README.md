# Conway's Game of Life
Written in Python with a great help of [NumPy](https://www.numpy.org/), [SciPy](https://www.scipy.org/) and [Pillow](https://python-pillow.org/).

[![Build Status](https://travis-ci.com/tomekzaw/python_game_of_life.svg?branch=master)](https://travis-ci.com/tomekzaw/python_game_of_life)

## Rules
```py
return (alive & (two | three)) | (dead & three)
```

## Examples

### Gosper's glider gun
```sh
python example_gospers_glider_gun.py
```
![](output/gospers_glider_gun.gif)

### Breeder
```sh
python example_breeder.py
```
![](output/breeder.gif)

### Random state
```sh
python example_random.py
```
![](output/random.gif)

## Testing
```sh
pytest
```
