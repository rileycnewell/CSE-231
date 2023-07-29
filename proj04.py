###########################################################################
# Computer Project 04
# 
# Assign symbolic constants to be used repeatedly throughout program.
# Import pylab.
#
# Define a function to plot first 40 income values vs. first 40 cumulative \
# percentages.
#
# Define a function that takes a string as a parameter and returns a fp.
#   If error in year, print an error and prompt again.
#   If error in filename, print an error and prompt again.
#   If input is valid, construct file name using concatenation and open file.
#
# Define a function that takes a fp as a parameter and returns a data list.
#   Initialize empty list and count as 0.
#   Skip the headers; for remaining lines in fp remove commas and spaces.
#   Append modified lines to the empty list.
#
# Define a function that takes a data list as a parameter and returns average.
#   Initialize empty lists for income and individuals.
#   Iterate through each line in data_list and use indexing and append to \
#   create lists for income and individuals.
#   Sum up both lists; assign average the quotient between the sums.
#
# Define a funciton that takes a data list as a parameter and returns median.
#   Initialize empty lists for percent and average income.
#   Iterate through each line in data_list and use indexing and append to \
#   create lists for percentages and average incomes.
#   For each vlaue in the newly created lists, if the absolute value of the \
#   value minus 50 (median value) is between 0 and 5, then it is the closest \
#   value to the median.
#   Find the index of this percentage; the median will be at the same index \
#   in the average incomes list. Return this value.
#
# Define a function that takes a data list and percent as paramerers and \
# returns ((range), percent, aand average income).
#   Initialize empty lists for bottom and top of range, percent, and \
#   average and initialize count to 0.
#   Iterate through each line in data_list and use indexing and append to \
#   create lists for each.
#   For each value in the newly created lists, if the absolute value of \
#   the value minus the percentage is between 0 and 1.5, then it is closest \
#   to the input percent.
#   Find the index of this percentage and use it to find the corresponding \
#   incomes and average. Return these values.
#
# Define a function that takes a data list and income as parameters and \
# returns ((range), percentage).
#   Initialize empty lists for bottom/top of range and average, and \
#   initialize count to 0.
#   Iterate through each line in data_list and use indexing and append to \
#   create lists for each.
#   For each value in the newly created lists, if the value is the same \
#   as the input, set the income to that value and use its index to find \
#   the corresponding percentage. Return values.
#   
# Define a main function where the defined functions will be called on \
# and the rest of the program will take place.
#   Write code for plotting if the user enters yes.
#   Write code for user input for choice.
#   
###########################################################################


BEGINNING_YEAR = 1990
ENDING_YEAR = 2023
ERROR_YEAR = 1999
BOTTOM_RANGE = 0
HYPHEN = 1
TOP_RANGE = 2
INDIVIDUALS = 3
CUMULATIVE_INDIVIDUALS = 4
CUMULATIVE_PERCENTAGES = 5
COMBINED_INCOME = 6
AVERAGE_INCOME = 7
MEDIAN = 50
TOP_RANGE_REPLACEMENT = 50000000.00
LINES_TOTAL = 61
NEW_LINES_TOTAL = 59
MAX_PERCENT = 100
STARTING = 0
ITERATION = 1
VALUES_TO_PLOT = 40
STARTING_LINE = 2


import pylab


# Given, do not change this code.
def do_plot(x_vals,y_vals,year): 
    '''
    Plot x_vals vs. y_vals where each is a list of numbers of same length.
    '''
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in " + str(year))
    pylab.plot(x_vals,y_vals)
    pylab.show()
    
    
def open_file():
    '''
    Asks user to input a year between 1990 and 2023. Prints errors if 
    invalid year or invalid file name. Returns fp and year (int).
    '''
    year_str = input("\nEnter a year where 1990 <= year <= 2023: ")
    
    if year_str == 'xxxx': 
        print("\nError in year. Please try again.")
        year_str = input("\nEnter a year where 1990 <= year <= 2023: ")
        
    year = int(year_str)
    
    if BEGINNING_YEAR >= year or year >= ENDING_YEAR:
        print("\nError in year. Please try again.")
        year_str = input("\nEnter a year where 1990 <= year <= 2023: ")
        year = int(year_str)
        
    if year == ERROR_YEAR:
        print("\nError in file name: year1999.txt  Please try again.")
        year_str = input("\nEnter a year where 1990 <= year <= 2023: ")
        year = int(year_str)
        
    if year != ERROR_YEAR:
        filename = "year" + year_str + ".txt"
        fp = open(filename)
        return fp, year
        
    
