from flask import Flask
from flask import render_template, request, url_for, redirect
import functions.json_tools as jt

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        
        dictStringAnimals = request.form.getlist("possibleAnimals")[0]
        dictStringFavorite = request.form.getlist("favoriteAnimal")[0]

        jt.save_config(dictStringAnimals, dictStringFavorite)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

