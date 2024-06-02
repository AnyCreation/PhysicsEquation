import Equation

def Do(Choice, meaning_one, meaning_two, meaning_three):

    if Choice == "Mass_Gravity_Weight".replace("_", " "):
        return Equation.Mass_Gravity_Weight(meaning_one, meaning_two, meaning_three)
    elif Choice == "Gravitational_Potential_Energy".replace("_", " "):
        return Equation.Gravitational_Potential_Energy(meaning_one, meaning_two, meaning_three)
    elif Choice == "Distance_Velocity_Time".replace("_", " "):
        return Equation.Distance_Velocity_Time(meaning_one, meaning_two, meaning_three)

def Energy_WITH_MASS(meaning_one, meaning_two, meaning_three, meaning_four):
    return Equation.Gravitational_Potential_Energy_WITH_MASS(meaning_one, meaning_two, meaning_three, meaning_four)
