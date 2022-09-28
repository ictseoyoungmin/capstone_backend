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
    
#_______________________________________________________

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.decorators import api_view,permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

#from users.models import Profile
from .serializers import PostSerializer#,PostCresteSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_feilds = ['author','likes']
    
    def get_serializer_class(self):
        if self.action == 'list' or 'reterive':
            return PostSerializer
        return PostSerializer #PostCresteSerializer
    
    def perform_create(self, serializer):
        serializer.save(author = self.request.user, profile=None)
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user) 
    else:
        post.likes.add(request.user)
        
    return Response({'status':'ok'})   
    
    