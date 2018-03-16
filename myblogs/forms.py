from django import forms


class ServiceForm(forms.Form):
    service_name = forms.CharField()
    service_protocol = forms.CharField()
    service_spec_selector = forms.CharField()
    service_port = forms.CharField()
    service_target_port = forms.CharField()


class DeployForm(forms.Form):
    deploy_name = forms.CharField()
    deploy_label_app = forms.CharField()
    deploy_replicas = forms.CharField()
    deploy_image_name = forms.CharField()
    deploy_image_version = forms.CharField()
    deploy_container_port = forms.CharField()
    deploy_namespace = forms.CharField()
