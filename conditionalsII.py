# Imagine an air traffic control program that tracks 
# three variables, altitude, speed, and propulsion 
# which for a particular airplane have the values 
# specified below.

altitude = 10000
speed = 250
propulsion = "Propeller"

# For each of the following boolean expressions, work 
# out whether it evaluates to True or False and match 
# the correct value.

altitude < 1000 and speed > 100     # ===> False
(propulsion == "Jet" or propulsion == "Turboprop") and speed < 300 and altitude > 20000     # ===> False
not (speed > 400 and propulsion == "Propeller")     # ===> True
(altitude > 500 and speed > 100) or not propulsion == "Propeller"     # ===> True