from django.shortcuts import render, HttpResponse

import joblib
model = joblib.load('static/random_forest_regression')


# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse('<h2>Home page </h2>')


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def prediction(request):
    if request.method == 'post':
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        bmi = int(request.POST.get('bmi'))
        children = int(request.POST.get('children'))
        smoker = int(request.POST.get('smoker'))
        region = int(request.POST.get('region'))
        
        print(age,sex,bmi,children,smoker,region)
        pass
    else:
        pass
    
    return render(request,'prediction.html')
