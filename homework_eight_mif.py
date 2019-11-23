class Car:
    max_speed = 310
    horse_power = 520
    production_year = 2019

    def __init__(self, color, model, made):
        self.color = color
        self.model = model
        self.made = made

    def drive(self):
        print(f"I am move {self.color}, {self.model}, {self.made} car")

    def sound(self):
        print("makes a sound")

    def stop(self):
        print(f"stop {self.color}, {self.model}, {self.made} machine")


car_bmw = Car(color='blue', model='bmw', made='Germany')
print(car_bmw.drive())
print(car_bmw.max_speed)


class Plane:
    max_speed = 1400
    horse_power = 4500
    production_year = 2016

    def __init__(self, color, model, made):
        self.color = color
        self.model = model
        self.made = made

    def fly(self):
        print(f"I am fly {self.color}, {self.model}, {self.made} plane")

    def sound(self):
        print("makes a sound")

    def autopilot(self):
        print(f"I fly without arms on {self.color}, {self.model}, {self.made} plane")


ty_134 = Plane(model='Concort', color='black', made='Chine')
print(ty_134.model)


class Ship:
    max_speed = 60
    horse_power = 1200
    production_year = 2014

    def __init__(self, color, model, made):
        self.color = color or 'White'
        self.model = model
        self.made = made

    def swim(self):
        print(f"I am swim on {self.color}, {self.model}, {self.made} ship")

    def sound(self):
        print("makes a sound")

    def anchoring(self):
        print(f"Whistle anchors! {self.color}, {self.model}, {self.made} in my ship!")


yacht = Ship(color='green', model='wow', made='Italy')
yacht.sound()
print(yacht.anchoring())


class AmphibianMachine(Car, Plane, Ship):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def swim(self):
        super().swim()
        print(f'I am the WITCHER!')


gerald = AmphibianMachine(color='red', model='witcher', made='Chechnya')

gerald.anchoring()
gerald.swim()
print(gerald.max_speed)
print(ty_134.max_speed)