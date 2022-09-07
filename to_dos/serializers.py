from rest_framework.serializers import ModelSerializer

from .models import ToDo


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"
        read_only_fields = ["user", "completed"]


class ToDoCompletedStatusSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = ["completed"]
