from django.conf.urls import patterns, include, url

from crowdtask.views import UserProfile

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djask.views.home', name='home'),
    # url(r'^djask/', include('djask.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^$', 'crowdtask.views.apps_list'),
    (r'^account/login$', 'django.contrib.auth.views.login', {'template_name': 'login_form.html'}),
    (r'^account/create$', 'crowdtask.views.create_user'),
    (r'^profile$', UserProfile.as_view()),
    (r'^apps/', include('crowdtask.urls')),
)
