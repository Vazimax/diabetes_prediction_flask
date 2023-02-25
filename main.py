from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def home(request):

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

