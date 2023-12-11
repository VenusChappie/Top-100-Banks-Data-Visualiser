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
    message = str("Unfortunately this country does not have any banks listed in the Top 100 Banks in the World\nPlease try again.")
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
    table.add_row(["Top 5 Banks", "Show the top 5 banks"])
    table.add_row(["Full Data", "View the full dataset"])
    table.add_row(["Below 500 Billion Assets", "Show banks with assets below 500 billion USD"])
    table.add_row(["Above 500 Billion Assets", "Show banks with assets above 500 billion USD"])
    table.add_row(["Top 10 Banks China", "Show the top 10 banks in China"])
    table.add_row(["Top 10 Banks USA", "Show the top 10 banks in the USA"])
    table.add_row(["Top 10 Banks Japan", "Show the top 10 banks in Japan"])
    table.add_row(["Top 5 Banks Germany", "Show the top 5 banks in Germany"])
    
    return table.get_string()

def call_all(country, count):
    print("I got to call all function")
    toppi = dt.top5_banks(country, count)
    # dt.lessthan_500US_Bancorp(country, count)
    # dt.morethan_500US_Bancorp(country, count)
    # dt.how_many_banks_in_top100(country, count)
    # dt.top10_banks(country, count=10)
 

def handle_instruction(comm):
    
    # print("I made it to handle instruction")
    
    country_list = dt.data_countries()
    
    blem = comm.split(" ")

    # Assigning the country and count from the user input
    country = blem[0]
    if len(blem) > 1:
        count = blem[1]
    
    # Standardizing the input from the user 
    command = country.title()
    print(command)
    
    # Handling the command from the user.
    if command == "Help":
        help_box = help()
        return print(help_box)
    elif command == "Full Data":
        return dt.view_full_data()
    elif command not in country_list:
        return print(country_notFound())
    elif command in country_list:
        print("I passed the condition that checks if the country exists")
        return call_all(command, count) 
    else:
        print("\nSorry we do not understand that command, please try again.\n")
        
        
def rungame():
    welcome()
    take_instructions() 
    # dt.lessthan_500US_Bancorp("US")
    # dt.data_countries()

    
def ascii_art(fn):
    f = open (fn, 'r')
    print(''.join([line for line in f]))
       
if __name__=="__main__":
    rungame()
