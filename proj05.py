###########################################################################
# Computer Project 05
# 
# Assign symbolic constants to be used throughout program, as opposed to \ 
# arbitrary numeric and character constants in the code.
#
# Define a function that takes nothing as a parameter and returns a  \
# filepointer.
#   If there is an error in the file name, print error and prompt again.
#   If file name is valid, open the file for reading.
#
# Define a function that takes a filepointer as a parameter and returns \
# a dictionary by state and a dictionary by crop.
#   Skip the first line (the header).
#   Create dictionary that has all 50 states as keys and sort in \
#   alphabetical order.
#   Create a list of each line in the file and extract certain values \
#   using indexing.
#   Using the dictionary containing all 50 states, create a nested \
#   dictionary giving the states values of crops and the crops values of \
#   years and percentages.
#   Create a dictionary that has all the crops in certain file and \
#   sort in alphabetical order. 
#   
# Define a function that takes the dictionary by state as a parameter and \
# returns a list of states and a list of crops.
#   Initialize empty lists.
#   Extract the state and crop keys in the nested dictionary the fucntion \
#   takes as a parameter and append them onto their respective empty lists.
#
# Define a function that takes the dictionary by state, the list of \
# states, and the list of crops as input and returns a new dictionary \
# containing the crop, state, and minimum and maximum years and values.
#   Initialize empty dictionary.
#   Create a dictionary with the keys as each crop in the list of crops \
#   and iterate through each of the states in the list of states.
#   If the crop is in the dictionary by state, then assign the min and max \
#   values to very high and low numbers, respectively. 
#   For each year and value in the dictionary by states, if the value is \
#   less than the minimum value or greater than the maximum value, update \ 
#   the value and assign the corresponding year to min/max year.
#   If the value is the same as the minimum or maximum value, take the \
#   smallest year.
#
# Define a main function where the defined functions will be called on \
# and the rest of the program will take place.
#   Print the crop.
#   Print header with specified formatting.
#   Print the data with specified formatting.
#   
###########################################################################


# Assign symbolic constants
STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', \
          'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', \
          'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', \
          'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', \
          'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', \
          'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', \
          'New Mexico', 'New York', 'North Carolina', 'North Dakota', \
          'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', \
          'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', \
          'Vermont', 'Virginia', 'Washington', 'West Virginia', \
          'Wisconsin', 'Wyoming']
STATE_INDEX = 0
CROP_INDEX = 1
VARIETY_INDEX = 3
YEAR_INDEX = 4
VALUE_INDEX = 6
MIN_VALUE = 10 ** 6
MAX_VALUE = -10 ** 6
HEADER_FORMAT = "{:<20s}{:>10s}{:>6s}{:>10s}{:>6s}"
DATA_FORMAT = "{:<20s}{:>10s}{:>6s}{:>10s}{:>6s}"
MAX_YEAR_INDEX = 0
MAX_VALUE_INDEX = 1
MIN_YEAR_INDEX = 2
MIN_VALUE_INDEX = 3


def open_file():
    
    '''
    
    Prompts a user to input a file name. If the file name 
    is invalid, an error is printed and the user is 
    prompted again. Otherwise, the file is opened.
    
    Returns: a filepointer
    
    '''
    
    # try to open the file provided with the input
    try:      
        filename = input("Enter a file: ") # prompts user to input file name
        fp = open(filename, "r")
    
    # if invalid file name, print an error and reprompt
    except FileNotFoundError:
        print("\nError in file name:" + " " + filename + "." + \
        " Please try again.")
        filename = input("Enter a file: ")
    
        
    fp = open(filename, "r")
    return fp
        
    
def read_file(fp):
    
    '''
    
    Creates a dictionary indexed by states and a 
    dictionary indexed by crops. These are both sorted 
    alphabetically and will be used throughout 
    the program.
    
    fp: filepointer
    
    Returns: a dictionary indexed by states (where 
    each state has a dictionary indexed by crops with years 
    and values), and a dictionary indexed by
    crops.  
    
    '''
    
    fp.readline() # skip the header
    
    # initialize empty dictionaries
    dictionary_by_state = {} 
    dictionary_by_crop = {}
    
    # create a dictionary in which each of the 50 states are keys
    # sort in alphabetical order
    for state in STATES:          
        dictionary_by_state[state] = {}
        states = list(dictionary_by_state.keys())
        states.sort()
        dictionary_by_state = {i:dictionary_by_state[i] for i in states}    
    
   # iterate through each line in the file
   # create a list containing each line in the file after removing whitespace
    for line in fp:
        line_list = line.strip().split(",")
        state = line_list[STATE_INDEX] # extract state
        state = state.strip()
        crop = line_list[CROP_INDEX] # extract crop
        variety = line_list[VARIETY_INDEX] # extract variety
        year = int(line_list[YEAR_INDEX]) # extract year, make int
        value = line_list[VALUE_INDEX] # extract value
              
        if state in STATES:
            
            # we are only interested in this variety
            if variety == "All GE varieties": 
                    
                # we are only interested in values that are digits
                if value.isdigit(): 
    
                        # now that we know it is digit, make int
                        value = int(line_list[VALUE_INDEX])
                        
                        # create a nested dictionary indexed by states, \
                        # where each state has a dictionary by crop \
                        # with years and percentages
                        if crop in dictionary_by_state[state]:
                            dictionary_by_state[state][crop][year] = value
                            
                        if crop not in dictionary_by_state[state]:
                            dictionary_by_state[state][crop] = {}
                            dictionary_by_state[state][crop][year] = value
                            
                        # create a dictionary containing crops present \
                        # in the file and sort alphabetically
                        dictionary_by_crop[crop] = {}
                        crops = list(dictionary_by_crop.keys())
                        crops.sort()
                        dictionary_by_crop = {i:dictionary_by_crop[i] for i in crops}
                    
    return dictionary_by_state, dictionary_by_crop
                       
                
