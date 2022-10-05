#imports
from distutils.text_file import TextFile
import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime

def get_html_data(url):
    data = requests.get(url)
    return data

# taking the HTML data from website
def get_covid_detail_bd():
    # url = "https://worldometers.info/coronavirus/country/India"
    url = "https://worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_detail = ""

    # for block in info_div:
    #     text = block.find("h1", class_=None).get_text()
    #     count = block.find("span", class_=None).get_text()
    #     all_detail = all_detail + text + " " + count + "\n"

    # for getting the no. of cases
    for i in range(3):
        text = info_div[i].find("h1", class_ = None).get_text()
        count = info_div[i].find("span", class_ = None).get_text()
        all_detail = all_detail + text + " " + count + "\n"

    return all_detail
    # print(all_detail)


# country data
def get_country_data():
    name = textfield.get()
    url="https://worldometers.info/coronavirus/country/" + name
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_detail = ""

    # for block in info_div:
    #     text = block.find("h1", class_=None).get_text()
    #     count = block.find("span", class_=None).get_text()
    #     all_detail = all_detail + text + " " + count + "\n"

    for i in range(3):
        text = info_div[i].find("h1", class_ = None).get_text()
        count = info_div[i].find("span", class_ = None).get_text()
        all_detail = all_detail + text + " " + count + "\n"

    #changing return to label
    mainlabel['text']=all_detail

def reload():
    new_data = get_covid_detail_bd()
    mainlabel['text']=new_data

get_covid_detail_bd()

# used for making the GUI
root = tk.Tk()
root.geometry("900x700")
root.title("Covid19 Update Tracker")
f = ("poppins", 25, "bold")

# For importing the image
banner = tk.PhotoImage(file="/Users/govindkushwaha/Programming/Python/covidNotify/icon.png") #the file of the image is in this folder only
bannerlabel = tk.Label(root, image=banner)
bannerlabel.pack()

# creating text box
textfield = tk.Entry(root, width = 50)
textfield.pack()

# showing the data inside the window
mainlabel = tk.Label(root, text = get_covid_detail_bd(), font=f)
mainlabel.pack()

# get data button
gbtn = tk.Button(root, text="Get Data", font=f, relief='solid', command=get_country_data)
gbtn.pack()

# reload button
rbtn = tk.Button(root, text="Reload", font=f, relief='solid', command=reload)
rbtn.pack()
  
root.mainloop()