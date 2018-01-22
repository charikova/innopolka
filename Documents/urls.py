from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #documents/<doc_id>
    url(r'^(\d+)/$', views.show_doc_inf, name='show_doc_inf'),


]
