
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('', views.home_aut, name='home_aut'),
    path('category/<slug:category_slug>/', views.home, name='category_wise_post'),
    path('author_app/',include('author.urls')),
    path('categories_app/',include('categories.urls')),
    path('post_app/',include('post.urls')),
    path('payment_app/', include('payment.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)