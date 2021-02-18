from django.db import models

class Academy(models.Model) :
    name = models.CharField(max_length=45)
    address_full = models.CharField(max_length=80)
    address_city = models.CharField(max_length=45)
    address_town = models.CharField(max_length=45)
    fee1 = models.IntegerField(null=True)
    fee2 = models.IntegerField(null=True)
    bus = models.CharField(max_length=500, null=True)
    phone_number = models.CharField(max_length=45, null=True)
    url = models.CharField(max_length=500, null=True)

    def __str__(self):
        return "main {}-{}-{}-{}-{}-{}-{}-{}-{}-{}".format(self.id, self.name, self.address_full, self.address_city,
                                                           self.address_town, self.fee1, self.fee2, self.bus, self.url,
                                                           self.phone_number)

class Academy_town(models.Model) :
    town_name = models.CharField(max_length=45)
    city_name = models.CharField(max_length=45)


class TestSite(models.Model) :
    name = models.CharField(max_length=45)
    address_full = models.CharField(max_length=45)
    courseA = models.CharField(max_length=500, null=True)
    courseB = models.CharField(max_length=500, null=True)
    courseC = models.CharField(max_length=500, null=True)
    courseD = models.CharField(max_length=500, null=True)
    phone_number = models.CharField(max_length=45, null=True)
    url = models.CharField(max_length=500, null=True)