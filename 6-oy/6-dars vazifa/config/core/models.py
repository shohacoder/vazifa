from django.db import models


class ServiceCategory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Mechanic(models.Model):
    full_name = models.CharField(max_length=155)
    experience_year = models.IntegerField()
    phone = models.CharField(max_length=13, unique=True)
    photo = models.ImageField(upload_to="mechanics/", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

