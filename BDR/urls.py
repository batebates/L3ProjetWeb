from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', include('core.urls')),
    url(r'^room/', include('room.urls')),
]
