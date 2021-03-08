

from django.urls import path
from ClassBasedAPI import views
urlpatterns = [
    path('api/persion/create', views.PersionCreate.as_view()),
    path('api/persion/list', views.PersionList.as_view()),
    path('api/persion/update/<int:id>', views.PersionUpdate.as_view()),
    
]