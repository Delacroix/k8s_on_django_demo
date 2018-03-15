from django.shortcuts import render
from kubernetes import client, config


# Create your views here.
from . import models
from .forms import ServiceConfigForm


def index(request):
    pod_list = models.ListPods.pod_info
    return render(request, 'index.html', {'pod_list': pod_list})


def service_list(request):
    config.load_kube_config()
    service_list = models.ListService.service_info
    return render(request, 'service_list.html', {'service_list': service_list})


def deploy_list(request):
    deploy_list = models.CreateDeploy.deploy_list
    return render(request, 'deploy_list.html', {'deploy_list': deploy_list})


def new_service(request):
    if request.method != 'POST':
        form = ServiceConfigForm()
    else:
        form = ServiceConfigForm(request.POST)
        if form.is_valid():
            form.save()
