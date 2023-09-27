from django.db import models
# Create your models here.
from .python_excel import field_names

class ExcelModelNew(models.Model):
    for field in field_names:
        locals()[field]=models.CharField(max_length=20)

    """
    city_name=models.CharField(max_length=10)
    event_name=models.CharField(max_length=30)
    event_details=models.CharField(max_length=50)
    """

    def __str__(self):
        return self.field_names[1]
    


        

