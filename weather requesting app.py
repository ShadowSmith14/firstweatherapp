import bs4, requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
n = ToastNotifier()
def getdata(url):
    r = requests.get(url)
    return r.text
page_content = requests.get("https://weather.com/en-IN/weather/today/l/cbaac1d32c1c53fb17b70538d11fb0f7a9b126f58b9515261d847f28c846d32c",cookies=dict(unitOfMeasurement="e")).content
soup = BeautifulSoup(page_content, 'html.parser')


def find_location():
    locator = 'div.CurrentConditions--header--27uOE h1.CurrentConditions--location--kyTeL'  # CSS locator
    item = soup.select_one(locator).string
    print(item)


def find_weather():
    locator = 'div.CurrentConditions--primary--2SVPh span.CurrentConditions--tempValue--3a50n'
    weather = soup.select_one(locator).string
    print(weather)
    return weather



def find_weather_type():
    locator = 'div.CurrentConditions--phraseValue--2Z18W'
    type_of = soup.select_one(locator).string
    print(type_of)



def as_of_time():
    locator = "div.CurrentConditions--timestamp--23dfw"
    as_of = soup.select_one(locator).string
    print(as_of)

find_location()
find_weather()
find_weather_type()

as_of_time()

result = "The current temp is " + find_weather().splitlines()[0] + " degrees in Republic"
n.show_toast("Live Weather Update", result, icon_path= 'C:\\Users\\brandsmp\\Documents\\java\\python\\hnet.com-image.ico', duration = 10)
