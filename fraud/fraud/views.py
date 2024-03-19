from django.http import HttpResponse
from django.shortcuts import  render

import joblib

def index(request):
    return render(request,"index.html",)

def result(request):
    # Load the machine learning model
    cls = joblib.load('model.joblib')

    # Retrieve form data from the GET parameters
    Transtype = request.GET['TransType']
    Amount = request.GET['Amount']
    OldBal = request.GET['OldBal']
    NewBal = request.GET['NewBal']
    OldBalDes = request.GET['OldBalDes']
    NewBalDes = request.GET['NewBalDes']

    # Store form data in a list
    lis = [Transtype, Amount, OldBal, NewBal, OldBalDes, NewBalDes]

    # Print the list for debugging
    print(lis)

    # Make prediction using the machine learning model
    ans = cls.predict([lis])

    # Convert the NumPy array to a list
    prediction = ans.tolist()

    # Print the prediction for debugging
    print(prediction)

    # Pass the prediction to the template context
    context = {
        'prediction': prediction
    }

    # Render the 'result.html' template with the prediction
    return render(request, "result.html", {'prediction': prediction})