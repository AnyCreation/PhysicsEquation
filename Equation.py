
def Mass_Gravity_Weight(Mass: float, Gravity: float, Weight: float):
    """ 
    Système International d'unités (SI):
    -
        * Mass - Kg
        * Weight - Newtons

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


def Gravitational_Potential_Energy(Height: float, Weight: float, Joul: float):
    """ 
    Système International d'unités (SI):
    -
        * Height - meters
        * Weight - Newtons 
        
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


def distance_Velocity_Time(distance: float, Velocity: float, Time: float):
    """ 
    Système International d'unités (SI):
    -
        * Speed by [meters per second]
        * Time by [second]
        * distance by [meter]

    Base:
    -
        * distance = Velocity * Time
        * distance / Time = Velocity
        * distance / Velocity = Time
    """
    try: 
        if Velocity == None:
            return ["Velocity", distance / Time, "meter per second"]
        elif Time == None:
            return ["Time - Second", distance / Velocity]
        
        return ["Distance - Meter", Velocity * Time]
    
    except TypeError:
        return "Need more than one known element"


if __name__ == "__main__":
    Height_room = 2.5
    for i in range(0, 101):
        print(Gravitational_Potential_Energy(Height_room * i, 10, None), i)