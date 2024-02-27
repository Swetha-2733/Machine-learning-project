from django.shortcuts import render

# Create your views here.


def index(request):
  return render(request,'index.html')

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
def homepage(request):
  if(request.method=="POST"):
    data=request.POST
    Utc=data.get('textutc')
    Temperature=data.get('texttemperature')
    Humidity=data.get('texthumidity')
    TVOC=data.get('textTVOC')
    eCO2=data.get('texteCO2')
    Raw_H2=data.get('textRawH2')
    Raw_Ethanol=data.get('textRawEthanol')
    Pressure=data.get('textpressure')
    PM1=data.get('textPM1')
    PM2=data.get('textPM2')
    NC0=data.get('textNC0')
    NC1=data.get('textNC1')
    NC2=data.get('textNC2')
    CNT=data.get('textCNT')
    if('buttonpredict' in request.POST):
      import pandas as pd
      path="C:\\Users\\swathi\\OneDrive\\Desktop\\7_smokedetectorclassification\\train_dataset.csv"
      data=pd.read_csv(path)
      #print(data)
      #print(data.shape) #very large data set
      inputs=data.drop('Fire Alarm','columns')
      output=data['Fire Alarm']
      #print(inputs)
      #print(output)
      import sklearn
      from sklearn.model_selection import train_test_split
      x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.8)
      #print(x_train)
      #print(x_test)
      #print(y_train)
      #print(y_test)
      from sklearn.ensemble import RandomForestClassifier
      model=RandomForestClassifier(n_estimators=50)
      model.fit(x_train,y_train)

      y_pred=model.predict(x_test)
      #print(y_pred)
      #print(y_test)
      res=model.predict([[int(Utc),float(Temperature),float(Humidity),int(TVOC),int(eCO2),int(Raw_H2),int(Raw_Ethanol),float(Pressure),float(PM1),float(PM2),float(NC0),float(NC1),float(NC2),int(CNT)]])
      print(res)
      if res==1:
        return HttpResponse("Fire is on!!!!!")
      else:
        return HttpResponse("Fire is off!!!!!!!!!!!!")
    return render(request,'homepage.html',context={'res':res})  
  return render(request,'homepage.html')