def get_lists(dictionary_by_state):
    
    """
    
    Extracts states and crops from previously created 
    nested dictionary, and puts them into their own 
    respective lists.
    
    dictionary_by_state: large nested dictionary
    
    Returns: list_of_states, list_of_crops
    
    """
    
    # initialize empty lists
    list_of_states = [] 
    list_of_crops = []
        
    # extract each state from the big nested dictionary and append them \
    # onto the list of states
    for state in dictionary_by_state:
        list_of_states.append(state)
        
        # extract each crop from the big nested dictionary and append \
        # them onto the list of crops
        for crop in dictionary_by_state[state]:
            list_of_crops.append(crop)
            
            
    return list_of_states, list_of_crops
                
                
def find_values(dictionary_by_state, dictionary_by_crop, list_of_states, list_of_crops):
    
    """
    
    Extracts values from nested dictionary. Iterates 
    through values to find minimum and maximum values. 
    If the same value occurs twice, the
    smaller year is taken.
    
    dictionary_by_state: large nested dictionary
    
    list_of_states: list of all the states in large 
    nested dictionary
    
    list_of_crops: list of all the crops in large 
    nested dictionary
    
    Returns: values_by_crop, a new big nested dictionary 
    indexed by the crops in the file, where each crop has a 
    dictionary by crop with min and max years and values.
    
    """
    
    # initialize empty dictionary
    values_by_crop = {}
    
    # make each crop in the list of crops an index with empty dictionaries \
    # as values
    for crop in list_of_crops:
        
        if crop in dictionary_by_crop:
            values_by_crop[crop] = {}
            
            # iterate through each state in the list of states
            for state in list_of_states:
                
                if state in dictionary_by_state: 
                    
                    # if the crop is in the big nested dictionary
                    if crop in dictionary_by_state[state]:               
                        # initialize max value to an extremely small number, \
                        # and min value to an extremely large number
                        max_value = MAX_VALUE
                        min_value = MIN_VALUE
                        
                        # for each year and value in the big nested dictionary
                        for year, value in dictionary_by_state[state][crop].items():
                            
                            # if the value is smaller than the min value, \
                            # update the min value and make min year the year
                            if value < min_value:
                                min_value = value
                                min_year = year
                                
                            # if the value is the same as the min value, take the \
                            # smallest year it occurred
                            if value == min_value and year < min_year:
                                min_year = year
                            
                            # if the value is larger than the max value, update \
                            # the max value and make max year the year
                            if value > max_value:
                                max_value = value
                                max_year = year
                                
                            # if the value is the same as the max value, take the \
                            # smallest year it occurred
                            if value == max_value and year < max_year:
                                max_year = year
                                               
                        # update new big dictionary with the min and max years and \
                        # values
                        values_by_crop[crop][state] = [max_year, max_value, \
                                                       min_year, min_value]

    return values_by_crop
        
                            
def main():
    
    """
    
    Calls on the functions defined previously. Prints 
    crop, header, and data with specified formatting.
    
    """
    
    # call on all the functions that were previously defined
    fp = open_file()
    dictionary_by_state, dictionary_by_crop = read_file(fp)
    list_of_states, list_of_crops = get_lists(dictionary_by_state)
    values_by_crop = find_values(dictionary_by_state, dictionary_by_crop,
                                 list_of_states, list_of_crops)
    
    # for each crop in the sorted dictionary of crops
    for crop in dictionary_by_crop:
        
        # if the crop is in the list of crops, print crop and header with \
        # specified formattimg
        if crop in list_of_crops:
           print("\nCrop:", crop)
           print(HEADER_FORMAT.format("State", "Max Year", "Max", \
           "Min Year", "Min"))
           
           # under the crop and header, for each state in the big nested \
           # dictionary, extract min and max years and values using indexing
           for state in values_by_crop[crop].keys():
               max_year = str(values_by_crop[crop][state][MAX_YEAR_INDEX])
               max_value = str(values_by_crop[crop][state][MAX_VALUE_INDEX])
               min_year = str(values_by_crop[crop][state][MIN_YEAR_INDEX])
               min_value = str(values_by_crop[crop][state][MIN_VALUE_INDEX])
               
               # print with specified formatting
               print(DATA_FORMAT.format(state, max_year, max_value, \
                                        min_year, min_value))
       
           
if __name__ == "__main__":
    main()