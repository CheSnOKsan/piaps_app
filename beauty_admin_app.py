from flask import Flask, render_template


app = Flask(__name__)


# декораторы

@app.route('/')
@app.route('/autorization_page')
def autorization_page():
    return render_template("index.html")


# на будущее
@app.route('/client/<int:cl_id>')
def client(cl_id):
    return f'CLient page - {cl_id}'


if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host = '0.0.0.0', port = 8080)
    app.run(debug=True)