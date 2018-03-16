from django.db import models

from kubernetes import client, config
from kubernetes.client.rest import ApiException
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


class NewService(models.Model):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    svc_name = models.CharField(max_length=32, default='my-service')
    svc_protocol = models.CharField(max_length=32, default='TCP')
    svc_spec_selector = models.CharField(max_length=32, default='MyApps')
    svc_port = models.CharField(max_length=32, default='80')
    svc_target_port = models.CharField(max_length=32, default='8080')
    svc_conf = [svc_name, svc_protocol, svc_spec_selector,
                svc_port, svc_target_port]

    def __str__(self):
        return self.svc_conf


class CreateDeploy(models.Model):
    config.load_kube_config()
    extension = client.ExtensionsV1beta1Api()
    deployment = client.ExtensionsV1beta1Deployment()

    deploy_list = extension.list_deployment_for_all_namespaces(watch=False)

    def __str__(self):
        return self.deploy_list



