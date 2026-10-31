from django.db import models
from django.utils.text import slugify
import os

# Create your models here.

def dynamic_upload_path(instance, filename):
    folder_name = slugify(instance.nafn)
    return os.path.join('uploads', 'aflaheim', folder_name, filename)

class Tegundaflah(models.Model):
    tegundaflah = models.CharField(max_length=50)

    def __str__(self):
        return self.tegundaflah
    
class Tegundsjavaraf(models.Model):
    tegundsjavaraf = models.CharField(max_length=10)

    def __str__(self):
        return self.tegundsjavaraf

from django.db import models
from django.utils.text import slugify

class Aflaheim(models.Model):
    birta = models.BooleanField(null=True, blank=True, choices=[(True, 'Já'), (False, 'Nei')], default=False)
    nyskr_dags= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    rodun = models.IntegerField(null=True, blank=True)
    uppf_dags = models.DateField(null=True, blank=True)
    nafn = models.CharField(max_length=50, null=True, blank=True)
    tegundaflah = models.ForeignKey(Tegundaflah, on_delete=models.CASCADE, null=True, blank=True)
    bat_nr = models.IntegerField(null=True, blank=True)
    tegsjavaraf = models.ForeignKey(Tegundsjavaraf, on_delete=models.CASCADE, null=True, blank=True)
    magn_hlutd = models.DecimalField(null=True, blank=True, max_digits=11, decimal_places=9)
    magn_aflmark = models.IntegerField(null=True, blank=True)
    verdsamt = models.IntegerField(null=True, blank=True)
    verdptonn = models.IntegerField(null=True, blank=True)
    lys_selj = models.TextField(null=True, blank=True)
    athsemd = models.TextField(null=True, blank=True)
    ktaflah = models.CharField(null=True, blank=True, max_length=100)
    tengil_nafn = models.CharField(null=True, blank=True, max_length=100)
    tengil_tp = models.EmailField(null=True, blank=True)
    tengil_simi = models.CharField(null=True, blank=True, max_length=14)
    notes = models.TextField(null=True, blank=True)
    lmynd = models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    slug = models.SlugField(unique=True, db_index=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nafn)
        if self.verdsamt and self.magn_aflmark:
            self.verdptonn = self.verdsamt / self.magn_aflmark
        super(Aflaheim, self).save(*args, **kwargs)

    def __str__(self):
        return self.nafn
    
class AflaheimFyrirspurn(models.Model):
    skrdags = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    nafn = models.CharField(max_length=30, null=True, blank=True)
    tengil_nafn= models.CharField(null=True, blank=True, max_length=100)
    tengil_tp= models.EmailField(null=True, blank=True)
    tengil_simi= models.CharField(max_length=20, null=True, blank=True)
    fyrirspurn = models.TextField(null=True)
    svarad = models.DateField(null=True, blank=True)
    
    def skrrev(self):
        return f'{self.nafn}'
  
    def __str__(self):
        return self.skrrev()
#    def __str__(self): 
#        return f"Request for {self.nafn.nafn}"
