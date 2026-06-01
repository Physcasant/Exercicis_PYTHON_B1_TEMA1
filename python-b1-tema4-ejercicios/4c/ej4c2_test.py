import pytest
from ej4c2 import Car, Bicycle, Vehicles


class TestVehicles:
    def test_drive_car(self):
        car = Car()
        assert car.drive() == "Driving a car", "Car.drive() should return 'Driving a car'"

    def test_drive_bicycle(self):
        bicycle = Bicycle()
        assert bicycle.drive() == "Riding a bicycle", "Bicycle.drive() should return 'Riding a bicycle'"

    def test_drive_vehicles_abstract_method(self):
        with pytest.raises(TypeError):
            vehicle = Vehicles()
            vehicle.drive()

    def test_drive_car_instance_of_vehicles_class(self):
        car = Car()
        assert isinstance(car, Vehicles), "Car should be an instance of Vehicles"

    def test_drive_bicycle_instance_of_vehicles_class(self):
        bicycle = Bicycle()
        assert isinstance(bicycle, Vehicles), "Bicycle should be an instance of Vehicles"
