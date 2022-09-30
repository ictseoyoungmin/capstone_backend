from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ListPost.as_view()),
    path('<int:pk>/', views.DetailPost.as_view()),
    path('upload/',views.model_form_upload,name='upload'),
    path('upload/image/',views.user_image_upload,name='upload_image')
]# + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

