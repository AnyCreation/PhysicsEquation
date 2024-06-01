
def Mass_Gravity_Weight(Mass: float, Gravity: float, Weight: float) -> list:
    """
    Base: 
    -
        * Weight = Mass * Gravity

        * Weight / Gravity = Mass

        * Weight / Mass = Gravity
    """
    try: 
        if Mass == None:
            return ["Mass", Weight / Gravity]
        elif Gravity == None:
            return ["Gravity", Weight / Mass]
        
        return ["Weight", Gravity * Mass]
    
    except TypeError:
        return "Need more than one known element"


def Gravitational_Potential_Energy(Height: float, Weight: float, Joul: float) -> list:
    """ 
    Base:
    -
        * Joul = Weight * Height

        * Joul / Height = Weight

        * Joul / Weight = Height

    """
    try: 
        if Height == None:
            return ["Height", Joul / Weight]
        elif Weight == None:
            return ["Weight", Joul / Height]
        
        return ["Joul", Weight * Height]
    
    except TypeError:
        return "Need more than one known element"


if __name__ == "__main__":
    rooms = 4
    Height_room = 2.5
    Weight = 30
    print(Gravitational_Potential_Energy(Height_room * rooms, Weight, None))
    print(Gravitational_Potential_Energy(Height_room * (rooms ** 3), Weight, None))