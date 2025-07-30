from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import LoginAPIView,generate_otp,FilterAPIView,SignupAPIview,UserAPIview,CandidateAPIView,RecruiterAPIView,AdminAPIView
urlpatterns = [
    path('users/',UserAPIview.as_view()),
    path('candidate/',CandidateAPIView.as_view()),
    path('recruiter/',RecruiterAPIView.as_view()),
    path('admin/',AdminAPIView.as_view()),
    path('login/',LoginAPIView.as_view()),
    path('signup/',SignupAPIview.as_view()),
    path('generate_otp/',generate_otp),
    path('filter_by/',FilterAPIView.as_view()),
    
]
# ✅ Only in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)