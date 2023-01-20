# -*- coding: utf-8 -*-

POPULATION_SIZE = 10  # количество геномов
MUTA_RATE = 0.3       # вероятность мутации
ROTATIONS = 4    # выбор вращения, 1: нет вращения
# Единица MM (мм)
SPACING = 5    # графический интервал между контурами

# разные размеры рабочей области
BIN_HEIGHT = 1500
BIN_WIDTH = 2500
BIN_NORMAL = [[0, 0], [0, BIN_HEIGHT], [BIN_WIDTH, BIN_HEIGHT], [BIN_WIDTH, 0]]  # области
BIN_CUT_BIG = [[0, 0], [0, 1570], [2500, 1570], [2500, 0]]  # Размер области для резки 1
BIN_CUT_SMALL = [[0, 0], [0, 1200], [1500, 1200], [1500, 0]]  # Размер области для резки 2


SIMPLIFYING_POLYGONS = False  # упрощать полигоны до минимального количенства точек

# Коэффициент масштабирования контуров для объекта SPLINE
COUNTOUR_SCALING = 9 # установите 1, если не надо масштабировать