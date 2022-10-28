def clearSquare(data, x, y, side):
    for yOffset in range(0, side):
        for xOffset in range(0, side):
            data[x + xOffset][y + yOffset] = False


def clearCorner(data, size):
    for yOffset in range(size - 6, size):
        for xOffset in range(size - 1, size - 5, -1):
            if xOffset > size - 6 + (size - yOffset):
                data[xOffset][yOffset] = False
