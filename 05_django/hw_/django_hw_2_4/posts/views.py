from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer

@api_view(['GET', 'POST'])
def post_list_create(request):
    if request.method == 'GET':
        qs = Post.objects.all().order_by('-created_at')
        return Response(
            {"count": qs.count(), "results": PostSerializer(qs, many=True).data},
            status=status.HTTP_200_OK,
        )
    ser = PostSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response({"message": "게시글이 생성되었습니다.", "data": ser.data},
                        status=status.HTTP_201_CREATED)
    return Response({"message": "유효성 검사 실패", "errors": ser.errors},
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':
        return Response({"data": PostSerializer(post).data}, status=status.HTTP_200_OK)

    if request.method in ['PUT', 'PATCH']:
        ser = PostSerializer(post, data=request.data, partial=(request.method == 'PATCH'))
        if ser.is_valid():
            ser.save()
            return Response({"message": "게시글이 수정되었습니다.", "data": ser.data},
                            status=status.HTTP_200_OK)
        return Response({"message": "유효성 검사 실패", "errors": ser.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
