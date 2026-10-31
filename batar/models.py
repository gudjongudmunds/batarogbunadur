from django.db import models
from django.utils.text import slugify
import os


def dynamic_upload_path(instance, filename):
    folder_name = slugify(instance.nr)
    return os.path.join('uploads', 'batar', folder_name, filename)


class Batategund(models.Model):
    tegund = models.CharField(max_length=50)

    def __str__(self):
        return self.tegund
    
class Batahradi(models.Model):
    hradi_bat = models.CharField(max_length=50)

    def __str__(self):
        return self.hradi_bat

class Batavel(models.Model):
    vel = models.CharField(max_length=50)

    def __str__(self):
        return self.vel
    
class Batagerd(models.Model):
    gerd = models.CharField(max_length=50)

    def __str__(self):
        return self.gerd
    
class Att(models.Model):
    att = models.CharField(max_length=50)

    def __str__(self):
        return self.att

class Stadsetning(models.Model):
    stadsetn = models.CharField(max_length=50)

    def __str__(self):
        return self.stadsetn
    
class Svaedi(models.Model):
    svaedi = models.CharField(max_length=50)

    def __str__(self):
        return self.svaedi
    
class Smidastod(models.Model):
    smidast = models.CharField(max_length=50)

    def __str__(self):
        return self.smidast

class Efnibol(models.Model):
    efnibol = models.CharField(max_length=50)

    def __str__(self):
        return self.efnibol
    
class Heimahofn(models.Model):
    heimahofn = models.CharField(max_length=50)

    def __str__(self):
        return self.heimahofn

class Batar(models.Model):
    birta = models.BooleanField(null=True, blank=True, choices=[(True, 'Já'), (False, 'Nei')], default=False)
    nyskr_dags= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    rodun= models.IntegerField(null=True, blank=True)
    uppf_dags= models.DateField(null=True, blank=True)
    nr= models.IntegerField()
    nafn= models.CharField(max_length=100)
    tegund = models.ForeignKey(Batategund, on_delete=models.CASCADE, null=True, blank=True)
    smidast= models.ForeignKey(Smidastod, on_delete=models.CASCADE, null=True, blank=True)
    arg_bat= models.IntegerField(null=True, blank=True)
    br_tonn= models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    lengd_bat= models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    mestlengd_bat= models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    breidd_bat= models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    dypt_bat= models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    efnibol_bat= models.ForeignKey(Efnibol, on_delete=models.CASCADE, null=True, blank=True)
    heimahofn= models.ForeignKey(Heimahofn, on_delete=models.CASCADE, null=True, blank=True)
    stadsetn= models.ForeignKey(Stadsetning, on_delete=models.CASCADE, null=True, blank=True)
    svaedi= models.ForeignKey(Svaedi, on_delete=models.CASCADE, null=True, blank=True)
    skipti= models.CharField(max_length=100, null=True, blank=True)
    lys_vel_selj= models.TextField(null=True, blank=True)
    vel= models.ForeignKey(Batavel, on_delete=models.CASCADE, null=True, blank=True)
    vel_arg= models.IntegerField(null=True, blank=True)
    vel_afl= models.CharField(max_length=100, null=True, blank=True)
    hradi_bat= models.ForeignKey(Batahradi, on_delete=models.CASCADE, null=True, blank=True)
    keyrsla_vel= models.IntegerField(null=True, blank=True)
    lys_vel= models.TextField(null=True, blank=True)
    lys_taeki_selj= models.TextField(null=True, blank=True)
    taeki_bjarg= models.CharField(max_length=100, null=True, blank=True)
    taeki_dypt= models.CharField(max_length=100, null=True, blank=True)
    taeki_gps= models.CharField(max_length=100, null=True, blank=True)
    taeki_plotter= models.CharField(max_length=100, null=True, blank=True)
    taeki_sjalfst= models.CharField(max_length=100, null=True, blank=True)
    taeki_talst= models.CharField(max_length=100, null=True, blank=True)
    taeki_rad= models.CharField(max_length=100, null=True, blank=True)
    taeki_tolva= models.CharField(max_length=100, null=True, blank=True)
    taeki_siglhugb= models.CharField(max_length=100, null=True, blank=True)
    taeki_ais= models.CharField(max_length=100, null=True, blank=True)
    taeki_annad= models.TextField(null=True, blank=True)
    lys_fylgi_selj= models.TextField(null=True, blank=True)
    fylgi_veidarf= models.TextField(max_length=200, null=True, blank=True)
    fylgi_aflah= models.CharField(max_length=100, null=True, blank=True)
    fylgi_kor= models.CharField(max_length=100, null=True, blank=True)
    fylgi_vagn= models.CharField(max_length=100, null=True, blank=True)
    lys_fylgi= models.TextField(null=True, blank=True)
    lys_annad_selj= models.TextField(null=True, blank=True)
    gerd_bat= models.ForeignKey(Batagerd, on_delete=models.CASCADE, null=True, blank=True)
    lys_annad= models.TextField(null=True, blank=True)
    verd_bat= models.IntegerField(null=True, blank=True)
    sgs= models.TextField(null=True, blank=True)
    fiskistofa= models.TextField(null=True, blank=True)
    tengil_nafn= models.CharField(null=True, blank=True, max_length=100)
    tengil_tp= models.EmailField(null=True, blank=True)
    tengil_simi= models.CharField(max_length=20, null=True, blank=True)
    notes= models.TextField(null=True, blank=True)
    att= models.ForeignKey(Att, on_delete=models.CASCADE, null=True, blank=True)
    lmynd= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd1= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd2= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd3= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd4= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd5= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd6= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd7= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd8= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd9= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd10= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd11= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd12= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd13= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd14= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd15= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd16= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd17= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd18= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd19= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    mynd20= models.ImageField(upload_to=dynamic_upload_path, null=True, blank=True)
    soluyfirl= models.FileField(upload_to=dynamic_upload_path, null=True, blank=True)
    slug= models.SlugField(unique=True, db_index=True)

    def __str__(self): 
        return f'{self.nr} - {self.nafn}' if self.nafn else str(self.nr)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nafn)
        super(Batar, self).save(*args, **kwargs)

   
class BatarFyrirspurn(models.Model):
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



    