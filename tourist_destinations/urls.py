from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import DestinationList, DestinationDetail, home, destination_create, destination_update, destination_delete, collections

urlpatterns = [
    path('home/', home, name='home'),
    path('api/', DestinationList.as_view(), name='destination-list'),
    path('api/<int:pk>/', DestinationDetail.as_view(), name='destination-detail'),
    path('create/', destination_create, name='destination-create'),
    path('update/<int:pk>/', destination_update, name='destination-update'),
    path('delete/<int:pk>/', destination_delete, name='destination-delete'),
    path('colletion/', collections, name='colletion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
