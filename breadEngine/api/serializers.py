from rest_framework import serializers

from breadEngine.models import Post, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 'user_id', 'content', 'username', 'created_at', 'num_likes', 'num_dislikes'
        )
