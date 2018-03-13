from django.shortcuts import render
from kubernetes import client, config
# Create your views here.
from . import models


def index(request):
    pod_list = models.ListPods.pod_info
    return render(request, 'index.html', {'pod_list': pod_list})


def service_list(request):
    config.load_kube_config()
    service_list = models.ListService.service_info
    return render(request, 'service_list.html', {'service_list': service_list})

