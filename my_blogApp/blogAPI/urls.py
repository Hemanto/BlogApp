from  django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.BlogList.as_view()),
    path('<slug:slug>', views.BlogDetail.as_view(), name='each_blog_details')
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
