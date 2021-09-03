import requests
import json
import util

""" Only for testing purpose
"""

getPatient_url = 'https://fhir-core-svc-prerelease.cfapps.eu10.hana.ondemand.com/fhir/Patient/8e9e9fb1-aab5-447b-9d72-3013775727a9'

token = ""

def getPatient():
    global token
    if token == "":
        token = util.fetch_client_token()
        if token == "":
            return

    headers = {}
    headers['Authorization'] = 'Bearer ' + token
    payload = None

    app_response = requests.get(
        getPatient_url,
        # stream = False,
        headers=headers,
        data=payload
    )
    json_formatted_str = json.dumps(app_response.json(), indent=2)
    print(json_formatted_str)