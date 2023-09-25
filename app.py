from flask import Flask, render_template
import requests
from translate import Translator


app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def conselhos():
        url = 'https://api.adviceslip.com/advice'

        response = requests.get(url)
        data = response.json()
        conselho = data["slip"]['advice']

        translator = Translator(to_lang='pt')
        conselhopt = translator.translate(conselho)
        return  render_template('conselho.html', conselho=conselho, conselhopt=conselhopt)

#rodar a aplicação
if __name__ == "__main__":
        app.run(debug = True)