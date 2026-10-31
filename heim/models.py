from django.db import models

# Create your models here.


# heim/models.py
from django.db import models

class PageVisit(models.Model):
    url = models.CharField(max_length=255, unique=True)
    visit_count = models.IntegerField(default=0, null=True, blank=True)
    ip_addresses = models.TextField()  # Store IP addresses as a comma-separated string

    def __str__(self):
        return f"{self.url} - {self.visit_count} visits"

    def add_ip_address(self, ip_address):
        ip_list = self.ip_addresses.split(',')
        if ip_address not in ip_list:
            ip_list.append(ip_address)
            self.ip_addresses = ','.join(ip_list)
            self.visit_count += 1
            self.save()


class Fyrirspurn(models.Model):
    dags= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    nafn = models.CharField(max_length=100)
    tp= models.EmailField()
    titill= models.CharField(max_length=100)
    fyrirspurn = models.TextField()
    svarad= models.DateTimeField(null=True, blank=True)
    
    def skrrev(self):
        return f'{self.dags} - {self.titill}'
  
    def __str__(self):
        return self.skrrev()
#    def __str__(self): 
#        return f"Request for {self.nafn.nafn}"