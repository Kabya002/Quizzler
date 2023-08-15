import requests

parameters = {
    "amount": 20,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

# category = data["results"][0]["category"]
# type = data["results"][0]["type"]
# difficulty = data["results"][0]["difficulty"]
# question = data["results"][0]["question"]
# correct_answer = data["results"][0]["correct_answer"]
# incorrect_answers = data["results"][0]["incorrect_answers"]


