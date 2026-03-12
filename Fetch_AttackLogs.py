import requests
import json
from pathlib import Path
import time
from datetime import date, datetime

Log_Folder = r'Folder Location'

URL = "https://tas.indusface.com/wafportal/rest/siem/v1/getAttackInfo"
API_Key = ""

endTime = round(time.time() * 1000)
startTime = endTime - 300000

with open(Log_Folder + r'\Indusface.ini', "r") as file:
    API_Key = str(file.read().rstrip())

headers = {'content-type': 'application/json', "Authorization": "Bearer " + str(API_Key)}

data = {"startTime": startTime, "endTime": endTime}

response = requests.post(URL, data=json.dumps(data), headers=headers)

now = datetime.now()

try:
    response.raise_for_status()  # Check for HTTP errors
    response_json = response.json()
    
    logMessage = ""
    print("Response received:", response_json)  # Debug print

    if response_json.get('successMessage') == "Success":
        for row in response_json["data"]:
            if bool(row["attacks"]) == True:
                for attack in row["attacks"]:
                    logMessage += str(attack) + "\n"
    else:
        print("Response does not contain 'successMessage':", response_json)  # Debug print

    today = str(date.today())
    hour = now.strftime("%H")

    file = Path(Log_Folder + r'\indusface-' + today + '.log')
    file.touch(exist_ok=True)

    with open(file, "a") as text_file:
        text_file.write(logMessage)
except requests.exceptions.RequestException as e:
    print("HTTP request error:", e)  # Debug print
    file = Path(Log_Folder + r'\Error.log')
    file.touch(exist_ok=True)
    with open(file, "a") as text_file:
        current_time = now.strftime("%H:%M:%S")
        text_file.write(current_time + '   ' + str(e) + '\n')
        if 'response_json' in locals():
            text_file.write(current_time + '   ' + str(response_json.get('errorMessages', 'No error message')) + '\n')
except Exception as e:
    print("General error:", e)  # Debug print
    file = Path(Log_Folder + r'\Error.log')
    file.touch(exist_ok=True)
    with open(file, "a") as text_file:
        current_time = now.strftime("%H:%M:%S")
        text_file.write(current_time + '   ' + str(e) + '\n')
        if 'response_json' in locals():
            text_file.write(current_time + '   ' + str(response_json.get('errorMessages', 'No error message')) + '\n')
