import os

from flask import Flask, render_template, redirect, request
app = Flask(__name__)

from data import init_with_file, get_entries, add_entry


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def home():
    return render_template('home.html', entries=get_entries())


@app.route("/posts/<int:post_id>")
def post(post_id):
    entry = get_entries()[post_id - 1]
    return render_template('post.html', entry=entry)


@app.route("/new_post", methods=["POST"])
def new_post():
    title = request.form['title']
    abstract = request.form['abstract']
    content = request.form['content']
    add_entry({
        'title': title,
        'abstract': abstract,
        'content': content
    })
    return redirect('/')


if __name__ == "__main__":
    init_with_file(os.path.join(SCRIPT_DIR, 'data.txt'))
    app.run(debug=True)
