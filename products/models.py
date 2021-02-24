from django.db import models


class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to='media')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
