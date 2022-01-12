from rest_framework import generics, permissions
from .permissions import IsAuhtorOrReadOnly
from .models import Post 
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuhtorOrReadOnly,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer