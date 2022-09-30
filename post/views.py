from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer

class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
###########################################################
# https://jakpentest.tistory.com/77
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .forms import DocumentForm,ImageForm

# text only
@method_decorator(csrf_exempt, name="dispatch")
def model_form_upload(request):
    print('model_form_upload')
    if request.method == "POST":
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({"status": "Success"}))
        else:
            return HttpResponse(json.dumps({"status": "Failed"}))
        
# image only        
@method_decorator(csrf_exempt, name="dispatch")
def user_image_upload(request):
    print('user_image_upload')
    if request.method == "POST":
        form = ImageForm(request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({"status": "Success"}))
        else:
            return HttpResponse(json.dumps({"status": "Failed"}))        