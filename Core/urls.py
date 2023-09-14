from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Basic_Query.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')), ## For Ck-editor, It is not a app.
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)