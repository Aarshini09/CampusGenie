from flask import Flask, request, jsonify,  render_template
from ai_logic import summarize_text, explain_topic, extract_deadlines

app = Flask(__name__)
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

if __name__ == "__main__":
    app.run(debug=True)
