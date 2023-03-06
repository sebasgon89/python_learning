import requests
from datetime import datetime

# Excersise part
GENDER = "Male"
WEIGHT_KG = 75
HEIGHT_CM = 175
AGE = 33

APP_ID = "1f3c59cb"
API_KEY = "cf9a4fa0ef44c503f71803954b567bb6"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

print(result)

# Sheety part - GET
url = 'https://api.sheety.co/c838cbaa1e0a35f100b6441cefcf78c2/myWorkouts/workouts'
url_filter = 'https://api.sheety.co/c838cbaa1e0a35f100b6441cefcf78c2/myWorkouts/workouts?filter[duration]=22'
print(requests.get(url=url).json())
print(requests.get(url=url_filter).json())

# Sheety part - POST
workout: {
    'date': '2023-03-03',
    'time': '16:00',
}

url_post = 'https://api.sheety.co/c838cbaa1e0a35f100b6441cefcf78c2/myWorkouts/workouts'
# requests.post(url_post)
# Esto no hizo nada

# la de Angela
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

# Basic Authentication

YOUR_USERNAME = "sheetyseba"
YOUR_PASSWORD = "wbIS9tlv"

sheet_response = requests.post(
    url=url,
    json=sheet_inputs,
    auth=(
        YOUR_USERNAME,
        YOUR_PASSWORD,
    ),
    headers="Authorization: Basic c2hlZXR5c2ViYTp3YklTOXRsdg=="
)

# sheet_response = requests.post(url, json=sheet_inputs)
# print(sheet_inputs)
# print(sheet_response.text)

# sheet_response = requests.post(exercise_endpoint, json=sheet_inputs)
#
# print(sheet_response.text)
