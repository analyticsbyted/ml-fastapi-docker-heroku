from flask import Flask, request, render_template
from model.model import predict_pipeline, __version__ as model_version

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        language = predict_pipeline(text)
        return render_template("result.html", user_input=text, predicted_language=language)
    return render_template("index.html", health_check="OK", model_version=model_version)

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(host="localhost", port=8000)

# Run the app

