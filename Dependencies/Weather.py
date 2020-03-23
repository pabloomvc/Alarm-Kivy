import requests
from bs4 import BeautifulSoup

def getWeather():
    # Set the URL you want to webscrape from
    url = """https://weather.com/es-CL/tiempo/hoy/l/a64186d9cfcc8ba1b5212834f28d189fc0699cbdd1c364c40920bbe4fbb0a7ea"""
    try:
        # Connect to the URL
        response = requests.get(url)
        # Parse HTML and save to BeautifulSoup object
        soup = BeautifulSoup(response.text, "html.parser")
        #Temperatura actual
        currentTemp = soup.find('div',{"class": "today_nowcard-temp"}).text
        desc = soup.find('div', {"class": "today_nowcard-phrase"}).text
        #print(currentTemp, desc)
        #Maxima y minima
        lista = list(soup.find('div', {"class": "today_nowcard-hilo"}))
        maxTemp = lista[1].text
        minTemp = lista[4].text
        #print("Max: {}C / Min: {}C".format(maxTemp,minTemp))
        d = {"currentTemp":currentTemp, "description":desc, "maxTemp":maxTemp, "minTemp":minTemp}
        return d
    except ConnectionError:
        pass

