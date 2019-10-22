from django.db import models


class Students(models.Model):
    roll_no = models.BigIntegerField()
    name = models.CharField(max_length=250)
    branch = models.CharField(max_length=250)

    def __str__(self):
        return str(self.roll_no)
