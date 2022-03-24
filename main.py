from flask import Flask, render_template, url_for

app = Flask("__main__")


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/quote")
def quote():
    return render_template('quote_home.html')


@app.route("/wizard/{%wizard_page_key%}")
def quote():
    return render_wizard_page(wizard_page_key)


if __name__ == '__main__':
    app.run(debug=True)



