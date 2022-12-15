from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import User
from rest_framework.renderers import JSONRenderer
from .serializers import UserSerializers
from django.http import HttpResponse

# Create your views here.


@csrf_exempt
def user_api(request):
    if request.method == 'GET':
        stu = User.objects.all()
        serializer = UserSerializers(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='applicaiton/json')

    if request.method == 'POST':
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = UserSerializers(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer.render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
