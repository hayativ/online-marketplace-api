from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)  # название курса
    description = models.TextField()          # описание курса
    price = models.DecimalField(max_digits=8, decimal_places=2)  # цена курса
    created_at = models.DateTimeField(auto_now_add=True)         # дата создания

    def __str__(self):
        return self.title