from django.urls import path

from . import views
from .views import PostViewSet,like_post, input_image 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ListPost.as_view()),
    path('<int:pk>/', views.DetailPost.as_view()),
    path('like/<int:pk>/',like_post,name='like_post'),
    path('input_image',input_image,name='input_image')
]# + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

