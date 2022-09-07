from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response, status

from .models import ToDo
from .permissions import IsOwnerTodoPermission
from .serializers import ToDoCompletedStatusSerializer, ToDoSerializer


class ToDoView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ToDoListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

    def get_queryset(self):

        return ToDo.objects.filter(user=self.request.user)


class ToDoCompleteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerTodoPermission]

    def get(self, request: Request, to_do_id: str) -> Response:
        to_do = get_object_or_404(ToDo, id=to_do_id)
        self.check_object_permissions(request, to_do)
        data = {"completed": True}
        serializer = ToDoCompletedStatusSerializer(to_do, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerTodoPermission]
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    lookup_url_kwarg = "to_do_id"


# Create your views here.
