from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Registration')
def reg():
    return render_template('Registration.html')

@app.route('/Application')
def app():
    return render_template('Application.html')

@app.route('/Jobs')
def job():
    return render_template('Jobs.html')

# @app.route('/LogIn')
# def logout():
#     return render_template('LogIn.html')

if __name__ == '__main__':
    app.run(debug=True)