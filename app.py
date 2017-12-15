#######Imports
from flask import Flask, render_template, request
import logging
from logging import Formatter, FileHandler
import urllib.request
import json
import pickle
from sklearn.externals import joblib
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARIMAResults
from forms import *
import os

#######Config
app = Flask(__name__)
app.config.from_object('config')


#######Controllers
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/forecast', methods=['GET','POST'])
def forecast():
    form = Forecast(request.form)
    return render_template('forecast.html', form=form)

#######API Calls
def cluster0(itemclass, onpromotion, transactions, oil, day, month, state):
    # set the one hots
    x1002,x1006,x1030,x1035,x1050,x1052,x1062=0,0,0,0,0,0,0
    x1064,x1068,x1075,x1079,x1082,x1087=0,0,0,0,0,0
    day_0,day_1,day_2,day_3,day_4,day_5=0,0,0,0,0,0
    month_1,month_2,month_3,month_7,month_8,month_10=0,0,0,0,0,0
    Azuay,Bolivar,Chimborazo,Cotopaxi,ElOro=0,0,0,0,0
    Esmeraldas,Guayas,Loja,LosRios,Manabi,SantaElena=0,0,0,0,0,0
    if(itemclass==1002):
        x1002=1
    elif(itemclass==1006):
        x1006=1
    elif(itemclass==1030):
        x1030=1
    elif(itemclass==1035):
        x1035=1
    elif(itemclass==1050):
        x1050=1
    elif(itemclass==1052):
        x1052=1
    elif(itemclass==1062):
        x1062=1
    elif(itemclass==1064):
        x1064=1
    elif(itemclass==1068):
        x1068=1
    elif(itemclass==1075):
        x1075=1
    elif(itemclass==1079):
        x1079=1
    elif(itemclass==1082):
        x1082=1
    elif(itemclass==1087):
        x1087=1
    if(day==0):
        day_0 = 1
    elif(day==1):
        day_1 = 1
    elif(day==2):
        day_2 = 1
    elif(day==3):
        day_3 = 1
    elif(day==4):
        day_4 = 1
    elif(day==5):
        day_5 = 1
    if(month==1):
        month_1=1
    elif(month==2):
        month_2=1
    elif(month==3):
        month_3=1
    elif(month==7):
        month_7=1
    elif(month==8):
        month_8=1
    elif(month==10):
        month_10=1
    if(state=='Azuay'):
        Azuay=1
    elif(state=='Bolivar'):
        Bolivar=1
    elif(state=='Chimborazo'):
        Chimborazo=1
    elif(state=='Cotopaxi'):
        Cotopaxi=1
    elif(state=='El Oro'):
        ElOro=1
    elif(state=='Esmeraldas'):
        Esmeraldas=1
    elif(state=='Guayas'):
        Guayas=1
    elif(state=='Loja'):
        Loja=1
    elif(state=='Los Rios'):
        LosRios=1
    elif(state=='Manabi'):
        Manabi=1
    elif(state=='Santa Elena'):
        SantaElena=1
    data = {
        "Inputs": {"input1":[{
                 '1002': x1002,
                 '1006': x1006,
                 '1030': x1030,
                 '1035': x1035,
                 '1050': x1050,
                 '1052': x1052,
                 '1062': x1062,
                 '1064': x1064,
                 '1068': x1068,
                 '1075': x1075,
                 '1079': x1079,
                 '1082': x1082,
                 '1087': x1087,
                 'unit_sales': "1",
                 'onpromotion': onpromotion,
                 'transactions': transactions,
                 'dcoilwtico': oil,
                 'day_0': day_0,
                 'day_1': day_1,
                 'day_2': day_2,
                 'day_3': day_3,
                 'day_4': day_4,
                 'day_5': day_5,
                 'month_1': month_1,
                 'month_2': month_2,
                 'month_3': month_3,
                 'month_7': month_7,
                 'month_8': month_8,
                 'month_10': month_10,
                 'Azuay': Azuay,
                 'Bolivar': Bolivar,
                 'Chimborazo': Chimborazo,
                 'Cotopaxi': Cotopaxi,
                 'El Oro': ElOro,
                 'Esmeraldas': Esmeraldas,
                 'Guayas': Guayas,
                 'Loja': Loja,
                 'Los Rios': LosRios,
                 'Manabi': Manabi,
                 'Santa Elena': SantaElena,
                 }],},
        "GlobalParameters":  {}
    }
    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/c27f2b7f3bf84107b15d822b6d7c9fb6/services/81a30562875d4c89a854ea6229d14f15/execute?api-version=2.0&format=swagger'

    api_key = 'AU6spG0D++i+MzTlIFkqm12LR02RsqWu/QptSqpHJNaydwFxmgHiD1L2gZoObI8RYcedug+d16xGWoA+r7j3Ig==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        return result['Results']['output1'][0]['Scored Label']
    except urllib.error.HTTPError as error:
        return "The request failed with status code: " + str(error.code)

