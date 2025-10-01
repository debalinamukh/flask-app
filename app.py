from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello MSOE"

if __name__ == "__main__":
    # run the dev server on port 8080 so it matches your screenshot
    app.run(host="0.0.0.0", port=8080, debug=True)
