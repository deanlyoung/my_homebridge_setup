#!/usr/bin/env python
import requests

baseUrl = 'https://maker.ifttt.com/trigger/'
iftttKey = 'XXX'

openWeatherMapKey = 'XXX'
cityZip = 'XXXXX,US'
openWeatherMapUrl = 'http://api.openweathermap.org/data/2.5/weather?zip='

event = 'outside'

def setup():
	print '\n Begin outside weather program...'

def outsideWeather():
	weatherUrl = openWeatherMapUrl + cityZip + '&appid=' + openWeatherMapKey
	try:
		outsideTempData = requests.get(weatherUrl).json()
		outsideTemp = outsideTempData['main']['temp']
		fahrenheit = outsideTemp * 1.8 - 459.67
		outside_weather_maker_url = baseUrl + event + '/with/key/' + iftttKey
		outside_weather_payload = {}
		outside_weather_payload['value1'] = '{0:0.2f}'.format(fahrenheit)
		try:
			q = requests.get(outside_weather_maker_url, params=outside_weather_payload)
			print q.text
		except requests.exceptions.Timeout as e:
			# timeout
			print e
		except requests.exceptions.ConnectionError as e:
			# connection error
			print e
		except requests.exceptions.RequestException as e:
			# error
			print e
	except requests.exceptions.Timeout as e:
		# timeout
		print e
	except requests.exceptions.ConnectionError as e:
		# connection error
		print e
	except requests.exceptions.RequestException as e:
		# error
		print e

if __name__ == '__main__':
	setup()
	try:
		outsideWeather()
	except KeyboardInterrupt:
		pass