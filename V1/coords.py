class Coordinates:
    def __init__(self, X_LIMIT = 7, Y_LIMIT = 6):
        self.X_LIMIT = X_LIMIT
        self.Y_LIMIT = Y_LIMIT

    def subtract_from_coord(self, coord):
        return coord - 1 if coord - 1 >= 0 else None

    def add_to_coord(self, coord, limit):
        return coord + 1 if coord + 1 <= limit - 1 else None

    def left_coord(self, x, y):
        lc = self.subtract_from_coord(x)
        return [lc, y] if lc != None else None

    def right_coord(self, x, y):
        rc = self.add_to_coord(x, self.X_LIMIT)
        return [rc, y] if rc != None else None

    def down_coord(self, x, y):
        dc = self.subtract_from_coord(y)
        return [x, dc] if dc != None else None

    def up_coord(self, x, y):
        uc = self.add_to_coord(y, self.Y_LIMIT)
        return [x, uc] if uc != None else None

    def top_left_coord(self, x, y):
        xm = self.subtract_from_coord(x)
        yp = self.add_to_coord(y, self.Y_LIMIT)
        return [xm, yp] if xm != None and yp != None else None

    def bottom_left_coord(self, x, y):
        xm = self.subtract_from_coord(x)
        ym = self.subtract_from_coord(y)
        return [xm, ym] if xm != None and ym != None else None

    def top_right_coord(self, x, y):
        xp = self.add_to_coord(x, self.X_LIMIT)
        yp = self.add_to_coord(y, self.Y_LIMIT)
        return [xp, yp] if xp != None and yp != None else None

    def bottom_right_coord(self, x, y):
        xp = self.add_to_coord(x, self.X_LIMIT)
        ym = self.subtract_from_coord(y)
        return [xp, ym] if xp != None and ym != None else None
