import Equation as E

Equations = {
    "Mass Gravity Weight": lambda One, Two, Three: E.Mass_Gravity_Weight_3(One, Two, Three),

    "Gravitational Potential Energy": lambda One, Two, Three: E.Gravitational_Potential_Energy_3(One, Two, Three),

    "Gravitational Potential Energy WITH MASS": lambda One, Two, Three, Four: E.Gravitational_Potential_Energy_WITH_MASS_4(One, Two, Three, Four),

    "Distance Velocity Time": lambda One, Two, Three: E.Distance_Velocity_Time_3(One, Two, Three)
}