from django.urls import path
from movietickets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('movietickets/', views.booking_list.as_view()),
    path('movietickets/<int:pk>/', views.booking_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)