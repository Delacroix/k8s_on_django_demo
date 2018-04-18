"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path
from . import views

app_name = 'myblogs'

urlpatterns = [
    re_path(r'^$', views.index, name="pod_list"),
    re_path(r'^service_list/$', views.service_list, name="service_list"),
    re_path(r'^deploy_list/$', views.deploy_list, name="deploy_list"),
    re_path(r'^new_deploy/$', views.new_deploy, name="new_deploy"),
    re_path(r'^new_svc_form/$', views.new_svc, name="new_svc"),
    re_path(r'^new_deploy_form/$', views.new_deploy, name="new_deploy"),
    re_path(r'^chart_repo_list/$', views.chart_repo_list, name="chart_repo_list"),
    re_path(r'^svc_list/$', views.svc_list, name="svc_list"),
]
