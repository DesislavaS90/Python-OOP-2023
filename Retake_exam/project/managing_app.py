from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VALID_VEHICLE_TYPES = {'PassengerCar': PassengerCar, 'CargoVan': CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        driving_license = [d for d in self.users if d.driving_license_number == driving_license_number]
        if driving_license:
            return f'{driving_license_number} has already been registered to our platform.'
        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f'{first_name} {last_name} was successfully registered under DLN-{driving_license_number}'

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        plate = [d for d in self.vehicles if d.license_plate_number == license_plate_number]

        if vehicle_type not in self.VALID_VEHICLE_TYPES:
            return f'Vehicle type {vehicle_type} is inaccessible.'

        if plate:
            return f'{license_plate_number} belongs to another vehicle.'

        self.vehicles.append(self.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number))
        return f'{brand} {model} was successfully uploaded with LPN-{license_plate_number}.'

    def allow_route(self, start_point: str, end_point: str, length: float):
        route = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point and r.length == length]
        smaller_length = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point and r.length < length]
        bigger_length = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point and r.length > length]

        if route:
            return f'{start_point}/{end_point} - {length} km had already been added to our platform.'

        if smaller_length:
            return f'{start_point}/{end_point} shorter route had already been added to our platform.'

        if bigger_length:
            bigger_length[0].is_locked = True

        self.routes.append(Route(start_point, end_point, length, len(self.routes) + 1))
        return f'{start_point}/{end_point} - {length} km is unlocked and available to use.'

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        driving_license = [d for d in self.users if d.driving_license_number == driving_license_number][0]
        plate = [p for p in self.vehicles if p.license_plate_number == license_plate_number][0]
        route = [r for r in self.routes if r.route_id == route_id][0]

        if driving_license.is_blocked:
            return f'User {driving_license.driving_license_number} is blocked in the platform! This trip is not allowed.'
        if plate.is_damaged:
            return f'Vehicle {plate.license_plate_number} is damaged! This trip is not allowed.'
        if route.is_locked:
            return f'Route {route.route_id} is locked! This trip is not allowed.'

        plate.drive(route.length)

        if is_accident_happened:
            plate.change_status()
            driving_license.decrease_rating()
        else:
            driving_license.increase_rating()  # here instead using increase, by mistake I used decrease

        return str(plate)

    def repair_vehicles(self, count: int):
        damaged_cars = [d for d in self.vehicles if d.is_damaged]
        damaged = sorted(damaged_cars, key=lambda d: (d.brand, d.model))

        if count > len(damaged):
            result = damaged[:count - len(damaged)]

        else:
            result = damaged[:count]

        for v in result:
            v.change_status()
            v.recharge()
        return f'{len(result)} vehicles were successfully repaired!'

    def users_report(self):
        result = [f'*** E-Drive-Rent ***']
        for user in sorted(self.users, key=lambda u: -u.rating):
            result.append(str(user))

        return '\n'.join(result)
