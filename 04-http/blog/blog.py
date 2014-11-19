from flask import Flask
app = Flask(__name__)

from data import entries


@app.route("/")
def home():
    html = ''
    for i, entry in enumerate(entries):
        html += '<a href="post/{0}"><h2>{1}</h2></a><p>{2}</p>'.format(
            i,
            entry['title'],
            entry['abstract']
        )
    return html


@app.route("/post/<post_id>")
def post(post_id):
    entry = entries[int(post_id)]
    html = '''
<h2>{0}</h2>
<h4>{1}</h4>
{2}
'''.format(entry['title'], entry['abstract'], entry['content'])
    return html


if __name__ == "__main__":
    app.run(debug=True)
