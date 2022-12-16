from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Todolist(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    task = models.CharField(max_length=200)
    priority = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task