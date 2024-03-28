from django.db import models


class Artiles(models.Model):
    title = models.CharField('Lucifer', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date of publication')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
