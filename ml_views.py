from django.shortcuts import render
from ml.models import TrainedModel

def dashboard(request):
    # Load the trained model from the database
    trained_model = TrainedModel.objects.last()

    # Extract the accuracy from the trained model
    model_accuracy = trained_model.accuracy

    # Pass the accuracy to the template
    context = {'model_accuracy': model_accuracy}

    return render(request, 'dashboard.html', context)