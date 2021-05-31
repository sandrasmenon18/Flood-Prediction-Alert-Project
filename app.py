from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__,template_folder='template')

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("forest.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)
    print(prediction)
    output='{0:.{1}f}'.format(prediction[0],4)

    if output>str(0.5):
        return render_template('forest_fire.html',pred='Your region is in Danger.\nDischarge rate is {}'.format(output),sel="alert")
    else:
        return render_template('forest_fire.html',pred='Your region is safe.\n Discharge rate is {}'.format(output),sel="alert1")


if __name__ == '__main__':
    app.run(debug=True)
