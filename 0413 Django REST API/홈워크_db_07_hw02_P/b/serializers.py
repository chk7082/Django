# b- serializers.py

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comment_set')