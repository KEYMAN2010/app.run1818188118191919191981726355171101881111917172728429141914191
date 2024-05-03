import flask
import requests

api_key = "X181BNMA11IQBAAKIIAK"
bypassing_api = "http://45.88.188.104:6087/api/adlinks/bypass?url="

app = flask.Flask(__name__)

@app.route("/xbypass/")
def xbypass():
    url = flask.request.args.get("url")
    if url is None:
        return flask.jsonify({"error": "No url provided"})
    if not url.startswith("https://") and not url.startswith("http://"):
        return flask.jsonify({"error": "Invalid url format. Must start with 'http://' or 'https://'"})
    
    # Constructing the URL with the api_key parameter
    full_url = bypassing_api + url + "&api_key=" + api_key
    
    # Making the request to the bypassing API
    response = requests.get(full_url)
    
    # Handling the response from the bypassing API
    if response.status_code == 200:
        api_data = response.json()
        if "bypassed" in api_data:
            return flask.jsonify({"bypassed_url": api_data["bypassed"]})
        else:
            return flask.jsonify({"error": "No bypassed URL found in the response data."})
    elif response.status_code == 500 and response.json().get("error") == "internal error lol contact shehajeez on discord":
        return flask.jsonify({"error": "Internal server error. Please try again later."})
    else:
        return flask.jsonify({"error": "Failed to bypass URL. Please try again later."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
