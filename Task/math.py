class Math:

    # Calculates the distance between two points
    @staticmethod
    def calculate_distance(self, x_start, y_start, x_end, y_end):
        return abs(x_start - x_end) + abs(y_start - y_end)

    # Returns if a vehicle can still get the bonus for a timely start
    @staticmethod
    def gets_bonus(vehicle, ride, current_time):
        distance = Math.calculate_distance(vehicle.pos_x, vehicle.pos_y, ride.x_start, ride.y_start)
        arrival_time = current_time + distance
        if arrival_time <= ride.earliest_start:
            return True
        else:
            return False
