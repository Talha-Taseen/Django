
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home.as_view(),name='home'),
    path('books/<slug:cat_slug>',views.home.as_view(),name='cat_slug'),
    path('Books/',include('Books.urls')),
    path('users/',include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)