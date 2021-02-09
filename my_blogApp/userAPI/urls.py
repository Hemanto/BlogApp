from django.urls import path
from .views import UserDetailAPI, UserUpdateAPI
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # path('register/', UserCreateView.as_view(), name='register'),
    path('get_user/', UserDetailAPI.as_view(), name='get_user_details'),
    path('update_user/', UserUpdateAPI.as_view(), name='update_user_details'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)