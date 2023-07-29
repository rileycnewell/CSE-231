###########################################################
# Computer Project 1
#
# prompt user to input number of rods
# convert string to a floating point value
# print floating point value of rods
# perform simple mathematic conversions to convert rods to new values
# calculate how long in minutes it takes to walk given distance
# print conversions rounded to three decimal places
###########################################################
    
    
# user input number of rods component
rods_str = input("Input rods: ") # user entered value is a string
rods_float = float(rods_str) # convert string to float to perform math
print("\nYou input", rods_float, "rods.\n") # print value as floating point


# code moves on to simple mathematical conversions of rods to other units
meters_float = rods_float * 5.0292 # conversion for rods to meters
feet_float = meters_float / 0.3048 # conversion for rods to feet
miles_float = meters_float / 1609.34 # conversion for rods to miles
furlongs_float = rods_float / 40 # conversion for rods to furlongs


# code moves on to calculate time to walk distance in minutes
hours_float = miles_float / 3.1 # find walking time in hours
minutes_float = hours_float * 60 # convert to minues 


# code moves on to print rounded calculations
print("Conversions") # display conversions as title of list
print("Meters:", round(meters_float, 3)) # display meters, rounded
print("Feet:", round(feet_float, 3)) # display feet, rounded
print("Miles:", round(miles_float, 3)) # display miles, rounded
print("Furlongs:", round(furlongs_float, 3)) # display furlongs, rounded
print("Minutes to walk", rods_float, "rods:", round(minutes_float, 3)) \
# display minutes to walk the numnber of rods, rounded


    



