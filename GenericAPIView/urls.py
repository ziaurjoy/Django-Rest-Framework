from django.urls import path
from GenericAPIView.views import AdmissionAllApi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'admission', AdmissionAllApi, basename='admission')
urlpatterns = router.urls

# urlpatterns = [
#     path('api/Admission', AdmissionAllApi.as_view()),
# ]