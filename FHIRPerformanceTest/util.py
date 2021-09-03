import requests

# Configurable vars
conf_auth_url = "https://saas-shg.authentication.eu10.hana.ondemand.com/oauth/token"
conf_client_id = "sb-hl7-fhir-service-a8299212-88c3-47ce-912c-ee12cd821771!b88462|hl7-fhir-service-prerelease!b63380"
conf_client_secret = "ljuFcHunoeArJ4H0bG7Ur1PGxBk="

def fetch_client_token():
    oauth_response = requests.get(
        conf_auth_url + "?grant_type=client_credentials",
        auth=(conf_client_id, conf_client_secret))
    if oauth_response.status_code != 200:
        print('Gen token error: %d' % oauth_response.status_code)
        return ""
    token = oauth_response.json()['access_token']
    #print('Gen token:\n%s' % token)
    print('Token fetched!')
    return token