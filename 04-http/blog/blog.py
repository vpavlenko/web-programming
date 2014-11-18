from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return """
<a href="post/1">Post #1</a>
<a href="post/2">Post #2</a>
"""


@app.route("/post/<post_id>")
def post(post_id):
    return "Concrete post #" + post_id


if __name__ == "__main__":
    app.run(debug=True)
