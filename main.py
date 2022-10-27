
from flask import( Flask , render_template , request)
import requests
from film_dir import country


response = requests.get(url= "https://hp-api.herokuapp.com/api/characters").json()
app = Flask(__name__)




@app.route('/')
def main():

    return render_template('index.html' , r = country)

if __name__ == "__main__":
    app.run(port=8089, debug=True)


