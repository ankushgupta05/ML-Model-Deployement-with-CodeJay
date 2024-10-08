from django.shortcuts import render, HttpResponse

import sklearn
import joblib 
from math import ceil
# import pickle
# model = joblib.load('static/random_forest_regression')
# model = joblib.load('Model/random_forest_regression.joblib')

model = joblib.load('static/Linear_Regression_model')

# with open('./Model/model_pickle','rb') as f:
#     model = pickle.load(f)

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse('<h2>Home page </h2>')


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def login(request):
    return render(request,'login.html')


def registration(request):
    return render(request,'registration.html')


def prediction(request):
    if request.method == 'POST':
        # print(request.POST)
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        bmi = int(request.POST.get('bmi'))
        children = int(request.POST.get('children'))
        smoker = int(request.POST.get('smoker'))
        region = int(request.POST.get('region'))
        
        print(age,sex,bmi,children,smoker,region)
        pred = model.predict([[age, sex, bmi, children, smoker, region]])
        
        # try:
        #     pred = model.predict([[age, sex, bmi, children, smoker, region]])
        #     print(pred)
        #  # Handle the specific attribute error
        # except AttributeError as e:
        #     print(f"An error occurred: {e}")
        
        
        
        
        pred = model.predict([[age, sex, bmi, children, smoker, region]])
        print(ceil(pred[0]))
        
        output ={
            'output':ceil(pred[0])
        }
        
        return render(request,'prediction.html',output)

    else:
        return render(request,'prediction.html')
    
    
    
    