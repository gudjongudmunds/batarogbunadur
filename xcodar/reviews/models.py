from django.db import models

# Create your models here.


class Boats(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    # Add other fields as needed
    
    def skrboats(self):
        return f'{self.name}'
  
    def __str__(self):
        return self.skrboats()
    
class Review(models.Model):
    rev_batur = models.ForeignKey(Boats, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True)
    comment = models.TextField(null=True)
    # Add other fields as needed
    
    def skrrev(self):
        return f'{self.rev_batur}'
  
    def __str__(self):
        return self.skrrev()
    

