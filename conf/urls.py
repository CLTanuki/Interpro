__author__ = 'cltanuki'
from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from . import views, api

router = DefaultRouter()
router.register(r'report', api.ReportViewset)

urlpatterns = patterns('',
    url(r'^$', views.ConfIndex.as_view(), name='conf_index'),
    url(r'^(?P<slug>.+)/$', views.ConfMain.as_view(), name='conf_main'),
    # url(r'^(?P<slug>.+)/', include(item_patterns)),
)
# urlpatterns += i18n_patterns('',
#     url(_(r'^about/$'), about_views.main, name='about'),
#     url(_(r'^news/'), include(news_patterns, namespace='news')),
# )

urlpatterns += router.urls