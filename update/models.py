import json
from django.core.serializers import serialize
from django.conf import settings
from django.db import models


def updateUpload(instance, filname):
    return f"/upload/instance.user/filename"

class UpdateQueryset(models.QuerySet):
    # this will return an array of objects containing all the detains to json data with all the db details
    # def serialize(self):
    #     qs = self
    #     json_data = serialize('json', qs, fields=("id", "user", "content", "image"))
    #     return json_data
    
    # def serialize(self):
    # this will return an array of json data only the data needed
    #     qs = self
    #     json_data = [json.loads(data.serialize()) for data in qs]
    #     return json.dumps(json_data)
    
      def serialize(self):
          # this will return exacly as second serialize 
          qs = self
          list_values = list(qs.values("id", "user", "content", "image"))
          return json.dumps(list_values)

class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQueryset(model=self.model, using=self._db)


class Update(models.Model):
    user          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content       = models.TextField(blank=True, null=True)
    image         = models.ImageField(upload_to=updateUpload, blank=True, null=True)
    updated       = models.DateField(auto_now=True)
    timestamp     = models.DateTimeField(auto_now_add=True)
    objects       = UpdateManager()
    
    def serialize(self):
        ######## this will return individual serializable object to json of this db 
        # obj = serialize('json', [self], fields=("id", "user", "content", "image"))
        # obj = json.loads(obj)
        # json_data = json.dumps(obj[0]['fields'])
        
        ## this will return better the same thing in a consice way
        try:
            image = self.image.url
        except:
            image = ""
        data = {
            "id":self.id,
            "user": self.user.id,
            "content":self.content,
            "image":image   
        }
        data = json.dumps(data)
        return data
    
    def __str__(self):
        return self.content or ""
        
        
