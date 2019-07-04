from django.urls import path, include
from .views import homepage, document_upload


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', homepage, name='homepage'),
    path('upload/', document_upload, name='upload'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
