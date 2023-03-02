import requests

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