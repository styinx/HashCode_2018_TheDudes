import sys
from ride import Ride
from info import Info
from vehicle import Vehicle
from mathss import Mathss


def write(cars, out):
    with open(out, "w+") as handle:
        for i, car in enumerate(cars):
            ids = ""
            for j, r in enumerate(car.completed_rides):
                ids += str(car.completed_rides[j].id) + " "
            out_str = str(len(cars[i].completed_rides)) + " " + ids + "\n"
            print(out_str)
            handle.write(out_str)


def printRides(rides):
    for r in range(0, len(rides)):
        print(str(rides[r].id) + ": " + str(rides[r].earliest_start))

def printCars(cars):
    for r in range(0, len(cars)):
        print(str(len(cars[r].completed_rides)))

if __name__ == "__main__":

    if len(sys.argv) > 1:
        with open(sys.argv[1], mode="r") as file:
            file_contents = file.readlines()

        first_line = file_contents[0].split(' ')
        info = Info(int(first_line[0]),  # rows
                    int(first_line[1]),  # cols
                    int(first_line[2]),  # cars
                    int(first_line[3]),  # rides
                    int(first_line[4]),  # bonus
                    int(first_line[5]))  # step
        rides = []
        cars = []

        ride_lines = file_contents[1:]
        for r, line in enumerate(ride_lines):
            l = line.split(' ')
            ride = Ride(int(l[0]),  # x_start
                        int(l[1]),  # y_start
                        int(l[2]),  # x_end
                        int(l[3]),  # y_end
                        int(l[4]),  # start
                        int(l[5]),  # finish
                        r)  # id
            rides.append(ride)

        for car in range(0, info.cars):
            cars.append(Vehicle(0, 0, 0))

        rides = Mathss.sortRidesByStart(rides)

        for i, car in enumerate(cars):
            cars[i].rides.append(rides[0])
            cars[i].avail_at += Mathss.calculate_distance(cars[i].pos_x, cars[i].pos_y, rides[0].x_start, rides[0].y_start) + rides[0].distance
            cars[i].completed_rides.append(rides[0])
            cars[i].pos_x = rides[0].x_end
            cars[i].pos_x = rides[0].y_end
            del rides[0]

        while len(rides) > 0:
            cars = Mathss.sortCarsByAvailibilityToNextRide(cars, rides[0])
            cars[0].rides.append(rides[0])
            cars[0].avail_at += Mathss.calculate_distance(cars[0].pos_x, cars[0].pos_y, rides[0].x_start,rides[0].y_start) + rides[0].distance
            cars[0].completed_rides.append(rides[0])
            cars[0].pos_x = rides[0].x_end
            cars[0].pos_x = rides[0].y_end
            del rides[0]

            #printCars(cars)

        out_name = sys.argv[1].split('/')[-1].split(".")[0]
        write(cars, out_name + ".out")