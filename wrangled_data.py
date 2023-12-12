import pandas as pd
import matplotlib.pyplot as pl
import openpyxl as op


file_path = "top100banks.xlsx"
raw_data = pd.read_excel(file_path)

def data_countries():
    list_of_countries = []
    data_country = raw_data["country"]
    for i in data_country:
        list_of_countries.append(i)
    # print(list_of_countries)
    return list_of_countries


def view_full_data():
    pl.figure(figsize=(11, 7.5))
    pl.scatter(raw_data["country"], raw_data["total_assets_us_b"])
    pl.xlabel("Coutry")
    pl.ylabel("Total Bank Assets (US Bullion)")
    pl.title("Scatter Plot of ")
    pl.xticks(rotation=90)
    print(raw_data)
    pl.show()
    
    
def scatter_top5_banks(country, count=5):

    # View the top 5 banks in the world represented in a scatter plot
    top5_banks = raw_data[raw_data["country"] == country].sort_values(by="total_assets_us_b", ascending=False).head(int(count))
    ax = top5_banks.plot(x="bank", y="total_assets_us_b", kind="bar", rot=6, fontsize=7, figsize=(14,7))
    pl.title("The Top 5 Banks in " + country)
    ax.set_xlabel("Bank")
    ax.set_ylabel("Total Assets (US Bullion)")
    pl.show()
    

def top5_banks(country, count=5):
    
    print("made it into top 5 banks function")
    
    # See the top 5 banks in the world represented in the terminal
    top_5_assets = raw_data[raw_data["country"] == country].sort_values(by="total_assets_us_b", ascending=False).head(int(count))
    banks_assets = top_5_assets[["bank", "total_assets_us_b"]]
    banks_assets["rank"] = banks_assets.index + 1
    banks_assets.set_index("rank", inplace=True)
    print(banks_assets)
    
    # Pandas visualization of the data
    scatter_top5_banks(country, count="5")
    

def how_many_banks_in_top100(country, count=5):
    
    try:
        
        # Terminal Based data representation
        banks_ = raw_data[raw_data["country"] == country][["country", "bank", "total_assets_us_b"]].head(int(count))
        banks_["rank"] = raw_data["rank"]
        fiver = banks_.set_index("rank")
        print(fiver)
        
        # Pandas visualization of the data
        banks_.set_index("bank", inplace=True)
        ax = banks_.plot.area(stacked=True, figsize=(14,7), rot=8)
        pl.title("Area Plot of " + country + " Banks in The Top 100")
        pl.xlabel("Bank")
        pl.ylabel("Total Assets (US Bullion")
        pl.legend(loc="best")
        pl.show()
        
    except IndexError:
        print(country + " does not have any banks in the Top 100 Banks in the world")


def lessthan_500US_Bancorp(country,count=5):
    
    try:
        
        # Terminal Based data representation
        less_than = raw_data[(raw_data["total_assets_us_b"] < 500) & (raw_data["country"] == country)].head(int(count))
        less_t = less_than.reset_index(drop=True) 
        print(less_t)
    
        # Pandas visualization of the data
        filtered_data = raw_data[(raw_data["total_assets_us_b"] <= 500) & (raw_data["country"] == country)]
        less_500 = filtered_data.groupby("bank")["total_assets_us_b"].sum().sort_values(ascending=False).head(int(count))
        ax = less_500.plot(kind="barh", fontsize=8, figsize=(14,7))
        pl.title("Banks Earning Less Than 500(US Bullion) in " + country)
        ax.set_xlabel("Total Assets (US Bullion)")
        ax.set_ylabel("Bank")
        pl.show()
        
    except IndexError:
        print(country + " does not have any banks earning less than 500(US Bankcorp)")
    
    
def morethan_500US_Bancorp(country, count=5):
    
    try:
        
        # Terminal Based data representation
        more_than = raw_data[(raw_data["total_assets_us_b"] > 500) & (raw_data["country"] == country)].head(int(count))
        more_t = more_than.reset_index(drop=True) 
        print(more_t)
        
        # Pandas visualization of the data
        filtered_data = raw_data[(raw_data["total_assets_us_b"] >= 500) & (raw_data["country"] == country)]
        less_500 = filtered_data.groupby("bank")["total_assets_us_b"].sum().sort_values(ascending=False).head(int(count))
        ax = less_500.plot(kind="barh", fontsize=8, figsize=(14,7))
        pl.title("Banks Earning More Than 500(US Bullion) in " + country)
        ax.set_xlabel("Total Assets (US Bullion)")
        ax.set_ylabel("Bank")
        pl.show()
        
    except IndexError:
        print(country + " does not have any banks earning more than 500(US Bankcorp)")
    
    
def top10_banks(country, count=10):
    
    try:
        # Terminal Based data representation
        _banks = raw_data[raw_data["country"] == country].head(10)
        dem_banks = _banks.reset_index(drop=True)
        print(dem_banks)
        
        # Pandas vizualization of the data
        banks = _banks["bank"]
        assets = _banks["total_assets_us_b"]
        pl.figure(figsize=(11,8))
        pl.pie(assets, labels=banks, autopct='%1.1f%%', startangle=140)
        pl.title("Top 10 Banks in " + country)
        pl.show()
        
    except IndexError:
        print(country + " does not have any banks in the Top 100 Banks in the world")
    
