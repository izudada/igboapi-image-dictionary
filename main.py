import json
import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

igbo_api_key_value = os.environ.get("IGBO_API_KEY")
igbo_api_key = {'X-API-Key': igbo_api_key_value}
pixabay_api_key = os.environ.get("PIXABAY_API_KEY")


@app.route("/")
def index():
    response = requests.get("https://igboapi.com/api/v1/words?keyword"
                            "=obi&page=2&range=%5B1%2C2%5D&strict"
                            "=true&dialects=true", headers=igbo_api_key)

    print(response.status_code)
    result = json.dumps(response.json())

    # Get image from pixabay using igba API word definiton
    pixa_endpoint = f"https://pixabay.com/api/?key={pixabay_api_key}&"
    "q=yellow+flowers&image_type=photo&pretty=true"

    return render_template()


if __name__ == '__main__':
    app.secret_key = 'secret@'
    app.run(debug=True)
