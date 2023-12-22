import wrangled_data as dt
from prettytable import PrettyTable 

def welcome():
    
    ascii_art('asciiArt.txt')
    
    name = input("Please enter your name: ")
    welcome_message = (f"""\nWelcome {name}! \n\n   This program is here to make reading, understanding and vsiualizing data more 
    convienient for you. \n\n   How you ask? \n
    I've created simple keywords you can use to textually analyse or visually see
    the most important aspects of the data available.\n
    To see what keywords are available, please type 'HELP' below""")
    
    print(welcome_message)
    
def country_notFound():
    
    message = str("\nUnfortunately this country does not have any banks listed in the Top 100 Banks in the World\n\nPlease try again.\n")
    return message
    
def take_instructions():
    
    while True:
        command = input("Please enter a country and argument Eg. : ")
        handle_instruction(command)

def help():
    table = PrettyTable()
    table.field_names = ["Command", "Description"]
    table.add_row(["Help", "Display help and instructions"])
    table.add_row(["Top 5 Countries", "Show the top 5 countries"])
    table.add_row(["Full Data", "View the full dataset"])
    table.add_row(["[Country of your choice]", "Will return banks in the Top 100 if any"])
    
    
    return table.get_string()

def call_all(country, count):

    dt.top5_banks(country, count)
    dt.lessthan_500US_Bancorp(country, count)
    dt.morethan_500US_Bancorp(country, count)
    dt.how_many_banks_in_top100(country, count)
    dt.top10_banks(country, count)

def standardize_input(comm):
    
    list_of_input = comm.split(" ")
    
    results = []
    
    if len(list_of_input) > 2:
        country = list_of_input[0] + " " + list_of_input[1]
        count = list_of_input[2]
    elif len(list_of_input) > 1:
        country = list_of_input[0]
        count = list_of_input[1]
    elif len(list_of_input) == 1:
        country = list_of_input[0]
        count = 5
        
    if country == "usa":
        country = "USA"
    elif country == "uk":
        country = "UK"
    else:
        country = country.title()
        
    results.append(country)
    results.append(count)
    
    return results

def handle_instruction(comm):
        
    country_list = dt.data_countries()
    
    standard_check = standardize_input(comm)
    
    command = standard_check[0]
    count = standard_check[1]
    
    # Handling the command from the user.
    if command == "Help":
        return print(help())
    elif command == "Full Data":
        return dt.view_full_data()
    elif command not in country_list:
        return print(country_notFound())
    elif command in country_list:
        return call_all(command, count) 
    else:
        print("\nSorry we do not understand that command, please try again.\n")
        
        
def rungame():
    welcome()
    take_instructions() 
    
def ascii_art(fn):
    f = open (fn, 'r')
    print(''.join([line for line in f]))
       
if __name__=="__main__":
    rungame()
