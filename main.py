class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other): 
        if self.sword_type == other.sword_type and self.sword_type == "bronze":
            return Sword("iron")
        elif self.sword_type == other.sword_type and self.sword_type == "iron":
            return Sword("steel")
        raise ValueError("can not craft")
    
    def __str__(self):
        return f"A new {self.sword_type} sword!"
    
def main():

    sword_1 = Sword("bronze")
    sword_2 = Sword("bronze")

    sword_3 = Sword("iron")
    sword_4 = Sword("iron")

    new_sword_1 = sword_1 + sword_2
    new_sword_2 = sword_3 + sword_4
    #new_sword_3 = sword_2 + sword_3
    print(new_sword_1)
    print(new_sword_2)
    #print(new_sword_3)

main()