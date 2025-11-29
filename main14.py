class vehicle:
    def __init__(self,name,mileage,speed):
        self.name = name
        self.speed = speed
        self.mileage = mileage

class bus(vehicle):
    pass

school_bus = bus("School volvo",12,180)
print("Vehicle name:", school_bus.name, "vehicle mileage:", school_bus.mileage, "vehicle speed:", school_bus.speed)