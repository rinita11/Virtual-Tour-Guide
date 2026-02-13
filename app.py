from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/explore', methods=["POST"])
def explore():
    location = request.form["location"]
    return render_template("explore.html", location=location)

@app.route('/custom_direction', methods=["POST"])
def custom_direction():
    source = request.form["source"]
    destination = request.form["destination"]

    url = f"https://www.google.com/maps/dir/?api=1&origin={source}&destination={destination}"
    return redirect(url)

if __name__ == "__main__":
    app.run(debug=True)
