from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import ssl
import time

def getTableData(table):
    """Function to get the column data"""
    #list to store columns

    columns=[]
    #get elements using tr element "ie table rows"
    table_rows=table.find_all("tr")
    for i in table_rows:
        #Using the tag td, get the closing value and text
        closing_price=i.find_all("td")[0].get_text()
        #get the date using the tag td and get text
        date=i.find_all("th")[0].get_text()
        #append to columns
        columns.append([closing_price, date])
    #return the columns
    return columns

def main():
    driver = webdriver.Chrome(executable_path="D:/Notes/bill-kassebakayoko/python csv/IS211_Assignment9/chromedriver.exe")
    driver.get("https://www.nasdaq.com/market-activity/stocks/aapl/historical")
    #delay of some kind wait for load time.sleep(3) or selenium wait for an element to be visible
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(1)
    page = BeautifulSoup(driver.page_source, 'lxml')

    #obtain the table's elements
    stats_table=page.find("tbody")

    #pass the table to the getTableData function, and the data is stored in the data variable
    data=getTableData(stats_table)

    #print heading
    print("Closing Price \t Dates")

    #iterate the data and print with spaces in between
    for i in data:
        print(" \t".join(map(str,i)))

if __name__ == "__main__":
    main()
