class Vehicle:

    def __init__(self, pos_x, pos_y, idle_time):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.has_ride = False
        self.rides = []
        self.completed_rides = []
        self.avail_at = 0
        self.idle_time = idle_time
