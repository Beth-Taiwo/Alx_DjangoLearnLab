from rest_framework import serializers
from .models import Post, Comment, Like


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post_comments = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='comment_detail')
    likes = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['title', 'content', 'author','post_comments', 'likes']

    def create(self, validated_data):
        obj = Post.objects.create(**validated_data)
        obj.author = validated_data.get('author')
        obj.save()
        return obj
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance
    
    def get_likes(self, obj):
        return obj.likes.count()
    
class CommentSerializer(serializers.ModelSerializer):
    comment_author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.id')
    post_title = serializers.SerializerMethodField('get_post_title')
    class Meta:
        model = Comment
        fields = ['content', 'comment_author', 'post', 'post_title']

    def create(self, validated_data):
        obj = Comment.objects.create(**validated_data)
        obj.save()
        return obj
    
    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        return instance
    
    def get_post_title(self, obj):
        return obj.post.title
    

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user']