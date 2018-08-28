from django.shortcuts import render
from kubernetes import client, config
from django.http import HttpResponse
import urllib3
import json
import requests


# Create your views here.
from . import models
from .forms import ServiceForm
from .forms import DeployForm


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
                                       port=80,
                                       target_port=8080)]
    service.spec = spec
    api_instance.create_namespaced_service(namespace="default", body=service)
    service_list = models.ListService.service_info
    return render(request, 'service_list.html', {'service_list': service_list})


def new_deploy(request):
    if request.method == 'POST':

        deploy_form = DeployForm(request.POST)

        config.load_kube_config()
        extension = client.ExtensionsV1beta1Api()
        deployment = client.ExtensionsV1beta1Deployment()

        if deploy_form.is_valid():
            deployment.api_version = "extentions/v1beta1"
            deployment.kind = "Deployment"
            deployment.metadata = client.V1ObjectMeta(name=str(deploy_form.cleaned_data['deploy_name']))
# TO BE DONE 20180316
            spec = client.ExtensionsV1beta1DeploymentSpec()
            spec.replicas = int(deploy_form.cleaned_data['deploy_replicas'])

            spec.template = client.V1PodTemplateSpec()
            spec.template.metadata = client.V1ObjectMeta(labels={"app": str(deploy_form.cleaned_data['deploy_label_app'])})
            spec.template.spec = client.V1PodSpec()

            container = client.V1Container()
            container.name = str(deploy_form.cleaned_data['deploy_image_name'])
            container.image = str(deploy_form.cleaned_data['deploy_image_version'])
            container.ports = [client.V1ContainerPort(container_port=int(deploy_form.cleaned_data['deploy_container_port']))]

            spec.template.spec.containers = [container]
            deployment.spec = spec

            extension.create_namespaced_deployment(namespace=str(deploy_form.cleaned_data['deploy_namespace']), body=deployment)
    else:
        deploy_form = DeployForm()
    return render(request, 'new_deploy_form.html', {'deploy_form': deploy_form})


def new_svc(request):
    # 提交表单创建K8S Service
    if request.method == 'POST':

        form = ServiceForm(request.POST)

        config.load_kube_config()
        api_instance = client.CoreV1Api()

        if form.is_valid():

            service = client.V1Service()
            service.api_version = "v1"
            service.kind = "Service"
            service.metadata = client.V1ObjectMeta(name=str(form.cleaned_data['service_name']))
            spec = client.V1ServiceSpec()
            spec.selector = {"app": str(form.cleaned_data['service_spec_selector'])}
            spec.ports = [client.V1ServicePort(protocol=str(form.cleaned_data['service_protocol']),
                                               port=int(form.cleaned_data['service_port']),
                                               target_port=int(form.cleaned_data['service_target_port']))]
            service.spec = spec
            api_instance.create_namespaced_service(namespace="default", body=service)
            return HttpResponse('New Service created success!')
    else:
        form = ServiceForm()
    return render(request, 'new_svc_form.html', {'form': form})


def chart_repo_list(request):
    http = urllib3.PoolManager()
    req = http.request('GET', 'http://local.k8snode1.com:8080/api/charts')
    res = req.data
    chart_repo_list = json.loads(res)
    for key, value in chart_repo_list.items():
        for v in value:
            repo_list = v['urls']
            return render(request, 'chart_repo_list.html', {'chart_repo_list': repo_list})


def svc_list(request):
    svc_list_url = 'https://local.k8stest.com:8443/api/v1/services'
    req = requests.get(svc_list_url, auth=('admin', 'abcd1234'), verify=False)
    res = req.content
    svc_list = json.loads(res)

    return render(request, 'svc_list.html', {'svc_list': svc_list})
