from flask import Flask, render_template
app = Flask(__name__)

from data import entries


@app.route("/")
def home():
    return render_template('home.html', entries=entries)


@app.route("/post/<post_id>")
def post(post_id):
    entry = entries[int(post_id) - 1]
    return render_template('post.html', entry=entry)


if __name__ == "__main__":
    app.run(debug=True)
