import os
from dotenv import load_dotenv
import requests
import openai

# Wczytaj zmienne środowiskowe z pliku .env
load_dotenv()

# Pobierz klucze API ze zmiennych środowiskowych
api_key_aidevs = os.getenv('API_KEY_AIDEVS')
api_key_openai = os.getenv('API_KEY_OPENAI')

# Podstawowe dane do autoryzacji
url_base = 'https://tasks.aidevs.pl/'
data = {
    "apikey": api_key_aidevs
}

# Pobierz token
response = requests.post(url_base + 'token/embedding', json=data)
response_json = response.json()
token = response_json.get('token', None)
print("token: " + token)

# Pobierz zadanie
response = requests.get(url_base + 'task/' + token)
response_json = response.json()
cookie_value = response_json.get('cookie', None)
print("Zadanie:")
print(response_json)

# Ustaw klucz API OpenAI
openai.api_key = api_key_openai

# Generowanie embeddingu dla frazy "Hawaiian pizza"
phrase = "Hawaiian pizza"

embedding_response = openai.Embedding.create(
    input=phrase,
    model="text-embedding-ada-002"
)

embedding = embedding_response['data'][0]['embedding']
print("Embedding generated for 'Hawaiian pizza':")
print(embedding)

# Przygotowanie danych do wysłania
answer_data = {
    "answer": embedding
}

# Wyślij odpowiedź na endpoint /answer
response = requests.post(url_base + 'answer/' + token, json=answer_data)
response_json = response.json()
print("Rezultat:")
print(response_json)
