from django.db import models

# Create your models here.
class CRUDModel(models.Model):
    int = models.IntegerField()
    char = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField()

    class Meta:
        verbose_name = 'CRUD_model'
        verbose_name_plural = 'CRUD_models'
        db_table = 'crud_model'
        ordering = ['-id']