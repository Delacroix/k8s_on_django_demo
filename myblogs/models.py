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
    # deployment.api_version = "extentions/v1beta1"
    # deployment.kind = "Deployment"
    # deployment.metadata = client.V1ObjectMeta(name="nginx-deployment")
    #
    # spec = client.ExtensionsV1beta1DeploymentSpec()
    # spec.replicas = 3
    #
    # spec.template = client.V1PodTemplateSpec()
    # spec.template.metadata = client.V1ObjectMeta(labels={"app": "nginx"})
    # spec.template.spec = client.V1PodSpec()
    #
    # container = client.V1Container()
    # container.name = "nginx"
    # container.image = "nginx:1.7.9"
    # container.ports = [client.V1ContainerPort(container_port=80)]
    #
    # spec.template.spec.containers = [container]
    # deployment.spec = spec
    #
    # extension.create_namespaced_deployment(namespace="default", body=deployment)

    deploy_list = extension.list_deployment_for_all_namespaces(watch=False)

    def __str__(self):
        return self.deploy_list



