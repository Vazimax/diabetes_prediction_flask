from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('home.html')

model = pickle.load(open('model.pkl','rb'))
@app.route('/predict',methods=['POST','GET'])
def predict():
    pregnancies = float(request.form.get('p'))
    glucose = float(request.form.get('g'))
    blood_pressure = float(request.form.get('b'))
    skin = float(request.form.get('s'))
    insulin = float(request.form.get('i'))
    bmi = float(request.form.get('bm'))
    dpf = float(request.form.get('d'))
    age = float(request.form.get('a'))
    prediction = model.predict([[pregnancies,glucose,blood_pressure,skin,insulin,bmi,dpf,age]])

    return render_template('home.html',text=f"{prediction}")


if __name__ == '__main__':
    app.run(debug=True)

