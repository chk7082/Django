# 홈워크_db_08_hw02_P.py
# serializers.py
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)