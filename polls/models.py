from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Question(models.Model):
	question_test=models.CharField(max_length=200)
	pub_date=models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.question_test

class Choice(models.Model):
	question=models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
	def test_fun(self):
		print("its working")

class Detail(models.Model):
	Name=models.CharField(max_length=20)
	age=models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
