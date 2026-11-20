from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")
@app.route('/about')
def about_page():
    return render_template("about.html")
@app.route('/another')
def another_page():
    return render_template("another.html")


@app.route('/forms_test')
def forms_test():
    return render_template("forms_test.html")

@app.route('/receive_form_data', methods=['POST'])
def receive_form_data():
    print(request.form)
    return "Apple"


if __name__ == "__main__":
    app.run()