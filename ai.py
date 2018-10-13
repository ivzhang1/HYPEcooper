import urllib3, requests, json

# retrieve your wml_service_credentials_username, wml_service_credentials_password, and wml_service_credentials_url from the
# Service credentials associated with your IBM Cloud Watson Machine Learning Service instance

wml_credentials={
  "password": "4b460114-ebcc-4b41-a104-a132b6a9096b",
  "url": "https://us-south.ml.cloud.ibm.com",
  "username": "e15325be-f0dd-4e66-a528-e24271caa7a2"
}

headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=wml_credentials['username'], password=wml_credentials['password']))
url = '{}/v3/identity/token'.format(wml_credentials['url'])
response = requests.get(url, headers=headers)
mltoken = json.loads(response.text).get('token')

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line

def getDictionary(dataset, day):
	payload_scoring = {"fields": ["time"], "values": [[day]]}

	links = {"chuckTay": "https://us-south.ml.cloud.ibm.com/v3/wml_instances/073a989d-6364-4e9a-b8ca-d7fbf1823d4c/deployments/1a8b7b82-0531-4b82-8711-29e2b2bd523e/online",
	 		"kithBogo": "https://us-south.ml.cloud.ibm.com/v3/wml_instances/073a989d-6364-4e9a-b8ca-d7fbf1823d4c/deployments/268d082e-b57e-427d-b4c4-3567b4fcf388/online", 
	 		"adidasTrip": "https://us-south.ml.cloud.ibm.com/v3/wml_instances/073a989d-6364-4e9a-b8ca-d7fbf1823d4c/deployments/07325ca6-da6e-4fb5-ae83-6fa0826eeaeb/online", 
	 		"hilfig":"https://us-south.ml.cloud.ibm.com/v3/wml_instances/073a989d-6364-4e9a-b8ca-d7fbf1823d4c/deployments/af36f863-ebd2-4636-b487-0d1c47da65c4/online", 
	 		"beluga":"https://us-south.ml.cloud.ibm.com/v3/wml_instances/073a989d-6364-4e9a-b8ca-d7fbf1823d4c/deployments/f6cfb93f-096a-4ee1-85bf-b92151e465b5/online"
	 		}
	magic = open('chucktay.csv', "w")
	for i in range(0, day):
		payload_scoring = {"fields": ["time"], "values": [[i]]}
		response_scoring = requests.post(links[dataset], json=payload_scoring, headers=header)

		magic.write('\n' + str(json.loads(response_scoring.text)['values'][0][2]) + ", " + str(i))

	magic.close()
	return (json.loads(response_scoring.text)['values'][0][2])

print(getDictionary("chuckTay", 700))