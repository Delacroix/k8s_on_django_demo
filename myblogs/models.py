from django.db import models
from kubernetes import client, config
# Create your models here.


class ListPods():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    pod_info = v1.list_pod_for_all_namespaces(watch=False)

    def __str__(self):
        return self.pod_info


class ListService(models.Model):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    service_info = v1.list_service_for_all_namespaces(watch=False)

    def __str__(self):
        return self.service_info


class ServiceConfig(models.Model):
    config.load_kube_config()
    v1 = client.CoreV1Api()

    def __init__(self, svc_name, svc_protocol, svc_spec_selector, svc_port, svc_target_port):
        self.svc_name = svc_name
        self.svc_protocol = svc_protocol
        self.svc_spec_selector = svc_spec_selector
        self.svc_port = svc_port
        self.svc_target_port = svc_target_port

    def svc_config(self):
        self.svc_name = models.CharField(max_length=32, default='my-service')
        self.svc_protocol = models.CharField(max_length=32, default='TCP')
        self.svc_spec_selector = models.CharField(max_length=32, default='MyApps')
        self.svc_port = models.CharField(max_length=32)
        self.svc_target_port = models.CharField(max_length=32)

    def __str__(self):
        return self.svc_name


class CreateDeploy(models.Model):
    config.load_kube_config()
    extension = client.ExtensionsV1beta1Api()
    deployment = client.ExtensionsV1beta1Deployment()
    deployment.api_version = "extentions/v1beta1"
    deployment.kind = "Deployment"
    pass
