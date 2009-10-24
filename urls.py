from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	(r'^admin/(.*)', admin.site.root),
	url(r'^$', 'vaccines.views.index', name="swineflu-index"),
	url(r'^download/xls/$', 'vaccines.views.xls', name="swineflu-download-xls"),

)
	








