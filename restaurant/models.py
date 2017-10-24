from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    EMIRATE_CHOICE = (
        ('DXB', 'Dubai'),
        ('SHJ', 'Sharjah'),
        ('AJM', 'Ajman'),
        ('ADB', 'Abu Dhabi'),
        ('UAQ', 'Umm Al Quwain'),
        ('ALA', 'Al Ain'),
        ('RAK', 'Ras Al Khaimah'),
    )

    user = models.OneToOneField(User)
    phone_no = models.CharField("Phone Number", max_length=20)
    address_1 = models.CharField("Address Line 1", max_length=50)
    address_2 = models.CharField("Address Line 2", max_length=50)
    address_emirate = models.CharField("Emirate", max_length=3, choices=EMIRATE_CHOICE)


    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)

    class Meta:
        permissions = (
            ('view_restaurant_portal', "Can view restaurant portal"),
        )

class FoodItem(models.Model):
    name = models.CharField("Name", max_length=50)
    price = models.FloatField("Price")
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    times_ordered = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{0} - {1} {2}".format(self.name, self.restaurant.user.first_name,
                                    self.restaurant.user.last_name)
