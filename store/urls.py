from django.conf.urls import include, url
from django.contrib import admin
from store import settings
import social.apps.django_app.urls
import paypal.standard.ipn.urls

urlpatterns = [
               url(r'^admin/', admin.site.urls),
               url(r'', include('blog.urls')),
               url('', include(social.apps.django_app.urls, namespace='social')),
               url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
               url(r'^paypal/', include(paypal.standard.ipn.urls)),
               ]