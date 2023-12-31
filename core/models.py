from django.db import models


class WorkCategory(models.Model):
    title = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to ='work-category/')
    
    def __str__(self):
        return self.title


class Work(models.Model):
    category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to ='work/')

    def __str__(self):
        return self.category.title + " : " + self.title
