from django.db import models

# Create your models here.

class Gallery(models.Model):
  slug= models.SlugField(unique=True, db_index=True)
  date= models.DateField(auto_now=True)
  titill= models.CharField(max_length=100)
  kynning= models.CharField(max_length=300)
  lysing= models.TextField()
  lmynd= models.CharField(max_length=100)
  mynd1= models.CharField(max_length=100)
  mynd2= models.CharField(max_length=100)
  mynd3= models.CharField(max_length=100)
  mynd4= models.CharField(max_length=100)
  ath= models.TextField()
  
  def titill_date(self):
    return f'{self.titill} {self.date}'
  
  def __str__(self):
    return self.titill_date()
  
 
class Fyrirspurn(models.Model):
  verk= models.ForeignKey(Gallery, on_delete=models.SET_NULL, null=True)
  dags= models.DateField(auto_now=True)
  nafn= models.CharField(max_length=100)
  tp= models.EmailField()
  umsogn= models.TextField()
  
  def verk_nafn(self):
    return f'{self.verk} {self.nafn}'
  
  def __str__(self):
    return self.verk_nafn()