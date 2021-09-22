import sys
import time

#INTRO--------------------------------------------------------

print(
"""
#####  #####  #####  ####   #   #   ####  #   #  #####  #####
  #    #   #  #      #   #  #   #  #      #   #  #        #  
  #    ####   #####  ####   #   #  #      #####  #####    #  
  #    #  #   #      #   #  #   #  #      #   #  #        #  
  #    #   #  #####  ####    ###    ####  #   #  #####    #  
-------------------------------------------------------------
    Welcome to Trebuchet, the Interactive Terminal Game!
-------------------------------------------------------------
Additional Notes:

    By:             QBjack

    Based on:       Python

    Player/s:        1

    Inspired by:    - Engineering Lessons back in College
                    - The game Crusader Kings

    Topics used:    - Python: input(), variable assignments,
                              loops (for, while),
                              import commands,
                    - Physics: Kinematics
                    - Optimization               
""")

input("Press Enter to continue...")

print(
"""
-------------------------------------------------------------

PREMISE:
    The year is 1096, the beginning of the First Crusade.
The Papacy has issued a Holy War to all kingdoms and armies
of Christian faiths to take back Jerusalem from the Seljuks.

Your character is an exceptional siege engineer, hired by 
the fictional queen, Queen Leona of the fictional Lion
Empire, to engineer a trebuchet that can siege Seljuk walls.
""")

input("Press Enter to continue...")

print(
"""
-------------------------------------------------------------

STORY:
    Queen Leona, while searching her land for strong men to
bolster her army for the Holy War, has instead gotten word
of you, and has heard tales of your excellent mathematical
prowess during your days as a scholar. She has employed
you in her martial ranks to make practical use of your
scholarly mind.
""")

input("Press Enter to continue...")

print(
"""
-------------------------------------------------------------

OBJECTIVE:
    Your commander has instructed you to
enginner a trebuchet; however, you are using the
military budget! 
(Refer to the scoring and pricing section below)

As you're already familiar with the kinematic equations,
you know that the concerned variables are the following:

    - Distance, d
    - Time, t
    - Initial Velocity, Vi

These variables will calculate for the final velocity (Vf)
of a trebuchet's projectile when applied in the kinematics
formula, Vf = (2d/t) - Vi .

We assume the projectile's mass (m) and travel distance (d)
to be 1 kg and 3 km, respectively.
""")

input("Press Enter to continue...")

print(
"""
-------------------------------------------------------------

SCORING:
    The commander wants your trebuchet to have maximum
damage at mimimum price. As the Final Velocity is
calculated, a projectile's Force (F) can be calculated using

F = m * (Vf - Vi) / t .

PRICING:
    - Gold increases by 50 for every second less the
      projectile travels
    
    - Gold increases by 10 for every metric increase in
      the projectile's initial velocity

Again, maximum damage at mimimum price. Begin!
""")

input("Press Enter to continue...")

#LOGIC: VARIABLES------------------------------------------------------

#time
while True:
    try:
        t = int(input(
"""
Input Time Conditions:
    - must be a value
    - value must be more than zero
        
Time: """))

        if t < 1:
            print("Input must be more than zero. Try again.")
        else:
            break

    except Exception:
        print("Input must be a value. Try again.")

#initial velocity
while True:
    try:
        Vi = int(input(
"""
Input Initial Velocity Conditions:
    - must be a value
    - value must be more than zero
        
Initial Velocity: """))

        if Vi < 1:
            print("Input must be more than zero. Try again.")
        else:
            break

    except Exception:
        print("Input must be a value. Try again.")

#LOGIC: CALCUALTIONS---------------------------------------------------

#kinematics
Vf = (2 * 3000 / t) - Vi
a = (Vf - Vi) / 2
F = 1000 * a

#pricing
goldt = t * -50
goldVi = Vi * 10

print("\033c", end = "")

print("""
Input Values:
    - Time:             {} s
    - Initial Velocity: {} m/s

Constants:
    - Projectile Mass:  1000 g
    - Distance:         3000 m

""".format(t, Vi))

for everyx in range(5):
    print("Calculating" + "." * everyx)
    sys.stdout.write("\033[F")
    time.sleep(1)

print("""
Calculated Final Velocity:      {} m/s
Calculated Projectile Force:    {} N

Score: {}
""".format(Vf, F, goldt + goldVi))