from flask import Flask, render_template, redirect, request
app = Flask(__name__)

from data import get_entries, add_entry


@app.route("/")
def home():
    return render_template('home.html', entries=get_entries())


@app.route("/vse-posty/<int:post_id>")
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
    app.run(debug=True)
