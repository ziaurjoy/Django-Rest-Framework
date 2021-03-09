from django.urls import path
from rest_framework import routers
from viewsetcreate import views

router = routers.DefaultRouter()
router.register(r'detailslist', views.PersionDetailsViewSet)
urlpatterns = router.urls


