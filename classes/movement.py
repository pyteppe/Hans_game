from msilib.schema import Error


class Movement:
    def __init__(self, velocity: list, acceleration: list, acceleration_acceleration=[0, 0]):
        self.velocity = velocity
        self.acceleration = acceleration
        self.acceleration_acceleration = acceleration_acceleration
    
    def execute_movement(self):
        self.acceleration[0] = self.acceleration_acceleration[0]
        self.acceleration[1] = self.acceleration_acceleration[1]
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]



    


