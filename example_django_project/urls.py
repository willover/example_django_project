from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'example_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^passreset/$',auth_views.password_reset,name='forgot_password1'),
    url(r'^passresetdone/$',auth_views.password_reset_done,name='forgot_password2'),
    url(r'^passresetconfirm/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.password_reset_confirm,name='forgot_password3'),
    url(r'^passresetcomplete/$',auth_views.password_reset_complete,name='forgot_password4'),
    
    url(r'^password/change/$',auth_views.password_change,name='auth_password_change'),
    url(r'^password/change/done/$',auth_views.password_change_done,name='auth_password_change_done'),
]
