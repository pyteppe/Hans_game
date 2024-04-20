
from msilib.schema import Error


class Crouch:
    def __init__(self, can_crouch: bool):
        self.can_crouch = can_crouch

    def execute_crouch(self):
        print("crouching")
        #self.execute_animation(self.animation_dict[crouching])


    


class Jump():
    def __init__(self, jump_amount, jump_strength):
        self.max_jump_amount = jump_amount
        self.current_jump_amount = jump_amount

        self.jump_strength = jump_strength
        self.jump_button_curently_down = False

    
    def execute_jump(self, ground):
        
        self.rect.bottom -= 1 # To make shure it does jump when you press jump, and it doesn't loose its velosity due to tuching og ground
        self.execute_movement(just_move_pos=True)

        self.velocity[1] -= self.jump_strength
        self.current_jump_amount -= 1
        #self.execute_animation(self.animation["jump"])



class Blow:
    def __init__(self):
        self.blow_direction = [0, 1]


    def execute_blow(self, direction):
        if len(direction) != 2:
            raise Error("Direction not in possible directions...")
        self.blow_direction = direction







