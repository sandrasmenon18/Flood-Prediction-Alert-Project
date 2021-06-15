from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__,template_folder='template')

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    import requests,bs4
    res=requests.get("https://www.worldweatheronline.com/nileshwar-weather/kerala/in.aspx")
    soup=bs4.BeautifulSoup(res.text,'lxml')
    para=soup.select('p')
    print(para[4].getText())
    lis=para[4].getText().split()
    print(lis)
    rain=float(lis[1])
    return render_template("index.html",r=rain)


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    print(int_features)
    import requests,bs4
    res=requests.get("https://www.worldweatheronline.com/nileshwar-weather/kerala/in.aspx")
    soup=bs4.BeautifulSoup(res.text,'lxml')
    para=soup.select('p')
    print(para[4].getText())
    lis=para[4].getText().split()
    print(lis)
    rain=float(lis[1])
    int_features[0]=rain
    # rese=requests.get("https://indiawris.gov.in/wris/#/evapotranspiration",verify=False)
    # print(rese.text)
    # # soup=bs4.BeautifulSoup(rese.text,'lxml')
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
    # output=float(output)
    print(type(output))
    if output>=str(4501):
        return render_template('flood_pred.html',pred='Your region is in Danger',sel="alert",r=rain)
    elif output>=str(0) and output<=str(2500):
        return render_template('flood_pred.html',pred='Your region is Safe',sel="alert1",r=rain)
    elif output>=str(2501) and output<=str(3500):
        return render_template('flood_pred.html',pred='Your region is in Slight Danger.Watch and Be updated!!!',sel="alert2",r=rain)
    elif output>=str(3501) and output<=str(4500):
        return render_template('flood_pred.html',pred='Be Prepared!!Your region is at risk.',sel="alert3",r=rain)


if __name__ == '__main__':
    app.run(debug=True)
