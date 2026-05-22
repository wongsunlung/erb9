from django.db import models

# Create your models here.
class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    Contact_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(blank=True, null=True)

    def _str_(self):
        return self.name
