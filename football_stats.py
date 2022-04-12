import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


def getRowData(table_row, tag):
    """Function to get row data"""
    #list to store the row data
    rowList=[]
    #list that contains the required rows ie player name, position, team and total TD
    needed_rows=[0,1,2,6]
    #find the element using the tag passed in the function
    columns=table_row.find_all(tag)
    #comprehension loop to get the required row list
    col = [columns[i] for i in needed_rows] 
    for i in col:
        #for the list of items append the text without the element ie if <td>Jones</td> then append Jones
        rowList.append(i.get_text())
    #return the row list
    return rowList

def getTableData(table):
    """Function to get the column data"""
    #list to store columns
    columns=[]
    #get elements using tr element "ie table rows"
    table_rows=table.find_all("tr")

    #for all the table rows excluding the first two heading till the next 20 players
    for i in range(3,23):
        #call the getRowData function and append result in columns
        columns.append(getRowData(table_rows[i],"td"))
    #return the list of columns    
    return columns

def main():
    """The main function called when the script is executed"""
    #ignore SSL Certificates errors
    p_context = ssl.create_default_context()
    p_context.check_hostname = False
    p_context.verify_mode = ssl.CERT_NONE

    # fetch data
    url="https://www.cbssports.com/nfl/stats/playersort/nfl/year-2021-season-regular-category-touchdowns"
    web_page = urllib.request.urlopen(url, context=p_context).read()
    page=BeautifulSoup(web_page,"html.parser")
    #get the table elements
    stats_table=page.find("table")

    #pass the table to getTableData function and store data in data variable
    data=getTableData(stats_table)

    #print heading
    print("Player \t Position \t Team \t Total TD")

    #iterate the data and print with spaces in between
    for i in data:
        print(" \t".join(map(str,i)))

if __name__ == "__main__":
    main()

