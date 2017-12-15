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
    if(holiday=='Black Friday'')
        blackfriday=1
    data = {
        "Inputs": {
            "input1": [{
                 'unit_sales': "1",
                 'onpromotion': onpromotion,
                 'transactions': transactions,
                 'dcoilwtico': oil,
                 'day_0': "1",
                 'day_3': "1",
                 'day_5': "1",
                 'month_3': "1",
                 'month_5': "1",
                 'month_6': "1",
                 'month_8': "1",
                 'month_9': "1",
                 'month_10': "1",
                 'Azuay': "1",
                 'Bolivar': "1",
                 'Chimborazo': "1",
                 'Cotopaxi': "1",
                 'El Oro': "1",
                 'Esmeraldas': "1",
                 'Guayas': "1",
                 'Imbabura': "1",
                 'Los Rios': "1",
                 'Manabi': "1",
                 'Pastaza': "1",
                 'Pichincha': "1",
                 'Santa Elena': "1",
                 'Santo Domingo de los Tsachilas': "1",
                 'nholidayspike': "1",
                 'blackfriday': "1",
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

