from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Recruiterview,signup,login,generate_otp
urlpatterns = [
    path('login/',login),
    path('signup/',signup),
    path('generate_otp/',generate_otp),
    
]
# ✅ Only in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)