import pandas as pd
import matplotlib as plt
import numpy as np
import matplotlib.pyplot as pl
import openpyxl as op
from scipy.stats import gaussian_kde
from scipy import stats




file_path = "top100banks.xlsx"
raw_data = pd.read_excel(file_path)


def view_full_data():
    pl.figure(figsize=(11, 7.5))
    pl.scatter(raw_data["country"], raw_data["total_assets_us_b"])
    pl.xlabel("Coutry")
    pl.ylabel("Total Bank Assets (US Bullion)")
    pl.title("Scatter Plot of ")
    pl.xticks(rotation=90)
    print(raw_data)
    pl.show()
    
    
def scatter_top5_banks():
    
    # View the top 5 banks in the world represented in a scatter plot
    top5_banks = raw_data.sort_values(by="total_assets_us_b", ascending=False).head(5)
    tryy = top5_banks.plot(x="bank", y="total_assets_us_b", kind="bar", rot=6, fontsize=5)
    tryy.set_xlabel("Bank")
    tryy.set_ylabel("Total Assets (US Bullion)")
    pl.show()
    

def top5_banks():
    
    # See the top 5 banks in the world represented in the terminal
    top_5_assets = raw_data.sort_values(by="total_assets_us_b", ascending=False).head(5)
    banks_assets = top_5_assets[["bank", "total_assets_us_b"]]
    banks_assets["rank"] = banks_assets.index + 1
    banks_assets.set_index("rank", inplace=True)
    print(banks_assets)
    scatter_top5_banks()
    

def most_freq_countries():
    
    # Terminal Based data representation
    five_countries = raw_data[["country", "bank", "total_assets_us_b"]]
    five_countries["rank"] = raw_data["rank"]
    fiver = five_countries.set_index("rank")
    print(fiver.head(5))
    
    # Pandas visualization of the data
    five_countries.set_index("country", inplace=True)
    ax = five_countries.plot.area(stacked=True, figsize=(10,6))
    pl.title("Area Plot of Top Five Countries")
    pl.xlabel("Countries")
    pl.ylabel("Total Assets (US Bullion")
    pl.legend(loc="best")
    pl.show()


def lessthan_500US_Bancorp():
    
    # Terminal Based data representation
    less_than = raw_data[raw_data["total_assets_us_b"] < 500].head(20)
    less_t = less_than.reset_index(drop=True) 
    print(less_t)
    
    # Pandas visualization of the data
    filtered_data = raw_data[raw_data["total_assets_us_b"] <= 500]
    less_500 = filtered_data.groupby("bank")["total_assets_us_b"].sum().sort_values(ascending=False).head(20)
    ax = less_500.plot(kind="barh", fontsize=6)
    ax.set_xlabel("Total Assets (US Bullion)")
    ax.set_ylabel("Bank")
    pl.show()
    
    
def morethan_500US_Bancorp():
    
    # Terminal Based data representation
    more_than = raw_data[raw_data["total_assets_us_b"] > 500].head(20)
    more_t = more_than.reset_index(drop=True) 
    print(more_t)
    
    # Pandas visualization of the data
    filtered_data = raw_data[raw_data["total_assets_us_b"] >= 500]
    less_500 = filtered_data.groupby("bank")["total_assets_us_b"].sum().sort_values(ascending=False).head(20)
    ax = less_500.plot(kind="barh", fontsize=6)
    ax.set_xlabel("Total Assets (US Bullion)")
    ax.set_ylabel("Bank")
    pl.show()
    
    
def top10_banks_china():
    
    # Terminal Based data representation
    china_banks = raw_data[raw_data["country"] == "China"].head(10)
    china = china_banks.reset_index(drop=True)
    print(china)
    
    # Pandas vizualization of the data
    banks = china_banks["bank"]
    assets = china_banks["total_assets_us_b"]
    pl.figure(figsize=(11,8))
    pl.pie(assets, labels=banks, autopct='%1.1f%%', startangle=140)
    pl.title("Top 10 Banks in China")
    pl.show()
    
def top10_banks_US():
    
    # View the top 10 banks in the US represented in the terminal
    us_banks = raw_data[raw_data["country"] == "USA"].head(10)
    united_states = us_banks.reset_index(drop=True)
    print(united_states)
    
    # View the top 10 banks in the US represented in a pie chart
    banks = us_banks["bank"]
    assets = us_banks["total_assets_us_b"]
    pl.figure(figsize=(10,8))
    pl.pie(assets, labels=banks, autopct='%1.1f%%', startangle=140)
    pl.title("Top 10 Banks in the US")
    pl.show()
    
def top10_banks_japan():
    
    # View the top 10 banks in japan represented in the terminal
    japan_banks = raw_data[raw_data["country"] == "Japan"].head(10)
    japan = japan_banks.reset_index(drop=True)
    print(japan)
    
    # View the top 10 banks in japan represented in 
    banks = japan_banks["bank"]
    assets = japan_banks["total_assets_us_b"]
    pl.figure(figsize=(10,8))
    pl.pie(assets, labels=banks, autopct='%1.1f%%', startangle=140)
    pl.title("Top 10 Banks in Japan")
    pl.show()
    
    
def top5_banks_germany():
    
    # View the top 10 banks in japan represented in the terminal
    german_banks = raw_data[raw_data["country"] == "Germany"].head(5)
    germany = german_banks.reset_index(drop=True)
    print(germany)
    
    # View the top 10 banks in japan represented in 
    banks = german_banks["bank"]
    assets = german_banks["total_assets_us_b"]
    pl.figure(figsize=(10,8))
    pl.pie(assets, labels=banks, autopct='%1.1f%%', startangle=140)
    pl.title("Top 5 Banks in Germany")
    pl.show()