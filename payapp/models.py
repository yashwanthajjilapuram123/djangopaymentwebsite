from django.db import models

# Contact models saves all the information related to user and ueer queries.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name + self.email



