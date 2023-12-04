from typing import List

from project.vehicles.base_vehicle import BaseVehicle
from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = next((u for u in self.users if u.driving_license_number == driving_license_number), None)
        if user is not None:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."
        vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)
        if vehicle is not None:
            return f"{license_plate_number} belongs to another vehicle."
        new_vehicle = self.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route = next((r for r in self.routes if r.start_point == start_point and r.end_point == end_point), None)

        if route is not None:
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if route.length > length:
                route.is_locked = True

        route_id = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str,
                  route_id: int, is_accident_happened: bool):

        user = next(u for u in self.users if u.driving_license_number == driving_license_number)
        vehicle = next(v for v in self.vehicles if v.license_plate_number == license_plate_number)
        route = next(r for r in self.routes if r.route_id == route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return vehicle.__str__()

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        selected_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))[:count]

        for vehicle in selected_vehicles:
            vehicle.is_damaged = False
            vehicle.battery_level = 100
        return f"{len(selected_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda user: -user.rating)
        users = [u.__str__() for u in sorted_users]
        result = f"*** E-Drive-Rent ***\n"
        result += '\n'.join(users)
        return result
