from django.db import models

class ContactInfo(models.Model):
    name = models.CharField(max_length = 150, null=False, blank=False)
    phone = models.CharField(max_length = 10, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length = 300)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name + '<'+ self.email +'>: ' + self.subject


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100, null=False, blank=False)
    role = models.CharField(max_length=100, null=False, blank=False)
    profile_pic = models.ImageField(upload_to='clients/img/')
    testimonial = models.TextField()

    def __str__(self):
        return f"{self.client_name} | {self.role}"

