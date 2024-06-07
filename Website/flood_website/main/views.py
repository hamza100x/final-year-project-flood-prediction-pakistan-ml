from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm, PredForm
from .ml_model import Ndsi_q, Rain_q, Temp_q, Veg_q
from django.contrib import messages
import pandas as pd
# Create your views here.

def index(request):
    return render(request=request, 
                  template_name='main/index1.html')

def predict(request): 
    return render(request=request, 
                      template_name='main/predict.html', context={"rain": round(rain[0],3), "flood":flood, "snow":round(snow[0],4) ,"date":date, "veg":round(veg[0],3) , "temp":int(temp[0]),"prov":pro })


def index2(request):
    if request.method == 'POST':
        form = PredForm(request.POST)
        if form.is_valid():
            year = int(form.cleaned_data['year'])
            Month = int(form.cleaned_data['Month'])
            prov =  int(form.cleaned_data['Pro'])
            global flood
            global temp
            global veg
            global snow
            global rain
            global pro
            global date
            date="Month :"+str(Month)+" Year :"+str(year)
            pro=prov
            if(prov==1):
                inp0=[[ Month, year]]
                temp = Temp_q(prov,inp0)
                inp1=[[Month,year,temp[0]]]
                snow=Ndsi_q(prov,inp1)
                inp2=[[Month,year,temp[0]]]
                veg=Veg_q(prov,inp2)
                inp3=[[Month,year,temp[0],snow[0]]]
                rain=Rain_q(prov,inp3)
            elif(prov==2):
                inp0=[[ Month, year]]
                temp = Temp_q(prov,inp0)
                inp1=[[Month,year,temp[0]]]
                snow=Ndsi_q(prov,inp1)
                inp2=[[Month,year,temp[0]]]
                veg=Veg_q(prov,inp2)
                inp3=[[Month,year,temp[0],snow[0],veg[0]]]
                rain=Rain_q(prov,inp3)
            elif(prov==3):
                inp0=[[ Month, year]]
                temp = Temp_q(prov,inp0)
                inp1=[[Month,year,temp[0]]]
                snow=Ndsi_q(prov,inp1)
                inp2=[[Month,year,temp[0]]]
                veg=Veg_q(prov,inp2)
                inp3=[[Month,year,temp[0],snow[0],veg[0]]]
                rain=Rain_q(prov,inp3)
            elif(prov==4):
                inp0=[[ Month, year]]
                temp = Temp_q(prov,inp0)
                inp1=[[Month,year,temp[0]]]
                snow=Ndsi_q(prov,inp1)
                inp2=[[Month,year,temp[0]]]
                veg=Veg_q(prov,inp2)
                inp3=[[Month,year,temp[0],snow[0]]]
                rain=Rain_q(prov,inp3)
            elif(prov==5):          
                inp0=[[ Month, year]]
                temp = Temp_q(prov,inp0)
                inp1=[[Month,year,temp[0]]]
                snow=Ndsi_q(prov,inp1)
                inp2=[[Month,year,temp[0]]]
                veg=Veg_q(prov,inp2)
                inp3=[[Month,year,temp[0],snow[0],veg[0]]]
                rain=Rain_q(prov,inp3)
            elif(prov==6):
                inp0=[[ Month, year]]
                temp = Temp_q(prov,inp0)
                inp1=[[Month,year,temp[0]]]
                snow=Ndsi_q(prov,inp1)
                inp2=[[Month,year,temp[0]]]
                veg=Veg_q(prov,inp2)
                inp3=[[Month,year,temp[0],snow[0]]]
                rain=Rain_q(prov,inp3)

            if(prov==1 and rain>97):
                flood='Risk in Punjab'
                return redirect("/predict")
            elif(prov==2 and rain>71):
                flood='Risk in Sindh'
                return redirect("/predict")
            elif(prov==4 and rain>26):
                flood='Risk in Balochistan'
                return redirect("/predict")
            elif(prov==3 and rain>95):
                flood='Risk in Kpk'
                return redirect("/predict")
            elif(prov==5 and rain>59):
                flood='Risk in Gilgit'
                return redirect("/predict")
            elif(prov==6 and rain>304):
                flood='Risk in Federal'
                return redirect("/predict")    
            else:
                flood='No Risk'
                print(rain)
                return redirect("/predict")    
        else:
            problem = form.errors.as_data()
            # This section is used to handle invalid data 
            messages.error(request, list(list(problem.values())[0][0])[0])
            form = PredForm()
    form = PredForm()
    return render(request=request, template_name='main/index2.html', context={"form": form})


def about(request):
    return render(request=request, 
            template_name="main/about.html")


def Guide(request):
    return render(request=request, 
            template_name="main/Guide.html")