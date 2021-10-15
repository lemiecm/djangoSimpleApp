from django.db import models

class Entry(models.Model):
    text = models.TextField()
    # automatically set the time when object is created 
    date_posted = models.DateTimeField(auto_now_add=True)
    
    # text representation of each object in your model
    # or in db
    def _str_(self):
        return 'Entry #{}'.format(self.id)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    
