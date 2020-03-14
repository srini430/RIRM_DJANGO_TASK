from django.db import models

class Clients(models.Model): #Clients table
    First_name = models.CharField(max_length = 100)

    

    class Meta:
        verbose_name_plural = 'clients'

    def __str__(self):
        return self.First_name

    

class ClientDetail(models.Model): #Client details to be filled by user into db
    client = models.ForeignKey('Clients', on_delete = models.CASCADE)
    full_name  = models.CharField(max_length = 100)
    mobile_phone = models.CharField(max_length = 20)
    client_value = models.FloatField()
    email  = models.EmailField()
    web_address = models.URLField()

    class Meta:
        unique_together = ["full_name", "mobile_phone", "email"]

    def __str__(self):
        return self.full_name
    

   
    



