from django.shortcuts import render
from kubernetes import client, config
# Create your views here.
from . import models


def index(request):
    pod_list = models.ListPods.pod_info
    return render(request, 'index.html', {'pod_list': pod_list})


def create_service(request):
    config.load_kube_config()
    api_instance = client.CoreV1Api()
    service = client.V1Service()
    service.api_version = "v1"
    service.kind = "Service"
    service.metadata = client.V1ObjectMeta(name=models.CreateService.svc_name)
    spec = client.V1ServiceSpec()
    spec.selector = {"app": models.CreateService.svc_spec_selector}
    spec.ports = [client.V1ServicePort(protocol=models.CreateService.svc_protocol,
                                       port=models.CreateService.svc_port,
                                       target_port=models.CreateService.svc_target_port)]
    service.spec = spec
    api_instance.create_namespaced_service(namespace="default", body=service)
    service_list = models.CreateService.service_info
    return render(request, 'create_svc.html', {'service_list': service_list})
