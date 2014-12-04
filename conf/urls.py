__author__ = 'cltanuki'
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from erp.enterprise.views import Register
from . import views

item_patterns = patterns('',
    url(r'^/$', views.ConfMain.as_view(), name='conf_main'),
    url(r'^/register$', Register.as_view(template_name='conf/register.html'), name='conf_main'),
)

urlpatterns = patterns('',
    url(r'^(?P<slug>.+)/$', views.ConfMain.as_view(), name='conf_main'),
    url(r'^(?P<slug>.+)/', include(item_patterns)),
)
# urlpatterns += i18n_patterns('',
#     url(_(r'^about/$'), about_views.main, name='about'),
#     url(_(r'^news/'), include(news_patterns, namespace='news')),
# )