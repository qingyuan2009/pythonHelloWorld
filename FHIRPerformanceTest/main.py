import temp
import patientDecoder
import json

def main():
    #temp.getPatient()

    file = open('data.txt', 'r')
    Lines = file.readlines()
    count = 0

    for line in Lines:
        count = count + 1
        if count > 1:
            json_formatted_str = json.dumps(patientDecoder.getPatientJson(line), indent=2)
            print(json_formatted_str)

main()