import jwt
import requests
import json
from time import time
import datetime

x = datetime.datetime.now()

def generateToken(API_KEY, API_SEC):
	token = jwt.encode(

		# Create a payload of the token containing
		# API Key & expiration time
		{'iss': API_KEY, 'exp': time() + 5000},

		# Secret used to generate token signature
		API_SEC,

		# Specify the hashing alg
		algorithm='HS256'
	)
	# token = str(token)
	return token.decode('utf-8')


# create json data for post requests


# send a request with headers including
# a token and meeting details


def createMeeting(topic,start ,API_KEY, API_SEC):
	headers = {'authorization': 'Bearer ' + generateToken(API_KEY, API_SEC),
			'content-type': 'application/json'}
	r = requests.post(
		f'https://api.zoom.us/v2/users/me/meetings',
		headers=headers,
		data=json.dumps({
			"topic": topic,
			"type": 2,
			"start_time": x.strftime("%Y-%m-%d")+"T"+start+"00",
			"duration": "90",
			"agenda": "test",
			"recurrence": {
				"type": 1,
				"repeat_interval": 1
			},
			"settings": {
				"host_video": "true",
				"participant_video": "true",
				"join_before_host": "False",
				"mute_upon_entry": "False",
				"watermark": "true",
				"audio": "voip",
				"auto_recording": "cloud"
			}
		})
	)

	print("\n creating zoom meeting ... \n")
	# print(r.text)
	# converting the output into json and extracting the details
	y = json.loads(r.text)
	join_URL = y["join_url"]
	meetingPassword = y["password"]
	return join_URL, meetingPassword
