import os
from flask import Flask, request, jsonify,  render_template
from flask_cors import CORS
from ai_logic import summarize_text, explain_topic, extract_deadlines

app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return"CampusGenie API is running!"
@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/summarize",methods=["GET","POST"])
def summarize():
    if request.method=="GET":
      return jsonify({
          "message":"Summarize API is running",
          "usage":"Send POST request with JSON:{'text':'your text here'}"
           })
    data = request.json
    text = data.get("text", "")
    summary = summarize_text(text)
    return jsonify({"summary": summary})

@app.route("/explain", methods=["POST"])
def explain():
    data = request.json
    topic = data.get("topic", "")
    explanation = explain_topic(topic)
    return jsonify({"explanation": explanation})

@app.route("/deadlines", methods=["POST"])
def deadlines():
    data = request.json
    text = data.get("text", "")
    deadlines = extract_deadlines(text)
    return jsonify({"deadlines": deadlines})
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    message = data.get("message", "")
    summary = summarize_text(message)
    deadlines = extract_deadlines(message)

    return jsonify({
        "title": "Detected Task",
        "date": deadlines[0] if deadlines else "No date found",
        "summary": summary
    })
@app.route("/add-to-calendar", methods=["POST"])
def add_to_calendar():
    return jsonify({"status": "success", "message": "Added to calendar"})


if __name__ == "__main__":
    port=int(os.environ.get("PORT",10000))
    app.run(host='0.0.0.0',port=port)
