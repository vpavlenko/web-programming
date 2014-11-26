import os

from flask import Flask, make_response, redirect, render_template, request, url_for
app = Flask(__name__)

from data import init_with_file, get_entries, add_entry


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def home():
    return render_template(
        'home.html',
        entries=get_entries(),
        login=request.cookies.get('login', None))


@app.route("/posts/<int:post_id>")
def post(post_id):
    entry = get_entries()[post_id - 1]
    return render_template('post.html', entry=entry, login=request.cookies.get('login', None))


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
    return redirect(url_for('home'))


@app.route("/signup", methods=["POST"])
def signup():
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('login', request.form['login'])
    return resp


if __name__ == "__main__":
    init_with_file(os.path.join(SCRIPT_DIR, 'data.txt'))
    app.run(debug=True)
