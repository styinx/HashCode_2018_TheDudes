class Mathss:

    # Calculates the distance between two points
    @staticmethod
    def calculate_distance(x_start, y_start, x_end, y_end):
        return abs(x_start - x_end) + abs(y_start - y_end)

    # Returns if a vehicle can still get the bonus for a timely start
    @staticmethod
    def gets_bonus(vehicle, ride, current_time):
        distance = Mathss.calculate_distance(vehicle.pos_x, vehicle.pos_y, ride.x_start, ride.y_start)
        arrival_time = current_time + distance
        if arrival_time <= ride.earliest_start:
            return True
        else:
            return False

    @staticmethod
    def sortRidesByStart(rides):
        rides_length = len(rides)

        for i in range(0, rides_length):
            for r in range(0, rides_length - 1):
                start_1 = rides[r].earliest_start
                distance_1 = Mathss.calculate_distance(0, 0, rides[r].x_start, rides[r].y_start)
                distance_2 = Mathss.calculate_distance(0, 0, rides[r + 1].x_start, rides[r + 1].y_start)
                start_2 = rides[r + 1].earliest_start
                if start_1 + distance_1 > start_2 + distance_2:
                    temp = rides[r + 1]
                    rides[r + 1] = rides[r]
                    rides[r] = temp
        return rides

    @staticmethod
    def sortRidesByDistance(rides):
        rides_length = len(rides)

        for i in range(0, rides_length):
            for r in range(0, rides_length - 2):
                if rides[r].distance > rides[r + 1].distance:
                    temp = rides[r + 1]
                    rides[r + 1] = rides[r]
                    rides[r] = temp
        return rides

    @staticmethod
    def sortCarsByAvailibilityToNextRide(cars, ride):
        car_length = len(cars)

        for i in range(0, car_length):
            for r in range(0, car_length - 2):
                avail_1 = cars[r].avail_at
                avail_2 = cars[r + 1].avail_at
                distance_1 = Mathss.calculate_distance(cars[r].pos_x, cars[r].pos_y, ride.x_start, ride.y_start)
                distance_2 = Mathss.calculate_distance(cars[r + 1].pos_x, cars[r + 1].pos_y, ride.x_start, ride.y_start)
                if avail_1 + distance_1 > avail_2 + distance_2:
                    temp = cars[r + 1]
                    cars[r + 1] = cars[r]
                    cars[r] = temp
        return cars