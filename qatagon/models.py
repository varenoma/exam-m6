from django.db import models

# Create your models here.


class QatagonClass(models.Model):
    full_name = models.CharField(max_length=150, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    died_date = models.DateField(null=False, blank=False)
    description = models.TextField()
    region = models.CharField(max_length=150)
    ayblov = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
