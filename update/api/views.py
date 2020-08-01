import json
from django.views.generic import View
from django.http import HttpResponse
from restapi.jsonResponseMixin import HttpResponseMixin
from .mixin import CSRFExemptMixin
from update.models import Update
from update.form import UpdateForm
from .utils import is_json


class UpdateModelDetailApiView(CSRFExemptMixin,HttpResponseMixin,View):
    is_json = True
    def get_data(self, id=None):
        try:
            obj = Update.objects.get(id=id)
        except Update.DoesNotExist:
            obj = None
        return obj
    
    def get(self, request, id, *args, **kwargs):
        obj = self.get_data(id=id)
        if obj is None:
            error = json.dumps({"error": "Not found"})
            return self.render_to_response(error, status=404)
        else:
          obj = Update.objects.get(id=id).serialize()
          return self.render_to_response(obj, status=200)
    
   
class UpdateModelListApiView(CSRFExemptMixin,HttpResponseMixin,View):
    is_json = True
    querySet = None
    def get_data(self, id=None):
        if id is None:
            return None
        try:
            obj = Update.objects.get(id=id)
        except Update.DoesNotExist:
            obj = None
        return obj
    
    def get_queryset(self):
        qs = Update.objects.all().serialize()
        self.querSet = qs
        return qs
    
    def get(self, request, *args, **kwargs):
        data = json.loads(request.body)
        passed_id = data.get("id", None)
        print(passed_id)
        if passed_id is not None:
            obj = self.get_data(id=passed_id)
            if obj is None:
                error = json.dumps({"error": "Not found"})
                return self.render_to_response(error, status=404)
            json_data = obj.serialize()
            return self.render_to_response(json_data, status=200)
        obj = Update.objects.all().serialize()
        return self.render_to_response(obj, status=200)
    
    def post(self, request, *args, **kwargs):
        valid_json = is_json(request.body) # to get the request being pass
        if not valid_json:
            error = json.dumps({"error":"Invalid data sent, please sent json data"})
            return self.render_to_response(error, status=400)
        data = json.loads(request.body)
        form = UpdateForm(data)
        if form.is_valid():
            obj = form.save(commit=True)
            data = obj.serialize()
            return self.render_to_response(data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        error = json.dumps({"message":"Not allow"})
        return self.render_to_response(error, status=400)
    def put(self, request, *args, **kwargs):
        old_data = json.loads(request.body)
        pass_id = old_data.get("id", None)
        if not pass_id:
            response = {"id":"This is required to update an item"}
            error = json.dumps(response)
            return self.render_to_response(error, status=400)
        obj = self.get_data(id=pass_id)
        if obj is None:
            error = json.dumps({"error":"Object not found"})
            return self.render_to_response(error, status=403)
        valid_json = is_json(request.body)# to get the request being pass
        if not valid_json:
            error = json.dumps({"error":"Invalid data sent, please sent json data"})
            return self.render_to_response(error, status=400)
        old_data = json.loads(request.body)
        form = UpdateForm(old_data, instance=obj)
        if form.is_valid():
            data = form.save()
            new_data = data.serialize()           
        return self.render_to_response(new_data, status=201)
        if form.errors:
            error = json.dumps(form.errors)
            return self.render_to_response(error, status=400)
        json_data = json.dumps({"content":"yeah it submited"})
        return self.render_to_response(json_data, status=201)

    def delete(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error = json.dumps({"error":"Invalid data sent, please sent json data"})
            return self.render_to_response(error, status=400)
        old_data = json.loads(request.body)
        pass_id = old_data.get("id", None) 
        if not pass_id:
            response = {"id":"This is required to update an item"}
            error = json.dumps(response)
            return self.render_to_response(error, status=400)     
        obj = self.get_data(id=pass_id)
        if obj is None:
            data = json.dumps({"error":"Object is not find"})
            return self.render_to_response(data, status=403)
        obj.delete()
        data = {"sucess": "data deleted succesfully"}
        res = json.dumps(data)
        return self.render_to_response(res, status=200)

    
  
    
   
    