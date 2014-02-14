from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('login.views',
                       # Examples:
                       # url(r'^$', 'myapps.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', 'index'),
                       url(r'^add/$', 'add'),
                   )

urlpatterns += patterns('',
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^login/$', 'login.views.index'),
                        url(r'^login/add/$', 'login.views.add')
                    )
