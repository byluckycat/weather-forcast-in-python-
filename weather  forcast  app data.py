"weather  forcast this is  medium  code "

#import the necessary package;
import requests
#input the city name
city = input('input the city name')
print(city)
# or you can also hard - code  the value
# city = "delhi"

#display the massage
print('Display weather report for: ' + city)
#fetch the weather details
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

#display the result !
print(res.text)