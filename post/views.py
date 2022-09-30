from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer
from rest_framework import status

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
    

#_________________________________________________________

# 책보고 구현중 
@api_view(['GET'])
def input_image(request):
    if request.method == 'GET':     
        print('addddddddddddddddddddddddd')
    else:
        print('not get')    
    print()
    # 
    return render(request, '../../frontend/src/workout.html')#component/aside.js')


@api_view(['GET', 'POST'])
def students_list(request):
    if request.method == 'GET':
        data = Post.objects.all()

        serializer = PostSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        print('sadddddddddddddddddddddddddddd')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
