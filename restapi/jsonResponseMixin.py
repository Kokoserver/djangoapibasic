from django.http import JsonResponse, HttpResponse


class HttpResponseMixin(object):
    def render_to_response(self, data, status):
        is_json = False
        content_type = "text/html"
        if is_json:
            content_type = "application/json"
        return HttpResponse(data, content_type=content_type, status=status)
class JsonMixin(object):
    def respond_json_data(self, context, *args, **kwargs):
        return JsonResponse(self.get_data(context))
    
    def get_data(self, context):
        return context