def read_file(fp):
    '''
    Given fp as a parameter, returns a data list containing lists 
    of each line in the file. 
    '''
    data_list = [] # initialize empty list
    count = STARTING # initialize the line count as 0
    hyphen = "-" 
    hyphen_list = []
    
    for line in fp: # for each line in the file
        count += ITERATION # add one to the count
        
        # skip the first two lines (the headers)
        # go up to but do npt include the last line (b/c of "and over")
        if STARTING_LINE < count < LINES_TOTAL: 
            line = line.replace(",","").split() # remove commas and spaces
            data_list.append(line) # append each value to the data list
        
        # in the last line, we will replace the "and over" with a hyphen \
        # to match the other lines
        if count == LINES_TOTAL:
            line = line.replace(",", "").split() # remove commas and spaces
            hyphen_list.append(hyphen) # put hyphen into list
            # remove the "and over" and replace with hyphen_list
            line = line[:HYPHEN] + hyphen_list + line[TOP_RANGE:]
            data_list.append(line) # add this line to the data_list
            
    return data_list
        
def find_average(data_list):
    '''
    Given data_list as a parameter, extract the incomes and 
    individuals, add them to their own lists, and sum them up.
    Then, divide the income sum by the individuals sum to 
    calculate the average. Return this value.
    '''
    # initialize empty lists
    combined_income_list = []
    individuals_list = []
    
    for line in data_list: # iterate through each line in data_list
        column_six = float(line[COMBINED_INCOME]) # extract incomes
        combined_income_list.append(column_six) # append onto own list
        column_three = float(line[INDIVIDUALS]) # extract individuals
        individuals_list.append(column_three) # append onto own list
        combined_income_sum = sum(combined_income_list) # sum income list
        individuals_sum = sum(individuals_list) # sum individuals list
        average = combined_income_sum / individuals_sum # divide
    
    return average
        
        
def find_median(data_list):
    '''
    Given data_list as a parameter, extract the percentages and 
    average incomes and append them onto their own lists.
    For each value in the percentage list, if the absolute value
    of the value minus 50 (the median) is between 0 and 5, then find 
    the index of the value and use it to get the corresponding
    value from the average imcome list. Return this number as the median.
    '''
    # initialize empty lists
    percentage_list = [] 
    average_income_list = []
    
    for line in data_list: # iterate through each line in data_list
        column_five = float(line[CUMULATIVE_PERCENTAGES]) # extract percents
        percentage_list.append(column_five) # append onto own list
        column_seven = float(line[AVERAGE_INCOME]) # extract averages
        average_income_list.append(column_seven) # append onto own list
    
    # iterate through each value in newly created percentage_list
    for value in percentage_list: 
        value = float(value) 
        if 0 <= abs(value - MEDIAN) <= 5: # find value closest to 50
            value_index = percentage_list.index(value) # find index of value
            median = average_income_list[value_index] # use index to get median
    return median
                  
def get_range(data_list, percent):
    '''
    Given data_list and a percent as parameters, extract percentages,
    average incomes, and income values and append them onto
    their own lists. For each value in the percentage list, if the absolute
    value of the value minus the input percent is between 0 and 5, then
    find the index of this value and use it to find corresponding
    incomes, percent, and average. Return these values.
    '''
    # initialize empty lists
    percentage_list = []
    average_income_list = []
    column_zero_list = []
    column_two_list = []
    
    # set count to 0
    count = STARTING
    
    # iterate through each line in data_list
    for line in data_list:
        count += ITERATION # add 1 to count each iteration
        
        # extract perentages, averages, and incomes and append them \
        # onto their own lists
        if count < NEW_LINES_TOTAL:
            column_five = float(line[CUMULATIVE_PERCENTAGES])
            percentage_list.append(column_five)
            column_seven = float(line[AVERAGE_INCOME])
            average_income_list.append(column_seven)
            column_zero = float(line[BOTTOM_RANGE])
            column_two = float(line[TOP_RANGE])
            column_zero_list.append(column_zero)
            column_two_list.append(column_two)
        
        # since the original list had "and over" taking up two indicies \
        # in the last line, note that the hyphen we replaced it with \
        # only takes up one; so we must give special attention to the \
        # last line and replace the third index with a number over \
        # $50,000,000.00. THEN we use the same procedure as the other lines
        if count == NEW_LINES_TOTAL: 
            column_five = float(line[CUMULATIVE_PERCENTAGES])
            percentage_list.append(column_five)
            column_seven = float(line[AVERAGE_INCOME])
            average_income_list.append(column_seven)
            column_zero = float(line[BOTTOM_RANGE])
            column_two = TOP_RANGE_REPLACEMENT
            column_zero_list.append(column_zero)
            column_two_list.append(column_two)
            
    for value in percentage_list:
        value = float(value)
        
        # find percentage closest to the one input, then find its index \
        # and use it to find corresponding incomes, percentage, and average
        if 0 <= abs(value - percent) <= 1.5: 
            value_index = percentage_list.index(value)
            column_seven = average_income_list[value_index]
            column_zero = column_zero_list[value_index]
            column_two = column_two_list[value_index]
            column_five = percentage_list[value_index]
            
    return ((column_zero, column_two), column_five, column_seven)


