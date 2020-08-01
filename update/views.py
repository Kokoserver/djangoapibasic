import json
from django.core.serializers import serialize
from django.http import JsonResponse
from django.views.generic import View
from django.shortcuts import render,HttpResponse
from .models import Update
from restapi.jsonResponseMixin import JsonMixin
# Create your views here.

def update_model_detail_view(request):
    # data = {
    #     "user":"owonikoko",
    #     "content":"it's working now"
    # }
    # return JsonResponse(data)
    ## using httpResponse
   data = {
        "user":"owonikoko",
        "content":"it's working now"
    }
   
   json_data = json.dumps(data)
   return HttpResponse(json_data, content_type="application/json")

## using class based view
class UpdateDetailView(View):
    def get(self, request, *args, **kwargs):
        data = {
        "user":"owonikoko",
        "content":"it's working now"
    }
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type="application/json")
    
## using jsonResponse with mixins
class UpdateDetailView2(JsonMixin,View):
    def get(self, request, *args, **kwargs):
        data = {
        "user":"owonikoko",
        "content":"it's working now"
        }
        return self.respond_json_data(data)
    
## using jsonResponse with mixins
class SerializeView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        # data = {
        # "user":obj.user.username,
        # "content":obj.content
        # }
        # json_data = serialize('json', [obj], fields=("id", "user", "content", "image"))
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type="application/json")
    
    
    
class SerializeListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        # json_data = serialize('json', qs, fields=("id", "user", "content", "image") )
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type="application/json")