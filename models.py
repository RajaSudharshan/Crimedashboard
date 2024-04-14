from django.db import models

class TrainedModel(models.Model):
    name = models.CharField(max_length=100)
    model = models.BinaryField()
    accuracy = models.FloatField()
    classification_report = models.TextField()

    def __str__(self):
        return self.name