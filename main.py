from flask import Flask, render_template, url_for
from wizard import Wizard

wiz = Wizard()
app = Flask("__main__")


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/quote")
def quote():
    return wiz.render_page("select-floor")


@app.route("/wizard/<page_key>", methods=["GET", "POST"])
def go_wizard(page_key):
    return wiz.render_page(page_key)


if __name__ == '__main__':
    app.run(debug=True)



