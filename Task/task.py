import sys
from ride import Ride
from info import Info
from vehicle import Vehicle


def write(cars, out):
    with open(out, "w+") as handle:
        for car in cars:
            ids = ""
            for ride in car.completed_rides:
                ids += str(ride.id) + " "
            handle.write(str(len(car.completed_rides)) + ids + "\n")


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

        for r, line in enumerate(file_contents):
            l = line.split(' ')
            ride = Ride(int(l[0]),  # x_start
                        int(l[1]),  # y_start
                        int(l[2]),  # x_end
                        int(l[3]),  # y_end
                        int(l[4]),  # start
                        int(l[5]),  # finish
                        r - 1)  # id
            rides.append(ride)

        for car in range(0, info.cars):
            cars.append(Vehicle(0, 0, 0))



        out_name = sys.argv[1].split('/')[-1].split(".")[0]
        write(cars, out_name + ".out")


def sortRidesByStart(rides):
    rides_length = len(rides)

    for i in range(0, rides_length):
        for r in range(0, rides_length - 2):
            if rides[r].t_start > rides[r + 1].t_start:
                temp = rides[r + 1]
                rides[r + 1] = rides[r]
                rides[r] = temp
    return rides


def sortRidesByDistance(rides):
    rides_length = len(rides)

    for i in range(0, rides_length):
        for r in range(0, rides_length - 2):
            if rides[r].distance > rides[r + 1].distance:
                temp = rides[r + 1]
                rides[r + 1] = rides[r]
                rides[r] = temp
    return rides
