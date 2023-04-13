# c- serializers.py
class ArticleSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comment_count',)


