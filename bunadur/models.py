from django.db import models
from django.utils.text import slugify
from batar.models import Stadsetning, Svaedi, Att
import os

def dynamic_upload_path_bun(instance, filename):
    # You can use any attribute of your model to create the folder name
    folder_name = slugify(instance.nafn)  # Adjust this as needed
    return os.path.join('uploads','bunadur', folder_name, filename)


class Tegundbun(models.Model):
    tegundbun = models.CharField(max_length=50)

    def __str__(self):
        return self.tegundbun

class Bunadur(models.Model):
    birta = models.BooleanField(null=True, blank=True, choices=[(True, 'Já'), (False, 'Nei')], default=False)
    nyskr_dags= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    rodun= models.IntegerField(null=True, blank=True)
    uppf_dags= models.DateTimeField(null=True, blank=True)
    nafn= models.CharField(max_length=20)
    tegundbun= models.ForeignKey(Tegundbun, on_delete=models.CASCADE, null=True, blank=True)
    stadsetn= models.ForeignKey(Stadsetning, on_delete=models.CASCADE, null=True, blank=True)
    skipti= models.CharField(max_length=100, null=True, blank=True)
    svaedi= models.ForeignKey(Svaedi, on_delete=models.CASCADE, null=True, blank=True)
    lys_selj= models.TextField(null=True, blank=True)
    lysing= models.TextField()
    verd_bun= models.IntegerField(null=True, blank=True)
    tengil_nafn= models.CharField(null=True, blank=True, max_length=100)
    tengil_tp= models.EmailField(null=True, blank=True)
    tengil_simi= models.CharField(null=True, blank=True, max_length=14)
    notes= models.TextField(null=True, blank=True)
    att= models.ForeignKey(Att, on_delete=models.CASCADE, null=True, blank=True)
    lmynd= models.ImageField(upload_to=dynamic_upload_path_bun, null=True, blank=True)
    mynd1= models.ImageField(upload_to=dynamic_upload_path_bun, null=True, blank=True)
    mynd2= models.ImageField(upload_to=dynamic_upload_path_bun, null=True, blank=True)
    mynd3= models.ImageField(upload_to=dynamic_upload_path_bun, null=True, blank=True)
    mynd4= models.ImageField(upload_to=dynamic_upload_path_bun, null=True, blank=True)
    mynd5= models.ImageField(upload_to=dynamic_upload_path_bun, null=True, blank=True)
    mynd6= models.ImageField(upload_to=dynamic_upload_path_bun, null=True, blank=True)
    slug= models.SlugField(unique=True, db_index=True, null=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nafn)
        super(Bunadur, self).save(*args, **kwargs)

    def __str__(self):
        return self.nafn
    
class BunadurFyrirspurn(models.Model):
    skrdags = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    nafn = models.CharField(max_length=30, null=True, blank=True)
    tengil_nafn= models.CharField(null=True, blank=True, max_length=100)
    tengil_tp= models.EmailField(null=True, blank=True)
    tengil_simi= models.CharField(max_length=20, null=True, blank=True)
    fyrirspurn = models.TextField(null=True, blank=True)
    svarad = models.DateField(null=True, blank=True)
    
    
    def skrrev(self):
        return f'{self.nafn}'
  
    def __str__(self):
        return self.skrrev()


    
