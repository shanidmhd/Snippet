from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.db import transaction
import sys, os
from django.contrib.auth import authenticate, login
import requests
import json
from user_login.models import UserDetails,SessionHandler

# Create your views here.
class loginCheck(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        try :
            """Log in API"""
            str_username= request.data['str_username']
            str_password=request.data['str_password']
            user = authenticate(request, username=str_username, password=str_password)
            if user:
                login(request, user)
                token_json = requests.post(request.scheme+'://'+request.get_host()+'/api-token-auth/',{'username':str_username,'password':str_password})
                token = json.loads(token_json._content.decode("utf-8"))['token']
                rst_user = UserDetails.objects.filter(user_ptr_id=request.user.id).values('user_ptr_id','first_name','last_name')
                if user.is_staff:
                    str_name='Super User'
                else:
                    str_name = rst_user[0]['first_name'] +" "+rst_user[0]['last_name']
                email = user.email or ''
                userdetails={'Name':str_name,'email':email}
                SessionHandler.objects.filter(fk_user_id = user.id).delete()
                SessionHandler.objects.create(vchr_session_key = request.session.session_key,fk_user_id = user.id)

                return Response({'status':1,'token':token,'userdetails':userdetails,"str_session_key":request.session.session_key})
            else:
                return Response({'status':0,'reason':'No user'})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({'status':0,'reason':str(e)+ ' in Line No: '+str(exc_tb.tb_lineno)})

class UserRegistration(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        """Get all users"""
        rst_user = UserDetails.objects.all()
        return Response({'status':1,'data':rst_user})

    def post(self,request):
        try:
            """Register a user"""
            with transaction.atomic():
                rst_user_exists = UserDetails.objects.filter(username = request.data.get('strUserName'))
                if not rst_user_exists:
                    rst_user_details = UserDetails(username = request.data.get('strUserName'),
                                                    email = request.data.get('strEmail'),
                                                    vchr_name = request.data.get('strName'),
                                                    dat_dob = request.data.get('datDob'),
                                                    bint_phone = request.data.get('intPhno'),
                                                    is_active = True
                                                    )

                    rst_user_details.set_password(request.data.get('strPassWord'))
                    rst_user_details.save()
                    return Response({'status':1,'data':"Success"})
                else:
                    return Response({'status':0,"data":"Username Allready Exists"})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({'status':0,'reason':str(e)+ ' in Line No: '+str(exc_tb.tb_lineno)})
