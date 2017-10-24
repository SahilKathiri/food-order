from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
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
            ('view_customer_portal', "Can view customer portal"),
        )
