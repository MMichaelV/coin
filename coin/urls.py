from django.conf.urls import url
from . import views

#app_name = 'coin'  # if is need, may be related to url throw ex.'coin:detail'
urlpatterns = [
    url(r'^$', views.CoinIndexView.as_view(), name='index'),
    url(r'^detail/(?P<pk>\w+)/$', views.CoinDetailView.as_view(), name='detail'),
    url(r'^update_list/$', views.CoinUpdateView.as_view(), name='update_list'),
    url(r'^edit/(?P<pk>\w+)/$', views.CoinEdit.as_view(), name='edit')
]