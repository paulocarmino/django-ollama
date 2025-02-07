from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PromptSerializer
from .services.ollama_service import OllamaService


class GenerateResponseView(APIView):
    """
    API endpoint that allows users to get responses from the Ollama model.
    """

    def post(self, request):
        """
        Generate a response from the Ollama model.
        """
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            ollama_service = OllamaService()
            try:
                response = ollama_service.generate_response(
                    serializer.validated_data["prompt"]
                )
                return Response(response, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(
                    {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
