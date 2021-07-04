from django.db import models

# Create your models here
class User(models.Model):
    userName = models.CharField("User Name", max_length=40, )
    email = models.CharField("Email", max_length=50)
    password = models.CharField("Password", max_length=40)

    # Change name seen to user name
    def __str__(self):
        return self.userName

class Answer(models.Model):
    name = models.CharField("Quiz Taker", max_length=30, default="Name")
    answer1 = models.CharField("How many planets does the solar sytem have?", max_length=10, default=0)
    answer2 = models.CharField("How far away is the sun from the earth? (In kms)", max_length=10, default=0)
    answer3 = models.BooleanField("Does Saturn have a ring system?", default=False)
    answer4 = models.BooleanField("The name of Mercury is based off of greek mythology.", default=False)
    answer5 = models.CharField("How many moons does Mars have?", max_length=10, default=0)
    answer6 = models.BooleanField("Does a planet have to orbit a star?", default=False)
    answer7 = models.CharField("How many moons does the Earth have?", max_length=10, default=0)
    answer8 = models.BooleanField("Does the name Venus have greek inspirations?", default=False)
    answer9 = models.BooleanField("Is Mars often referred as the Blue Planet?", default=False)
    answer10 = models.CharField("What is the name of the satellite orbiting the Earth?", max_length=20, default="Satellite")

    def __str__(self):
        return self.name

class Comment(models.Model):
    userName = models.CharField("User Name", max_length=30)
    comment = models.CharField("Comment", max_length=255)
    rating = models.CharField("Rating (0...9)", max_length=1, default=0)

    def __str__(self):
        return self.userName
