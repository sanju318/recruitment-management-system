from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import login,generate_otp,filter_by,SignupAPIview,UserAPIview
urlpatterns = [
    path('user/',UserAPIview.as_view()),
    path('login/',login),
    path('signup/',SignupAPIview.as_view()),
    path('generate_otp/',generate_otp),
    path('filter_by/',filter_by),
    
]
# ✅ Only in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)