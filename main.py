import json
import os
import requests
from flask import Flask

app = Flask(__name__)

# iNITIALIZING IGBO API AND PIXABAY API KEYS
igbo_api_key_value = os.environ.get("IGBO_API_KEY")
igbo_api_key = {'X-API-Key': igbo_api_key_value}
pixabay_api_key = os.environ.get("PIXABAY_API_KEY")


@app.route("/api/v1/<string:igbo_word>")
def index(igbo_word):

    """
    iA single endpoint that queries Igbo API endpoint for an igbo_word,
    gets various definitions of that word, sends each derivate through
    pixabay API with the end result of getting corresponding images to
    """

    images = []

    # Hitting Igbo API endpoint
    response = requests.get(f"https://igboapi.com/api/v1/words?keyword={igbo_word}", headers=igbo_api_key)
    result = response.json()
    
    words = [word.split(";") for x in result for word in x['definitions']]

    for array in words:
        for word in array:
            if len(word) > 0:
                # Get image from pixabay using igba API word definiton
                pixa_image = requests.get(f"https://pixabay.com/api/?key={pixabay_api_key}&q={word}&image_type=photo&pretty=true") 
                pixa_result = pixa_image.json()
                images += [data['webformatURL'] for data in pixa_result['hits'][0:1]]
        
    return {"images":images}


if __name__ == '__main__':
    app.secret_key = os.environ.get("APP_SECRET")
    app.run(debug=True)
