from django.contrib import admin
from django.urls import path,include
from article import views   
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = "index"),
    path('about/',views.about,name = "about"),
    path('user/',include("user.urls")),
    path("articles/",include("article.urls"))
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)