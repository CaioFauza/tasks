from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from tasks.models import Task
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers

@csrf_exempt
def task(request, id=None):
    if(request.method == 'GET'):
        tasks = Task.objects.all()
        return HttpResponse(serializers.serialize('json', tasks), content_type='application/json')

    if(request.method == 'POST'):
        data = json.loads(request.body)
        task = Task.objects.create(**data)
        return HttpResponse(json.dumps({'Status': 'Success', 'Message': 'Task successfully created.', 'Id': task.pk}))

    if(request.method == 'PATCH'):
        data = json.loads(request.body)
        update = Task.objects.filter(pk=id).update(**data)
        if update == 0: return HttpResponseBadRequest(json.dumps({'Status': 'Error', 'Message': 'Invalid task provided.', 'Id': id}))
        return HttpResponse(json.dumps({'Status': 'Success', 'Message': 'Task successfully updated.', 'Id': id}))

    if(request.method == 'DELETE'):
        delete = Task.objects.filter(pk=id).delete()
        if delete[0] == 0: return HttpResponseBadRequest(json.dumps({'Status': 'Error', 'Message': 'Invalid task provided.', 'Id': id}))
        return HttpResponse(json.dumps({'Status': 'Success', 'Message': 'Task successfully deleted.', 'Id': id}))
