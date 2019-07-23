from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)

    def full_name(self):
        full_name = ('{} {}'.format(self.first_name, self.last_name))
        return full_name

    def __str__(self):
        return self.full_name()