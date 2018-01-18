#!/usr/bin/env python
import requests

baseUrl = 'https://maker.ifttt.com/trigger/'
iftttKey = 'XXX'
event = 'outside'

lat = 'XXX'
lon = 'XXX'
wundergroundApiKey = 'XXX'
wundergroundUrl = 'http://api.wunderground.com/api/'

def setup():
	print '\n Begin outside weather program...'

def outsideWeather():
	weatherUrl = wundergroundUrl + wundergroundApiKey + '/conditions/q/' + lat + ',' + lon + '.json'
	try:
		outsideData = requests.get(weatherUrl).json()
		outsideTemp = outsideData['current_observation']['temp_c']
		fahrenheit = outsideTemp * 1.8 + 32
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