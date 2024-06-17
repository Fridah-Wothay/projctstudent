from django.db import models

# Create your models here.
class Class(models.Model):
      educational_resources = models.CharField(max_length = 20)
      tables = models.PositiveSmallIntegerField()
      chairs = models.CharField(max_length = 20)
      room_number = models.PositiveSmallIntegerField()
      assignment = models.CharField(max_length = 20)
      capacity = models.PositiveSmallIntegerField()
      class_id = models.PositiveSmallIntegerField()
      teacher = models.CharField(max_length = 20)
      academic_year = models.PositiveSmallIntegerField()
      learning_hours = models.PositiveSmallIntegerField()



def __str__(self):
        return f"{self.educational_resources} {self.tables}"









