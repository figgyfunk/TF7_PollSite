from django.db import models
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Arch(models.Model):
    name = models.CharField(max_length=200)
    jan = models.IntegerField(default=0)
    feb = models.IntegerField(default=0)
    mar = models.IntegerField(default=0)
    apr = models.IntegerField(default=0)
    may = models.IntegerField(default=0)
    jun = models.IntegerField(default=0)
    jul = models.IntegerField(default=0)
    aug = models.IntegerField(default=0)
    sep = models.IntegerField(default=0)
    oct = models.IntegerField(default=0)
    nov = models.IntegerField(default=0)
    dec = models.IntegerField(default=0)

    mark = models.IntegerField(default=0)
    acc = models.IntegerField(default=0)
    exec = models.IntegerField(default=0)
    des = models.IntegerField(default=0)
    pro = models.IntegerField(default=0)

    def __str__(self):
        return self.name
