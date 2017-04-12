#!/usr/bin/env python
import requests
import json

base = 'https://maker.ifttt.com/trigger/'
key = 'XXX'

uv_event = 'current_uv_index'

def setup():
	print '\n UV Index begins...'

def uv():
	zipCode = 'XXXXX'
	url = 'http://api.wunderground.com/api/XXX/conditions/q/' + zipCode + '.json'
	try:
		uvjdata = requests.get(url).json()
		uv_index = uvjdata['current_observation']['UV']
		maker_url = base + uv_event + '/with/key/' + key
		payload = {}
		payload['value1'] = '{0}'.format(uv_index)
		try:
			q = requests.get(maker_url, params=payload)
			print q.text
			
			pushover_url = 'https://api.pushover.net/1/glances.json'
			params_p = {}
			params_p['token'] = 'XXX'
			params_p['user'] = 'XXX'
			params_p['count'] = '{0:.0}'.format(uv_index)
			try:
				p = requests.post(pushover_url, params_p)
				print p.text
			except requests.exceptions.Timeout as e:
				print e
			except requests.exceptions.ConnectionError as e:
				print e
			except requests.exceptions.RequestException as e:
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
		uv()
	except KeyboardInterrupt:
		pass