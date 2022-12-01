class Ship:
    __init__(self, length, front, direction, life):\
        self.length = length
    self.front = front
    self.direction = direction
    self.life = life


def dots(self):
    ship_cells = []
    for i in range(self.length):
        cell = (self.front[i] + self.direction[i], self.front[i + 1] + self.direction[i + 1])
        ship_cells.append(cell)
    return ship_cells
