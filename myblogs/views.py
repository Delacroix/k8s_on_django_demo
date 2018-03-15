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


def deploy_list(request):
    deploy_list = models.CreateDeploy.deploy_list
    return render(request, 'deploy_list.html', {'deploy_list': deploy_list})


def new_service(request):
    config.load_kube_config()
    api_instance = client.CoreV1Api()
    service = client.V1Service()
    service.api_version = "v1"
    service.kind = "Service"
    service.metadata = client.V1ObjectMeta(name='my-service')
    spec = client.V1ServiceSpec()
    spec.selector = {"app": 'MyApps'}
    spec.ports = [client.V1ServicePort(protocol='TCP',
                                       port='80',
                                       target_port='8080')]
    service.spec = spec
    api_instance.create_namespaced_service(namespace="default", body=service)
