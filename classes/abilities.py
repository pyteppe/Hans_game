
from msilib.schema import Error


class Crouch:
    def __init__(self, can_crouch: bool):
        self.can_crouch = can_crouch

    def execute_crouch(self):
        self.execute_animation(self.crouch_animation)


    


class Jump():
    def __init__(self, jump_amount, jump_strength):
        self.jump_amount = jump_amount
        self.doble_jump_done = 0
        self.jump_strength = jump_strength
        self.jump_button_curently_down = False

    
    def execute_jump(self):
        print("jump")
        #self.execute_animation(self.animation["jump"])
        #self.y_velocity -= self.jump_strength



class Blow:
    def __init__(self, direction:list):
        self.blow_direction = direction


    def execute_blow(self, direction):
        if direction not in self.blow_direction:
            raise Error("Direction not in possible directions...")
        




