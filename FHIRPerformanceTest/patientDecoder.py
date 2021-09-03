import json
import uuid

def getPatientJson(line):

    lineItems = line.split('#')

    with open('Patient.json', 'r') as patientFile:
        data = patientFile.read()

    # change json
    obj = json.loads(data)

    #generate guid
    uuidRandom =  str(uuid.uuid4())
    obj['id'] = uuidRandom

    #generate ID
    identifiers = obj['identifier']
    for identifier in identifiers:
        if identifier['use'] == "usual":
            identifier['value'] = lineItems[0]

    names = obj['name']
    for name in names:
        if name['use'] == "official":
            name['given'][0] = lineItems[1]
            name['family'] = lineItems[2]


    return obj