def cluster1(itemclass, onpromotion, transactions, oil, day, month, state, holiday):
    x1010,x1012,x1042,x1060,x1066,x1070,x1077=0,0,0,0,0,0,0
    day_0,day_1,day_2,day_3,day_4,day_5=0,0,0,0,0,0
    month_3,month_4,month_11=0,0,0
    Azuay,Bolivar,Chimborazo,Cotopaxi,ElOro=0,0,0,0,0
    Esmeraldas,Guayas,Imbabura,Loja,LosRios=0,0,0,0,0
    Manabi,Pastaza,Pichincha,SantaElena,SantoDomingo=0,0,0,0,0
    regionalholiday,nationalother,nholidayspike=0,0,0
    earthquakespike,earthquakespike=0,0
    if(itemclass==1010):
        x1010=1
    elif(itemclass==1012):
        x1012=1
    elif(itemclass==1042):
        x1042=1
    elif(itemclass==1060):
        x1060=1
    elif(itemclass==1066):
        x1066=1
    elif(itemclass==1070):
        x1070=1
    elif(itemclass==1077):
        x1077=1
    if(day==0):
        day_0 = 1
    elif(day==1):
        day_1 = 1
    elif(day==2):
        day_2 = 1
    elif(day==3):
        day_3 = 1
    elif(day==4):
        day_4 = 1
    elif(day==5):
        day_5 = 1
    if(month==3):
        month_3=1
    elif(month==4):
        month_4=1
    elif(month==11):
        month_11=1
    if(state=='Azuay'):
        Azuay=1
    elif(state=='Bolivar'):
        Bolivar=1
    elif(state=='Chimborazo'):
        Chimborazo=1
    elif(state=='Cotopaxi'):
        Cotopaxi=1
    elif(state=='El Oro'):
        ElOro=1
    elif(state=='Esmeraldas'):
        Esmeraldas=1
    elif(state=='Guayas'):
        Guayas=1
    elif(state=='Imbabura'):
        Imbabura=1
    elif(state=='Loja'):
        Loja=1
    elif(state=='Los Rios'):
        LosRios=1
    elif(state=='Manabi'):
        Manabi=1
    elif(state=='Pastaza'):
        Pastaza=1
    elif(state=='Pichincha'):
        Pichincha=1
    elif(state=='Santa Elena'):
        SantaElena=1
    elif(state=='Santo Domingo de los Tsachilas'):
        SantoDomingo=1
    if(holiday=='Regional'):
        regionalholiday=1
    list = ['Additional','Bridge','Transfer','Work Day']
    if(holiday in list):
        nationalother=1
    list2=['Dia de Difuntos','Dia del Trabajo','Independencia de Cuenca','Primer dia del ano']
    if(holiday in list2):
        nholidayspike=1
    list3=['Terremoto Manabi+1','Terremoto Manabi+2','Terremoto Manabi+3','Terremoto Manabi+4','Terremoto Manabi+8','Terremoto Manabi+14','Terremoto Manabi+15']
    if(holiday in list3):
        earthquakespike=1
    list4=['Terremoto Manabi+9','Terremoto Manabi+10','Terremoto Manabi+11','Terremoto Manabi+12','Terremoto Manabi+13']
    if(holiday in list4):
        earthquakedrop=1

    data = {
        "Inputs": {
            "input1":[{
                      '1010': x1010,
                      '1012': x1012,
                      '1042': x1042,
                      '1060': x1060,
                      '1066': x1066,
                      '1070': x1070,
                      '1077': x1077,
                      'unit_sales': "1",
                      'onpromotion': onpromotion,
                      'transactions': transactions,
                      'dcoilwtico': oil,
                      'day_0': day_0,
                      'day_1': day_1,
                      'day_2': day_2,
                      'day_3': day_3,
                      'day_4': day_4,
                      'day_5': day_5,
                      'month_3': month_3,
                      'month_4': month_4,
                      'month_11': month_11,
                      'Azuay': Azuay,
                      'Bolivar': Bolivar,
                      'Chimborazo': Chimborazo,
                      'Cotopaxi': Cotopaxi,
                      'El Oro': ElOro,
                      'Esmeraldas': Esmeraldas,
                      'Guayas': Guayas,
                      'Imbabura': Imbabura,
                      'Loja': Loja,
                      'Los Rios': LosRios,
                      'Manabi': Manabi,
                      'Pastaza': Pastaza,
                      'Pichincha': Pichincha,
                      'Santa Elena': SantaElena,
                      'Santo Domingo de los Tsachilas': SantoDomingo,
                      'regionalholiday': regionalholiday,
                      'nationalother': nationalother,
                      'nholidayspike': nholidayspike,
                      'earthquakespike': earthquakespike,
                      'earthquakedrop': earthquakedrop,
                      }],},

            "GlobalParameters":  { }
    }
    body = str.encode(json.dumps(data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/c27f2b7f3bf84107b15d822b6d7c9fb6/services/d2acabe823f64288bc21b86b8fd3ba29/execute?api-version=2.0&format=swagger'
    api_key = 'ye/nishLl4GhLoxHq2x/TuKRbjZeEMlN81qgEiFelS832OHNLRPxemRa61NLqXpUJTk1FzqhZrigSIN591gtJg=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        return result['Results']['output1'][0]['Scored Label']
    except urllib.error.HTTPError as error:
        return "The request failed with status code: " + str(error.code)

def cluster2(onpromotion, transactions, oil, day, month, state, holiday):
    day_0,day_1,day_2,day_3,day_4=0,0,0,0,0
    month_1,month_2,month_3,month_4,month_7,month_8,month_9,month_10=0,0,0,0,0,0,0,0
    Azuay,Bolivar,Chimborazo,Cotopaxi,ElOro,Esmeraldas=0,0,0,0,0,0
    Guayas,Imbabura,Loja,LosRios,Manabi,Pastaza=0,0,0,0,0,0
    Pichincha,SantaElena,SantoDomingo=0,0,0
    localholiday,regionalholiday,nationalother,nholidayspike,goodfriday=0,0,0,0,0
    earthquakespike,earthquakedrop=0,0
    if(day==0):
        day_0 = 1
    elif(day==1):
        day_1 = 1
    elif(day==2):
        day_2 = 1
    elif(day==3):
        day_3 = 1
    elif(day==4):
        day_4 = 1
    if(month==1):
        month_1=1
    elif(month==2):
        month_2=1
    elif(month==3):
        month_3=1
    elif(month==4):
        month_4=1
    elif(month==7):
        month_7=1
    elif(month==8):
        month_8=1
    elif(month==9):
        month_9=1
    elif(month==10):
        month_10=1
    if(state=='Azuay'):
        Azuay=1
    elif(state=='Bolivar'):
        Bolivar=1
    elif(state=='Chimborazo'):
        Chimborazo=1
    elif(state=='Cotopaxi'):
        Cotopaxi=1
    elif(state=='El Oro'):
        ElOro=1
    elif(state=='Esmeraldas'):
        Esmeraldas=1
    elif(state=='Guayas'):
        Guayas=1
    elif(state=='Imbabura'):
        Imbabura=1
    elif(state=='Loja'):
        Loja=1
    elif(state=='Los Rios'):
        LosRios=1
    elif(state=='Manabi'):
        Manabi=1
    elif(state=='Pastaza'):
        Pastaza=1
    elif(state=='Pichincha'):
        Pichincha=1
    elif(state=='Santa Elena'):
        SantaElena=1
    elif(state=='Santo Domingo de los Tsachilas'):
        SantoDomingo=1
    if(holiday=='Local'):
        localholiday=1
    if(holiday=='Regional'):
        regionalholiday=1
    list = ['Additional','Bridge','Transfer','Work Day']
    if(holiday in list):
        nationalother=1
    list2=['Dia de Difuntos','Dia del Trabajo','Independencia de Cuenca','Primer dia del ano']
    if(holiday in list2):
        nholidayspike=1
    if(holiday=='Viernes Santo'):
        goodfriday=1
    list3=['Terremoto Manabi+1','Terremoto Manabi+2','Terremoto Manabi+3','Terremoto Manabi+4','Terremoto Manabi+8','Terremoto Manabi+14','Terremoto Manabi+15']
    if(holiday in list3):
        earthquakespike=1
    list4=['Terremoto Manabi+9','Terremoto Manabi+10','Terremoto Manabi+11','Terremoto Manabi+12','Terremoto Manabi+13']
    if(holiday in list4):
        earthquakedrop=1
    data = {
        "Inputs": {
            "input1":[{
                      'unit_sales': "1",
                      'onpromotion': onpromotion,
                      'transactions': transactions,
                      'dcoilwtico': oil,
                      'day_0': day_0,
                      'day_1': day_1,
                      'day_2': day_2,
                      'day_3': day_3,
                      'day_4': day_4,
                      'month_1': month_1,
                      'month_2': month_2,
                      'month_3': month_3,
                      'month_4': month_4,
                      'month_7': month_7,
                      'month_8': month_8,
                      'month_9': month_9,
                      'month_10': month_10,
                      'Azuay': Azuay,
                      'Bolivar': Bolivar,
                      'Chimborazo': Chimborazo,
                      'Cotopaxi': Cotopaxi,
                      'El Oro': ElOro,
                      'Esmeraldas': Esmeraldas,
                      'Guayas': Guayas,
                      'Imbabura': Imbabura,
                      'Loja': Loja,
                      'Los Rios': LosRios,
                      'Manabi': Manabi,
                      'Pastaza': Pastaza,
                      'Pichincha': Pichincha,
                      'Santa Elena': SantaElena,
                      'Santo Domingo de los Tsachilas': SantoDomingo,
                      'localholiday': localholiday,
                      'regionalholiday': regionalholiday,
                      'nationalother': nationalother,
                      'nholidayspike': nholidayspike,
                      'goodfriday': goodfriday,
                      'earthquakespike': earthquakespike,
                      'earthquakedrop': earthquakedrop,
                      }],},
        "GlobalParameters":  { }
    }
    body = str.encode(json.dumps(data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/c27f2b7f3bf84107b15d822b6d7c9fb6/services/6a861b74875f47119352b7ed31850bcd/execute?api-version=2.0&format=swagger'
    api_key = 'sndlp+UwgMZSTBV9U5kalFUCm/iFEU6bUWc98e2KWAkLaWE+ooYHmgU5cjcvffUFitHpiMGG91dZcK4OPSStHg=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        return result['Results']['output1'][0]['Scored Label']
    except urllib.error.HTTPError as error:
        return "The request failed with status code: " + str(error.code)

#def cluster3():
#def cluster4():

def cluster5(itemclass, transactions, oil, day, month, state, holiday):
    x1018,x1029,x1033,x1041 = 0,0,0,0
    day_4,day_5=0,0
    month_7=0
    Pichincha,SantoDomingo=0,0
    nationalother,nholidayspike,worldcupdrop=0,0,0
    if(itemclass==1018):
        x1018=1
    elif(itemclass==1029):
        x1029=1
    elif(itemclass==1033):
        x1033=1
    elif(itemclass==1041):
        x1041=1
    if(day==4):
        day_4=1
    elif(day==5):
        day_5=1
    if(month==7):
        month_7=1
    if(state=='Pichincha'):
        Pichincha=1
    elif(state=='Santo Domingo de los Tsachilas'):
        SantoDomingo=1
    list = ['Additional','Bridge','Transfer','Work Day']
    if(holiday in list):
        nationalother=1
    list2=['Dia de Difuntos','Dia del Trabajo','Independencia de Cuenca','Primer dia del ano']
    if(holiday in list2):
        nholidayspike=1
    list3=['Inauguracion Mundial de futbol Brasil','Mundial de futbol Brasil: Ecuador-Francia','Mundial de futbol Brasil: Ecuador-Honduras']
    if(holiday in list3):
        worldcupdrop=1
    data = {
        "Inputs": {
            "input1":[{
                      '1018': x1018,
                      '1029': x1029,
                      '1033': x1033,
                      '1041': x1041,
                      'unit_sales': "1",
                      'transactions': transactions,
                      'dcoilwtico': oil,
                      'day_4': day_4,
                      'day_5': day_5,
                      'month_7': month_7,
                      'Pichincha': Pichincha,
                      'Santo Domingo de los Tsachilas': SantoDomingo,
                      'nationalother': nationalother,
                      'nholidayspike': nholidayspike,
                      'worldcupdrop': worldcupdrop,
                      }],},
        
        "GlobalParameters":  { }
    }
    body = str.encode(json.dumps(data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/c27f2b7f3bf84107b15d822b6d7c9fb6/services/a62e41f387914f78ada498df34bf5f4b/execute?api-version=2.0&format=swagger'
    api_key = 'pbCdeb/iBtPyz+eWm5I/tXTstb9KoN4kT7JUtir2WQC+4l36K8UCEAwthZCfOyO0NsztXBjfPUyFHm2O9e+PIQ=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        return result['Results']['output1'][0]['Scored Label']
    except urllib.error.HTTPError as error:
        return "The request failed with status code: " + str(error.code)

#def cluster6():

def cluster7(onpromotion, transactions, oil, day, month, state, holiday):
    day_0,day_3,day_5=0,0,0
    month_3,month_5,month_6,month_8,month_9,month_10=0,0,0,0,0,0
    Azuay,Bolivar,Chimborazo,Cotopaxi,ElOro,Esmeraldas=0,0,0,0,0,0
    Guayas,Imbabura,LosRios,Manabi,Pastaza,Pichincha=0,0,0,0,0,0
    SantaElena,SantoDomingo=0,0
    nholidayspike,blackfriday=0,0
    if(day==0):
        day_0 = 1
    elif(day==3):
        day_3 = 1
    elif(day==5):
        day_5 = 1
    if(month==3):
        month_3=1
    elif(month==5):
        month_5=1
    elif(month==6):
        month_5=1
    elif(month==8):
        month_5=1
    elif(month==9):
        month_5=1
    elif(month==10):
        month_5=1
    elif(state=='Azuay'):
        Azuay=1
    elif(state=='Bolivar'):
        Bolivar=1
    elif(state=='Cotopaxi'):
        Cotopaxi=1
    elif(state=='Chimborazo'):
        Chimborazo=1
    elif(state=='El Oro'):
        ElOro=1
    elif(state=='Esmeraldas'):
        Esmeraldas=1
    elif(state=='Guayas'):
        Guayas=1
    elif(state=='Imbabura'):
        Imbabura=1
    elif(state=='Los Rios'):
        LosRios=1
    elif(state=='Manabi'):
        Manabi=1
    elif(state=='Pastaza'):
        Pastaza=1
    elif(state=='Pichincha'):
        Pichincha=1
    elif(state=='Santa Elena'):
        SantaElena=1
    elif(state=='Santo Domingo de los Tsachilas'):
        SantoDomingo=1
    list2=['Dia de Difuntos','Dia del Trabajo','Independencia de Cuenca','Primer dia del ano']
    if(holiday in list2):
        nholidayspike=1
    if(holiday=='Black Friday'):
       blackfriday=1
    data = {
       "Inputs": {
       "input1": [{
                  'unit_sales': "1",
                  'onpromotion': onpromotion,
                  'transactions': transactions,
                  'dcoilwtico': oil,
                  'day_0': day_0,
                  'day_3': day_3,
                  'day_5': day_5,
                  'month_3': month_3,
                  'month_5': month_5,
                  'month_6': month_6,
                  'month_8': month_8,
                  'month_9': month_9,
                  'month_10': month_10,
                  'Azuay': Azuay,
                  'Bolivar': Bolivar,
                  'Chimborazo': Chimborazo,
                  'Cotopaxi': Cotopaxi,
                  'El Oro': ElOro,
                  'Esmeraldas': Esmeraldas,
                  'Guayas': Guayas,
                  'Imbabura': Imbabura,
                  'Los Rios': LosRios,
                  'Manabi': Manabi,
                  'Pastaza': Pastaza,
                  'Pichincha': Pichincha,
                  'Santa Elena': SantaElena,
                  'Santo Domingo de los Tsachilas': SantoDomingo,
                  'nholidayspike': nholidayspike,
                  'blackfriday': blackfriday,
                  }],},
        "GlobalParameters":  { }
       
       }
    body = str.encode(json.dumps(data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/c27f2b7f3bf84107b15d822b6d7c9fb6/services/67e478ab155c4ec1ac58d9b836f74cbc/execute?api-version=2.0&format=swagger'
    api_key = 'SkNSMnZMVt3K24oB+FC7Dvb+s8D6yfABzOqqdmEQ8BrdMKPRADpAq95l3h/MTtdherqGWhNFcv3IpfF7cURkVw=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    try:
       response = urllib.request.urlopen(req)
       result = response.read()
       return result['Results']['output1'][0]['Scored Label']
    except urllib.error.HTTPError as error:
       return "The request failed with status code: " + str(error.code)

def cluster8(itemclass, onpromotion, transactions, oil, day, month, state, holiday):
    x1013,x1072=0,0
    day_0,day_1,day_2,day_3,day_4,day_5=0,0,0,0,0,0
    month_1,month_2,month_3,month_4,month_5=0,0,0,0,0
    month_6,month_7,month_8,month_9,month_10,month_11=0,0,0,0,0,0
    ElOro,Esmeraldas,Guayas,Imbabura,LosRios=0,0,0,0,0
    Manabi,Pichincha,SantaElena,SantoDomingo=0,0,0,0
    nationalother,nholidayspike,goodfriday=0,0,0
    worldcupspike,worldcupdrop,earthquakespike,earthquakedrop=0,0,0,0
    if(itemclass==1013):
        x1013=1
    elif(itemclass==1072):
        x1072=1
    if(day==0):
        day_0 = 1
    elif(day==1):
        day_1 = 1
    elif(day==2):
        day_2 = 1
    elif(day==3):
        day_3 = 1
    elif(day==4):
        day_4 = 1
    elif(day==5):
        day_5 = 1
    if(month==1):
        month_1=1
    elif(month==2):
        month_2=1
    elif(month==3):
        month_3=1
    elif(month==4):
        month_4=1
    elif(month==5):
        month_5=1
    elif(month==6):
        month_5=1
    elif(month==7):
        month_5=1
    elif(month==8):
        month_5=1
    elif(month==9):
        month_5=1
    elif(month==10):
        month_5=1
    elif(month==11):
        month_5=1
    if(state=='El Oro'):
        ElOro=1
    elif(state=='Esmeraldas'):
        Esmeraldas=1
    elif(state=='Guayas'):
        Guayas=1
    elif(state=='Imbabura'):
        Imbabura=1
    elif(state=='Los Rios'):
        LosRios=1
    elif(state=='Manabi'):
        Manabi=1
    elif(state=='Pichincha'):
        Pichincha=1
    elif(state=='Santa Elena'):
        SantaElena=1
    elif(state=='Santo Domingo de los Tsachilas'):
        SantoDomingo=1
    list = ['Additional','Bridge','Transfer','Work Day']
    if(holiday in list):
        nationalother=1
    list2=['Dia de Difuntos','Dia del Trabajo','Independencia de Cuenca','Primer dia del ano']
    if(holiday in list2):
        nholidayspike=1
    if(holiday=='Viernes Santo'):
        goodfriday=1
    list3=['Terremoto Manabi+1','Terremoto Manabi+2','Terremoto Manabi+3','Terremoto Manabi+4','Terremoto Manabi+8','Terremoto Manabi+14','Terremoto Manabi+15']
    if(holiday in list3):
        earthquakespike=1
    list4=['Terremoto Manabi+9','Terremoto Manabi+10','Terremoto Manabi+11','Terremoto Manabi+12','Terremoto Manabi+13']
    if(holiday in list4):
        earthquakedrop=1
    list5=['Mundial de futbol Brasil: Cuartos de Final','Mundial de futbol Brasil: Ecuador-Suiza','Mundial de futbol Brasil: Final','Mundial de futbol Brasil: Octavos de Final','Mundial de futbol Brasil: Tercer y cuarto lugar']
    if(holiday in list5):
        worldcupspike=1
    list6=['Inauguracion Mundial de futbol Brasil','Mundial de futbol Brasil: Ecuador-Francia','Mundial de futbol Brasil: Ecuador-Honduras']
    if(holiday in list6):
        worldcupdrop=1

    data = {
        "Inputs": {
            "input1": [{
                       '1013': x1013,
                       '1072': x1072,
                       'unit_sales': "1",
                       'onpromotion': onpromotion,
                       'transactions': transactions,
                       'dcoilwtico': oil,
                       'day_0': day_0,
                       'day_1': day_1,
                       'day_2': day_2,
                       'day_3': day_3,
                       'day_4': day_4,
                       'day_5': day_5,
                       'month_1': month_1,
                       'month_2': month_2,
                       'month_3': month_3,
                       'month_4': month_4,
                       'month_5': month_5,
                       'month_6': month_6,
                       'month_7': month_7,
                       'month_8': month_8,
                       'month_9': month_9,
                       'month_10': month_10,
                       'month_11': month_11,
                       'El Oro': ElOro,
                       'Esmeraldas': Esmeraldas,
                       'Guayas': Guayas,
                       'Imbabura': Imbabura,
                       'Los Rios': LosRios,
                       'Manabi': Manabi,
                       'Pichincha': Pichincha,
                       'Santa Elena': SantaElena,
                       'Santo Domingo de los Tsachilas': SantoDomingo,
                       'nationalother': nationalother,
                       'nholidayspike': nholidayspike,
                       'goodfriday': goodfriday,
                       'worldcupspike': worldcupspike,
                       'worldcupdrop': worldcupdrop,
                       'earthquakespike': earthquakespike,
                       'earthquakedrop': earthquakedrop,
                       }],},
        "GlobalParameters":  { }
    }
    body = str.encode(json.dumps(data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/c27f2b7f3bf84107b15d822b6d7c9fb6/services/5a5c4f698f304729a5e5768c6cd2549d/execute?api-version=2.0&format=swagger'

    api_key = 'uoJEkYSzbJiaym7jHzprUEqcgkh0Hc+ivRG2Uc1DporZNNc5xaE211tvCH398C22il7wzECP2v8Av3hIWs2i/Q=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        return result['Results']['output1'][0]['Scored Label']
    except urllib.error.HTTPError as error:
        return "The request failed with status code: " + str(error.code)

def cluster9(onpromotion, transactions, oil, day, month, state, holiday):
    day_0,day_1,day_2,day_3,day_4 =0,0,0,0,0
    month_1,month_2,month_3,month_4=0,0,0,0
    month_5,month_7,month_10=0,0,0
    Azuay,Bolivar,Chimborazo,Cotopaxi,ElOro=0,0,0,0,0
    Esmeraldas,Guayas,Imbabura,LosRios,Manabi=0,0,0,0,0
    Pastaza,Pichincha,SantaElena,SantoDomingo=0,0,0,0
    nationalother,nholidayspike,earthquakespike=0,0,0
    if(day==0):
        day_0 = 1
    elif(day==1):
        day_1 = 1
    elif(day==2):
        day_2 = 1
    elif(day==3):
        day_3 = 1
    elif(day==4):
        day_4 = 1
    if(month==1):
        month_1=1
    elif(month==2):
        month_2=1
    elif(month==3):
        month_3=1
    elif(month==4):
        month_4=1
    if(state=='Azuay'):
        Azuay=1
    elif(state=='Bolivar'):
        Bolivar=1
    elif(state=='Chimborazo'):
        Chimborazo=1
    elif(state=='Cotopaxi'):
        Cotopaxi=1
    elif(state=='El Oro'):
        ElOro=1
    elif(state=='Esmeraldas'):
        Esmeraldas=1
    elif(state=='Guayas'):
        Guayas=1
    elif(state=='Imbabura'):
        Imbabura=1
    elif(state=='Los Rios'):
        LosRios=1
    elif(state=='Manabi'):
        Manabi=1
    elif(state=='Pastaza'):
        Pastaza=1
    elif(state=='Pichincha'):
        Pichincha=1
    elif(state=='Santa Elena'):
        SantaElena=1
    elif(state=='Santo Domingo de los Tsachilas'):
        SantoDomingo=1
    list = ['Additional','Bridge','Transfer','Work Day']
    if(holiday in list):
        nationalother=1
    list2=['Dia de Difuntos','Dia del Trabajo','Independencia de Cuenca','Primer dia del ano']
    if(holiday in list2):
        nholidayspike=1
    list3=['Terremoto Manabi+1','Terremoto Manabi+2','Terremoto Manabi+3','Terremoto Manabi+4','Terremoto Manabi+8','Terremoto Manabi+14','Terremoto Manabi+15']
    if(holiday in list3):
        earthquakespike=1
    data = {
    "Inputs": {
        "input1": [{
                   'unit_sales': "1",
                   'onpromotion': onpromotion,
                   'transactions': transactions,
                   'dcoilwtico': oil,
                   'day_0': day_0,
                   'day_1': day_1,
                   'day_2': day_2,
                   'day_3': day_3,
                   'day_4': day_4,
                   'month_1': month_1,
                   'month_2': month_2,
                   'month_3': month_3,
                   'month_4': month_4,
                   'month_5': month_5,
                   'month_7': month_7,
                   'month_10': month_10,
                   'Azuay': Azuay,
                   'Bolivar': Bolivar,
                   'Chimborazo': Chimborazo,
                   'Cotopaxi': Cotopaxi,
                   'El Oro': ElOro,
                   'Esmeraldas': Esmeraldas,
                   'Guayas': Guayas,
                   'Imbabura': Imbabura,
                   'Los Rios': LosRios,
                   'Manabi': Manabi,
                   'Pastaza': Pastaza,
                   'Pichincha': Pichincha,
                   'Santa Elena': SantaElena,
                   'Santo Domingo de los Tsachilas': SantoDomingo,
                   'nationalother': nationalother,
                   'nholidayspike': nholidayspike,
                   'earthquakespike': earthquakespike,
                   }],},
        "GlobalParameters":  { }
    }
    body = str.encode(json.dumps(data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/c27f2b7f3bf84107b15d822b6d7c9fb6/services/9f37f2a24cea4d2e8f3bca7aa8686a47/execute?api-version=2.0&format=swagger'
    api_key = 'AJ4VbYioTuQoZhiIgtYX8Oax/qQ/XbXXzpyAztpTif896XXdr3rdHh4qpySOl1Ikyph0frMlzfKH1/PpflI0sA=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        return result['Results']['output1'][0]['Scored Label']
    except urllib.error.HTTPError as error:
        return "The request failed with status code: " + str(error.code)



######Launch.


# Default port:
if __name__ == '__main__':
    app.run()