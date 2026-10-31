from django.db import models

# Create your models here.

class Gjaldskra(models.Model):
    birta = models.BooleanField(choices=[(True, 'Já'), (False, 'Nei')], default=False)
    dags= models.DateField(auto_now_add=True)
    gildi_dags= models.DateField()
    tho_bat_alms= models.DecimalField(max_digits=8, decimal_places=5)
    fk_selj= models.IntegerField()
    tho_bat_lagm= models.IntegerField()
    tho_kaup= models.IntegerField()
    vm_bat= models.IntegerField()
    tho_bun_alms= models.DecimalField(max_digits=8, decimal_places=5)
    tho_bun_lagm= models.IntegerField()
    tho_kaup_bun= models.IntegerField(blank=True, null=True)
    tho_vheim_alms= models.DecimalField(max_digits=8, decimal_places=5)
    tho_vheim_lagm= models.IntegerField()
    tho_kaup_vheim= models.IntegerField(blank=True, null=True)
    tho_ft= models.DecimalField(max_digits=8, decimal_places=5)
    tho_ft_lagm= models.IntegerField()
    tho_ft_kaup= models.IntegerField(blank=True, null=True)
    timav_fast= models.IntegerField()
        
    def gjskr(self):
        return f'{self.birta} - {self.gildi_dags}'
  
    def __str__(self):
        return self.gjskr()
