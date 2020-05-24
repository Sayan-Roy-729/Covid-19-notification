from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notify_me(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon  = 'C:/Users/Sanchayan/Desktop/Python Practice with Harry/icon.ico',
        timeout = 5,
    )

def getData(url):
    r = requests.get(url)
    return r.text



if __name__ == "__main__":

    while True:

        # notify_me("Sayan", "Lets stop the spread of this virus together")
        myHTMLData = getData('https://www.mohfw.gov.in/')

        # print(myHTMLData)
        soup = BeautifulSoup(myHTMLData, 'html.parser')
        # print(soup)
        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()
        
        myDataStr = myDataStr[1:]

        itemList = myDataStr.split("\n\n")

        states = ['West Bengal']

        for item in itemList[0:34]:
            dataList = item.split("\n")
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases of Covid-19'
                nText = f" State--> {dataList[1]} \nTotal active cases---> {dataList[2]} \nCured/Discharged/Migrated--> {dataList[3]} \nDeaths--> {dataList[4]}"
                notify_me(nTitle, nText)
                time.sleep(4)
        
        time.sleep(5400)
                

