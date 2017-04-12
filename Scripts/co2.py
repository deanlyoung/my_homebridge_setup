#!/usr/bin/env python
import requests
import json
from urllib import urlopen

base = 'https://maker.ifttt.com/trigger/'
key = 'XXX'

event = 'co2'

def setup():
	print '\n Begin CO2 program...'

def co2():
	url = 'http://www.hqcasanova.com/co2/'
	try:
		str1 = urlopen(url).read()
		wrd1 = str1.split(' ', 1)[0]
		co2 = float(wrd1)
		co2_maker_url = base + event + '/with/key/' + key
		co2_payload = {}
		co2_payload['value1'] = '{0:0.2f}'.format(co2)
		try:
			u = requests.get(co2_maker_url, params=co2_payload)
			print u.text
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
		co2()
	except KeyboardInterrupt:
		pass