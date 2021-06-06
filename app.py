from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__,template_folder='template')

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    print(int_features)
    # import requests,bs4
    # res=requests.get("https://www.worldweatheronline.com/nileshwar-weather/kerala/in.aspx")
    # soup=bs4.BeautifulSoup(res.text,'lxml')
    # para=soup.select('p')
    # print(para[4].getText())
    # lis=para[4].getText().split()
    # print(lis)
    # rain=float(lis[1])
    # int_features[0]=rain
    final=[np.array(int_features)]
    print(final)
    prediction=model.predict(final)
    print(prediction)
    output='{0:.{1}f}'.format(prediction[0],4)
    output=float(output)
    print(type(output))
    if output>=4501:
        return render_template('flood_pred.html',pred='Your region is in Danger.\nDischarge rate is {}'.format(output),sel="alert")
    elif output>=0 and output<=2500:
        return render_template('flood_pred.html',pred='Your region is Safe.\nDischarge rate is {}'.format(output),sel="alert1")
    elif output>=2501 and output<=3500:
        return render_template('flood_pred.html',pred='Your region is in Slight Danger.Watch and Be updated!!!\nDischarge rate is {}'.format(output),sel="alert2")
    elif output>=3501 and output<=4500:
        return render_template('flood_pred.html',pred='Be Prepared!!Your region is at risk.\n Discharge rate is {}'.format(output),sel="alert3")


if __name__ == '__main__':
    app.run(debug=True)
