from django.db import models

# Create your models here.

##****************** Admin Model ******************##
class Admin_Info(models.Model):
    adminname = models.CharField(max_length=300, unique=True)
    adminpassword = models.CharField(max_length=300)
    adminemail = models.EmailField(unique=True)
    adminmobile_no = models.BigIntegerField()

    class Meta:
        db_table = 'admins'


##****************** Questions Model ******************##
class Questions(models.Model):
    qid = models.AutoField(primary_key=True)
    qtext = models.CharField(max_length=300)
    qoption1 = models.CharField(max_length=300)
    qoption2 = models.CharField(max_length=300)
    qoption3 = models.CharField(max_length=300)
    qoption4 = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)

    class Meta:
        db_table = 'questions'

##****************** Student Model ******************##
class Student_Info(models.Model):
    username = models.CharField(primary_key=True, max_length=250)
    password = models.CharField(max_length=300)
    mobile_no = models.BigIntegerField()

    class Meta:
        db_table = 'students'


##****************** Result Model ******************##
class Result(models.Model):
    username = models.ForeignKey('Student_Info', on_delete = models.CASCADE)
    score = models.IntegerField()
    subject = models.CharField(max_length=250)

    class Meta:
        db_table = 'result'   