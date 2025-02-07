from rest_framework import serializers


class PromptSerializer(serializers.Serializer):
    prompt = serializers.CharField(
        required=True, help_text="The input prompt for the model"
    )


class ResponseSerializer(serializers.Serializer):
    response = serializers.CharField(help_text="The model's response")
