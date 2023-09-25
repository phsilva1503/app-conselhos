import requests
from translate import Translator

url = 'https://api.adviceslip.com/advice'

response = requests.get(url)
data = response.json()
conselho = data['slip']['advice']



translator = Translator(to_lang='pt')

conselhoPt = translator.translate(conselho)

print(conselho)
print(conselhoPt)

