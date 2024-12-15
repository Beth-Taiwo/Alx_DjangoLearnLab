from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, generics, permissions, status
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .models import Post, Comment, Like
from django_filters import rest_framework as r_filters
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from notifications.models import Notification
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, r_filters.DjangoFilterBackend]
    search_fields = ['author__username', 'title', 'content']
    ordering_fields = ['title']
    filterset_fields = ['created_at']
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        if Like.objects.filter(post=post, user=user).exists():
            return Response({'detail': 'You already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        like = Like.objects.create(post=post, user=user)

        # Create a notification
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked',
            target=post
        )

        return Response({'status': 'post liked'}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        like = Like.objects.filter(post=post, user=user).first()
        if not like:
            return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()

        return Response({'status': 'post unliked'}, status=status.HTTP_204_NO_CONTENT)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class  = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')