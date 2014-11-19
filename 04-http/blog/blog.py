from flask import Flask, render_template, redirect, request
app = Flask(__name__)

from data import entries


@app.route("/")
def home():
    return render_template('home.html', entries=entries)


@app.route("/post/<post_id>")
def post(post_id):
    entry = entries[int(post_id) - 1]
    return render_template('post.html', entry=entry)


@app.route("/new_post", methods=["POST"])
def new_post():
    title = request.form['title']
    abstract = request.form['abstract']
    content = request.form['content']
    entries.append({
        'title': title,
        'abstract': abstract,
        'content': content
    })
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
