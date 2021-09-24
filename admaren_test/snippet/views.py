from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import traceback
import sys, os
from snippet.models import *
from datetime import datetime
from django.contrib.auth.models import User
from django.db import transaction
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
# Create your views here.

class snippetAPI(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        try:
            """Detail API"""
            snippet_id = request.GET.get('snippetId')
            rst_snippet = Snippet.objects.filter(pk_bint_id = int(snippet_id)).values('pk_bint_id','vchr_content','fk_created_by_id','fk_created_by_id__first_name','fk_created_by_id__last_name','dat_created','fk_tag_id','fk_tag_id__vchr_title').first()
            return Response({'status':1,'data':rst_snippet})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({'status':0,'reason':str(e)+ ' in Line No: '+str(exc_tb.tb_lineno)})

    def post(self,request):
        try:
            """Create API"""
            with transaction.atomic():
                vchr_content = request.data.get('strContent')
                vchr_title = request.data.get('strTitle')
                ins_tag = Tag.objects.filter(vchr_title__iexact = vchr_title).values('pk_bint_id').first()
                if not ins_tag:
                    rst_tag = Tag(vchr_title = vchr_title)
                    rst_tag.save()
                    int_tag_id  = rst_tag.pk_bint_id
                else:
                    int_tag_id = ins_tag['pk_bint_id']
                rst_snippet = Snippet(vchr_content = vchr_content,fk_tag_id  = int_tag_id , fk_created_by_id = request.user.id , dat_created = datetime.now())
                rst_snippet.save()
                return Response({'status':0,'data':'Success'})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({'status':0,'reason':str(e)+ ' in Line No: '+str(exc_tb.tb_lineno)})

    def put(self,request):
            try:
                """Update API"""
                with transaction.atomic():
                    snippet_id = request.GET.get('snippetId')
                    vchr_content = request.data.get('strContent')
                    vchr_title = request.data.get('strTitle')
                    ins_tag = Tag.objects.filter(vchr_title__iexact = vchr_title).values('pk_bint_id').first()
                    if not ins_tag:
                        rst_tag = Tag(vchr_title = vchr_title)
                        rst_tag.save()
                        int_tag_id  = rst_tag.pk_bint_id
                    else:
                        int_tag_id = ins_tag['pk_bint_id']
                    Snippet.objects.filter(pk_bint_id = int(snippet_id)).update(vchr_content = vchr_content,fk_tag_id  = int_tag_id , fk_created_by_id = request.user.id , dat_created = datetime.now())
                    rst_snippet = Snippet.objects.filter(pk_bint_id = int(snippet_id)).values('pk_bint_id','vchr_content','fk_created_by_id','fk_created_by_id__first_name','fk_created_by_id__last_name','dat_created','fk_tag_id','fk_tag_id__vchr_title').first()
                    return Response({'status':1,'data':rst_snippet})
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                return Response({'status':0,'reason':str(e)+ ' in Line No: '+str(exc_tb.tb_lineno)})

    def delete(self,request):
            try:
                """Delete API"""
                snippet_id = request.GET.get('snippetId')
                Snippet.objects.filter(pk_bint_id = int(snippet_id)).delete()
                return Response({'status':1,'data':'Success'})
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                return Response({'status':0,'reason':str(e)+ ' in Line No: '+str(exc_tb.tb_lineno)})

class tagAPI(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        try:
            """Tag List API"""
            rst_tag = list(Tag.objects.all())
            return Response({'status':1,'data':rst_tag})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({'status':0,'reason':str(e)+ ' in Line No: '+str(exc_tb.tb_lineno)})

class tagDetailAPI(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        try:
            """Tag Detail API"""
            tagId = request.GET.get('snippetId')
            rst_snippet = Snippet.objects.filter(fk_tag_id = int(tagId)).values('pk_bint_id','vchr_content','fk_created_by_id','fk_created_by_id__first_name','fk_created_by_id__last_name','dat_created','fk_tag_id','fk_tag_id__vchr_title').first()
            return Response({'status':1,'data':rst_snippet})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({'status':0,'reason':str(e)+ ' in Line No: '+str(exc_tb.tb_lineno)})

class overallAPI(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        try:
            """Overview API"""
            rst_snippet = Snippet.objects.all()
            int_count = Snippet.objects.count()
            return Response({'status':1,'data':rst_snippet,'count':int_count})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({'status':0,'reason':str(e)+ ' in Line No: '+str(exc_tb.tb_lineno)})
