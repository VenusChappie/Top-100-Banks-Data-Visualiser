import pandas as pd
import matplotlib as plt

file_path = "top100banks.xlsx"
raw_data = pd.read_excel(file_path)

def view_full_data():
    print(raw_data)

def top5_banks():
    top_5_assets = raw_data.sort_values(by="total_assets_us_b", ascending=False).head(5)
    banks_assets = top_5_assets[["bank", "total_assets_us_b"]]
    banks_assets["rank"] = banks_assets.index + 1
    banks_assets.set_index("rank", inplace=True)
    print(banks_assets)


def most_freq_countries():
    values_count = raw_data["country"].value_counts()
    countries_ = values_count.head(5).reset_index()
    countries_.columns = ["country", "frequency"]
    countries_["rank"] = countries_.index + 1
    countries_.set_index("rank", inplace=True)
    print(countries_)


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
    print("HELP!")   

def handle_instruction(comm):
    command = comm.title()
    if command == "Help":
        return help()
    elif command == "Top 5 Countries":
        return most_freq_countries()
    elif command == "Top 5 Banks":
        return top5_banks()
    elif command == "Full Data":
        return view_full_data()
    else:
        print("Sorry we do not understand that command, please try again.")
        
        
def rungame():
    welcome()
    take_instructions()
    
def ascii_art(fn):
    f = open (fn, 'r')
    print(''.join([line for line in f]))
       
if __name__=="__main__":
    rungame()
