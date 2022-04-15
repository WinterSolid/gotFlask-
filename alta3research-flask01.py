from flask import Flask
from flask import request
from flask import jsonify
from flask import sessions
import json

app= Flask(__name__)
app.secret_key = "Winteriscoming"

gotdata= [{
	"name": "Jon Snow",
	"gender": "Male",
	"aliases": [
		"Lord Snow",
		"Ned Stark's Bastard",
		"The Snow of Winterfell",
		"The Crow-Come-Over",
		"The 998th Lord Commander of the Night's Watch",
		"The Bastard of Winterfell",
		"The Black Bastard of the Wall",
		"Lord Crow"
	],
	"allegiances": [
		"https://anapioficeandfire.com/api/houses/362"
	]
    }]

@app.route("/protected/<name>")
def session_option(name):
	session["username"] = name

	if session["username"] == "Winteriscoming":
		return (jsonify(gotdata))
	else: 
		return "Only kings of the North may enter!"		
# get/post to data then append data

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
           data= json.loads(data)
           name = data["name"]
           gender = data["gender"]
           aliases = data["aliases"]
           allegiances = data["allegiances"]
           gotdata.append({"name":name,"gender":gender,"aliases":aliases,"allegiances":allegiances})
	# filters data through jsonify
    return jsonify(gotdata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)



	