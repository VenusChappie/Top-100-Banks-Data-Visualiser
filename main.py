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
    
def take_instructions():
    
    while True:
        command = input("Please enter a command: ")
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
 

def handle_instruction(comm):
    command = comm.title()
    if command == "Help":
        help_box = help()
        return print(help_box)
    elif command == "Top 5 Countries":
        # Done
        return dt.most_freq_countries()
    elif command == "Top 5 Banks":
        # Done
        return dt.top5_banks()
    elif command == "Full Data":
        # Done
        return dt.view_full_data()
    elif command == "Below 500 Billion Assets":
        # Done
        return dt.lessthan_500US_Bancorp()
    elif command == "Above 500 Billion Assets":
        # Done
        return dt.morethan_500US_Bancorp()
    elif command == "Top 10 Banks China":
        # Done
        return dt.top10_banks_china()
    elif command == "Top 10 Banks USA":
        # Done
        return dt.top10_banks_US()
    elif command == "Top 10 Banks Japan":
        return dt.top10_banks_japan()
    elif command == "Top 5 Banks Germany":
        return dt.top5_banks_germany()
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
