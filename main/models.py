from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    slug=models.SlugField()
    content=models.CharField(max_length=1024)

    def __str__(self):
        return self.content
        
class Answer(models.Model):
    question=models.ForeignKey('Question',on_delete=models.CASCADE)   #Answer is made by an user by a choice for                                                                       #a question
    choice=models.ForeignKey('Choice',on_delete=models.CASCADE)       # a question
    user=models.ForeignKey(User,on_delete=models.CASCADE)        


class Choice(models.Model):
    question=models.ForeignKey('Question',on_delete=models.CASCADE)
    content=models.CharField(max_length=256)

    @property
    def answer_count(self):  #This function will tell us the number of users who have chosen a particular choice for a given question
        return Answer.objects.filter(
            question=self.question,
            choice=self.id
        ).count()

    def __str__(self):
        return "{}-{}".format(self.question.content[:50],self.content)

