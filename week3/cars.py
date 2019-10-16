import csv
import os

class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
    
    def get_photo_file_ext(self):
        root, ext = os.path.splitext(self.photo_file_name)

        return ext
    
    def __repr__(self):
        return " ".join([self.car_type, self.brand, self.photo_file_name, str(self.carrying)])


class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
    
    def __repr__(self):
        return super().__repr__() + " " + str(self.passenger_seats_count)


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_width, self.body_height, self.body_length = \
            tuple(map(float, body_whl.split('x'))) if body_whl else (0, 0, 0)
    
    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length
    
    def __repr__(self):
        return super().__repr__() + " " + " ".join(map(str, [self.body_width, self.body_height, self.body_length]))


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra
    
    def __repr__(self):
        return super().__repr__() + " " + self.extra


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if not row or len(row) < 5:
                continue
            
            car_type, brand, photo_file_name, carrying = row[0], row[1], row[3], float(row[5])

            if not (car_type and brand and photo_file_name and carrying):
                continue
                
            if car_type == 'car':
                passenger_seats_count = row[2]

                if passenger_seats_count and passenger_seats_count.isdigit():
                    car_list.append(Car(car_type, brand, photo_file_name, carrying, int(passenger_seats_count)))
            elif car_type == 'truck':
                body_whl = row[4]

                car_list.append(Truck(car_type, brand, photo_file_name, carrying, body_whl))
            elif car_type == 'spec_machine':
                extra = row[6]

                if extra:
                    car_list.append(SpecMachine(car_type, brand, photo_file_name, carrying, extra))


    return car_list

def _main():
    csv_filename = 'coursera_week3_cars.csv'

    vehicles = get_car_list(csv_filename)
    
    for vehicle in vehicles:
        print(vehicle.get_photo_file_ext())

        if vehicle.car_type == 'truck':
            print(vehicle.get_body_volume())

if __name__ == '__main__':
    _main()