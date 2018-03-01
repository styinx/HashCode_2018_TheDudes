
class Ride:

    def __init__(self, x_start, y_start, x_end, y_end, earliest_start, latest_finish):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish
        self.distance = self.calculate_distance(x_start, y_start, x_end, y_end)

    def __init__(self, x_start, y_start):
        self.x_start = x_start
        self.y_start = y_start

    # Calculates the distance between two points
    def calculate_distance(self, x_start, y_start, x_end, y_end):
        distance = abs(x_start - x_end) + abs(y_start - y_end)
        return distance

