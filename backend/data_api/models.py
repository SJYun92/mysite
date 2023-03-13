from django.db import models
from django.utils import timezone

# Create your models here.

class MyDesignItem(models.Model) :
    design_name = models.CharField(max_length=255)
    designer = models.CharField(max_length=20)
    design_code = models.CharField(max_length=17, unique=True)
    img = models.TextField(blank=True ,default='https://izapislewska.weebly.com/uploads/4/9/8/6/49862713/custom-design_orig.png')

    def __str__(self) :
        return self.design_name