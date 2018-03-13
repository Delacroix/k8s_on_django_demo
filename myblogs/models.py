from django.db import models
from kubernetes import client, config
# Create your models here.


class ListPods():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    pod_info = v1.list_pod_for_all_namespaces(watch=False)

    def __str__(self):
        return self.pod_info


class CreateService(models.Model):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    service_info = v1.list_service_for_all_namespaces()
    svc_name = models.CharField(max_length=32, default='my-service')
    svc_protocol = models.CharField(max_length=32, default='TCP')
    svc_spec_selector = models.CharField(max_length=32)
    svc_port = models.CharField(max_length=32)
    svc_target_port = models.CharField(max_length=32)

    def __str__(self):
        return self.service_info
