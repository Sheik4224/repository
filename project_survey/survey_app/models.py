from django.db import models
from django.http import HttpResponse
# Create your models here.
from django.db import models
from django.db.models import ForeignKey
class Question(models.Model):
    question_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    question=models.CharField(max_length=255)
class Answer(models.Model):
    surveyid=ForeignKey(Question,on_delete=models.CASCADE)
    answer=models.CharField(max_length=255)
'sheik'

