from django.conf.urls import include, url
from django.contrib import admin
from store import settings
urlpatterns = [
               url(r'^admin/', admin.site.urls),
               url(r'', include('blog.urls')),

               url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
               ]