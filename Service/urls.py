#coding:utf-8
#@Author    :   Nicky

from django.conf.urls import include, url
from Service.views import server,AjaxService,ServerList_ajax,getConnect,gateValid


urlpatterns = [
        url(r'^$', server),
        url(r'^(?P<page>\d+)', server),
        url(r'^ajax_server/$', AjaxService),
        url(r'^ajax_server/(?P<page>\d+)/$', AjaxService),
        url(r'^sj/$', ServerList_ajax),
        url(r'^getConnect/$', getConnect),
        url(r"^gateValid/$", gateValid),

]