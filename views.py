from django.shortcuts import render
from mlmodels.models import TrainedModel

def dashboard(request):
    # Load the trained model from the database
    trained_model = TrainedModel.objects.last()

    # Extract the accuracy from the trained model
    model_accuracy = trained_model.accuracy

    # Load the data from the database
    data = TrainedModel.objects.all()

    # Pass the data and accuracy to the template
    context = {'data': data, 'model_accuracy': model_accuracy}

    return render(request, 'dashboard.html', context)