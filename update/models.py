from django.conf import settings
from django.db import models


def updateUpload(instance, filname):
    return f"/upload/instance.user/filename"


class Update(models.Model):
    user          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content       = models.TextField(blank=True, null=True)
    image         = models.ImageField(uppload_to=updateUpload, blank=True, null=True)
    def __str__(self):
        return self.content or ""
        
        
