# 홈워크_db_08_hw02_P.py
# views.py

@api_view(['POST'])
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)