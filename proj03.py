###########################################################################
# Computer Project 03
# 
# Define a function for opening a specific file containing data
#   Function repeatedly prompts for file names until a file successfully opens
# Define a function for finding the minimum percentage of change in GDP
#   Takes one argument, one line (str) from the GDP.txt file
#   Initialize minimum as a very, very large number
#   Function iterates through values in line and takes the smaller of the two
#   Returns minimum (float) and its index (int)
# Define a function for finding the maxmimum percetage of change in GDP
#   Takes one argument, one line (str) from the GDP.txt file
#   Initialize minimum as a very, very small number
#   Function iterates through values in line and takes the larger of the two
#   Returns maximum (float) and its index (int)
# Define a function that determines how many years from the starting year \
# that the minimum or maximum percent change occurs
#   Takes one argument, index (int)
#   Returns the number of years that occurred from min/max index the year the \
#   data was first being collected
# Define a function for determining the min/max GDP for each year
#   Takes two arguments, one line (str) from GDP.txt and an index (int)
#   Returns GDP value at the specific index
# Define a function that displays min/max change, GDP, and year
#   Takes six arguments and does not reutrn anything
#   Converts GDP from billions to trillions
#   Formatting matches guidelines
# Define a main function where the defined functions will be called on \
# and the rest of the program will take place
#   Loops through file to find starting year and access lines 9 and 44
#   Sets up values for the call to display function
#   
###########################################################################

def open_file():
   
    """ Asks to user to enter a file name while checking if it's an existing 
    file. """
    
    exit_boolean = False
    while exit_boolean != True:
        try:
            filename = input("Enter a file name: ")
            fp = open(filename, 'r')
        except FileNotFoundError:
            print("\nError. Please try again")
            continue
        exit_boolean = True
    return fp


def find_min_percent(line):
    
    """ Extracts values from specified line and iterates through them to find
    the smallest value in the line. """
    
    min_value = 10 ** 6  # start with an extremely large number
    min_value_index = 0 # initialize as 0
    index = 0 # initialize as 0
    
    for i in range(0, 46): # there are 47 data items
       
        # first data point is at index 76 and each spans 12 columns
        # first data item can be extracted using line[76:76+12]; this form \
        #    works for finding any data item in line given its index
        value = float(line[(76 + index * 12):(76 + (index + 1) * 12)])
        
        if value < min_value:
           
            # program iterates through values in the line, comparing two \
            #    values to each other and keeping the smaller one
            min_value = value
            min_value_index = (76 + index * 12)
            
        index += 1 # adds 1 each time to iterate through all data items in line
    return min_value, min_value_index


def find_max_percent(line):  
    
    """ Extracts values from specified line and iterates through them to find
    the largest value in the line. """
    
    max_value = -10 ** 6 # start with an extremely small number
    max_value_index = 0 # initialize as 0
    index = 0 # initialize as 0
    
    for i in range(0, 46): # there are 47 data items
    
        # first data point is at index 76 and each spans 12 columns
        # first data item can be extracted using line[76:76+12]; this form \
        #    works for finding any data item in line given its index
        value = float(line[(76 + index * 12):(76 + (index + 1) * 12)])
        
        if value > max_value:
            
            # program iterates through values in the line, comparing two \
            #   values to each other and keeping the larger one
            max_value = value
            max_value_index = (76 + index * 12) 
        
        index += 1 # adds 1 each time to iterate through all data items in line
    return max_value, max_value_index    
        

def years_from_starting(index):
    
    """ Takes an index as an argument and determines its deviation from the
    first year that data was collected. """
    
    # given index, subtract the starting column (76) and divide by the number \
    #   of columns the data item spans (12)
    years_from_starting = (index - 76)/12  
    return years_from_starting


def find_gdp(line, index):
    
    """ Given a specific line and index, goes through the data in the line and 
    returns the GDP value at the specified index value. """
    
    gdp = float(line[index:index + 12]) # gives data item at specified index 
    return gdp


def display(min_value, min_year, min_value_gdp, max_value, max_year, max_value_gdp): 
    
    """ Displays the six arguments min_value, min_year, min_value_gdp, 
    max_value,max_year, and max_value_gdp in specific formatting to match 
    anticipated output. """
    
    print("\n\nGross Domestic Product")
    print("{:<10s}{:>8s}{:>6s}{:>18s}".format("min/max", "change", "year", "GDP (trillions)"))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("min", float(min_value), int(float(min_year)), float(min_value_gdp)/1000))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("max", float(max_value), int(float(max_year)), float(max_value_gdp)/1000))


def main():
    
    """ Opens file and iterates through the lines to find information 
    concerning max/min percent change in GDP, and the years and GDP values
    that correspond. """
    
    fp = open_file() # open GDP.txt    
    count = 0 # set count variable to count lines in GDP.txt
    for line in fp: 
        count += 1 # add 1 each time GDP.txt has a new line
        
        if count == 8: # eighth line contains years
            year = line[76:76+12] # first data in line 8 is starting year
            year = int(year) # convert string to integer
        
        if count == 9: # ninth line contains change in GDP
        
            # call find_min_percent and find_max_percent functions to find \
            #   min/max values and their corresponding indicies in line 9
            min_value, min_value_index = find_min_percent(line) 
            max_value, max_value_index = find_max_percent(line)
            
            # call years_from_starting function to find how far the min/max \
            #   values are from the year data started to be collected
            min_from_starting = years_from_starting(min_value_index)
            max_from_starting = years_from_starting(max_value_index)
            
            # add the min/max years from starting to the year that data \
            #   started to be collected
            min_year = min_from_starting + year
            max_year = max_from_starting + year
        
        if count == 44:
            
            # call find_gdp function to find the GDP value that corresponds \
            #   to the min/max values
            min_value_gdp = find_gdp(line, min_value_index)
            max_value_gdp = find_gdp(line, max_value_index) 
   
    # call display function to print the six values with specific formatting
    display(min_value, min_year, min_value_gdp, max_value, max_year, max_value_gdp)
    fp.close()
    
    
# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
# DO NOT CHANGE THESE 2 lines  
if __name__ == "__main__":
    main()