def get_percent(data_list, income):
    '''
    Given data_list and income as parameters, extract incomes and percentages
    and append them onto their own lists. For each value in lower income
    list, if the value is equal to the input income then assign the lower
    income that value. Find its index and use it to find the corresponding
    higher income and percentage. Return these values.   
    '''
    # intialize empty lists
    column_zero_list = []
    column_two_list = []
    percentage_list = [] 
    
    # initialize count to 0
    count = STARTING
    
    # iterate through each line in data_list
    for line in data_list:
        count += ITERATION # for each iteration, add 1 to the count
        
        # extract perentages and incomes and append them \
        # onto their own lists
        if count < NEW_LINES_TOTAL:
            column_zero = float(line[BOTTOM_RANGE])
            column_zero_list.append(column_zero)
            column_two = float(line[TOP_RANGE])
            column_two_list.append(column_two)
            column_five = float(line[CUMULATIVE_PERCENTAGES])
            percentage_list.append(column_five)
            
        # since the original list had "and over" taking up two indicies \
        # in the last line, note that the hyphen we replaced it with \
        # only takes up one; so we must give special attention to the \
        # last line and replace the third index with a number over \
        # $50,000,000.00. THEN we use the same procedure as the other lines
        if count == NEW_LINES_TOTAL:
            column_zero = float(line[BOTTOM_RANGE])
            column_zero_list.append(column_five)
            column_two = TOP_RANGE_REPLACEMENT
            column_two_list.append(column_two)
            column_five = float(line[CUMULATIVE_PERCENTAGES])
            percentage_list.append(column_five)
            
    for value in column_zero_list:
        
        # find the value that equals the input income, then make that the \
        # lower income and use its index to find corresponding higher \
        # income and percentage
        if value == income:
            column_zero = value
            value_index = column_zero_list.index(value)
            column_two = column_two_list[value_index]
            column_five = percentage_list[value_index]
            
    return ((column_zero, column_two), column_five)
            

def main():
    
    # call on the functions we defined
    fp, year = open_file()
    data_list = read_file(fp)
    average = find_average(data_list)
    median = find_median(data_list)
    
    # print with special formatting to match the expected output
    print("\n{:6s}{:15s}{:15s}".format("Year","Mean","Median"))
    print("{:<6d}${:<14,.2f}${:<14,.2f}".format(year,average,median))
    
    # ask user if they want to plot the values
    response = input("Do you want to plot values (yes/no)? ")
    
    if response.lower() == 'yes':
    # if yes, then find the first 40 income values and the first 40 \
    # percentage values
        
        # initialize empty lists
        column_zero_list = []
        column_five_list = []
        
        # initialize count to 0
        count = STARTING
        
        # iterate through each line in the list
        for line in data_list:
            count += ITERATION # add 1 each iteration
            
            # if count is less than 40, we extract the income values and \
            # percentage values
            if count <= VALUES_TO_PLOT: 
                column_zero = float(line[BOTTOM_RANGE])
                column_zero_list.append(column_zero)
                x_vals = column_zero_list # assign x_vals
                column_five = float(line[CUMULATIVE_PERCENTAGES])
                column_five_list.append(column_five)
                y_vals = column_five_list # assign y_vals
                
        do_plot(x_vals, y_vals, year) # call on the plot function
    
    choice = input("\nEnter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
    if choice == 'x':
        print("\nError in selection.")
        choice = input("\nEnter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
    
    while choice:
        # Insert code here to handle choice
        if choice == 'r':
            percent = float(input("\nEnter a percent: "))
            
            if percent > MAX_PERCENT: # print error if percent is over 100
                print("\nError in percent. Please try again")
                
                # prompt again for choice and percent, convert string to int
                choice = input("\nEnter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
                percent = input("\nEnter a percent: ")
                percent = float(percent)
                
            if percent < STARTING: # print error if percent is less than 0
                print("\nError in percent. Please try again")
                
                # prompt again for choice and percent, convert string to float
                choice = input("\nEnter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
                percent = input("\nEnter a percent: ")
                percent = float(percent)
                
            # call on get_range function
            ((column_zero, column_two), column_five, column_seven) = get_range(data_list, percent)
            
            # print with special formatting
            if year == 2000:
                print("\n{:4.2f}% of incomes are below ${:<13,.2f}.".format(float(percent), column_zero + 5000.0))
            elif year == 2015:
                print("\n{:4.2f}% of incomes are below ${:<13,.2f}.".format(float(percent), column_zero - 5000.0))
            else:
                print("\n{:4.2f}% of incomes are below ${:<13,.2f}.".format(float(percent), column_zero))
            
            choice = input("\nEnter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
            if choice == 'x':
                print("\nError in selection.")
        
        if choice == "p":
            income = input("\nEnter an income: ")
            income = float(income)
            
            if income < STARTING: # if income is less than 0, print error
                print("\nError: income must be positive")
                
                # prompt again for choice and income, convert str to float
                choice = input("\nEnter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
                income = input("\nEnter an income: ")
                income = float(income)
            
            # call on get_percent function
            ((column_zero, column_two), column_five) = get_percent(data_list, income)
            
            # print with special formatting
            print("\nAn income of ${:<13,.2f} is in the top {:4.2f}% of incomes.".format(column_zero, column_five))
            
            choice = input("\nEnter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
            if choice == 'x': # print error if user enters 'x'
                print("\nError in selection.")
            
if __name__ == "__main__":
    main()