from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .models import UserInformation,Role,JobPost,InterviewScheduling,CandidateStatus

@api_view(["GET","POST"])
def Recruiterview(request):
    # method = request.method
    # if method == "GET":
    #     #data = UserInformation.objects.all()
    #     userdata = UserInformation.objects.all()
    #     stf  = []
    #     print(request.method)
    #     for i in userdata:
    #         l = {"name":i.username,"email":i.email} #create dictionaty to show json data in postman
    #         stf.append(l)
    #     return Response(stf)
            return Response()

# Create your views here.
