import requests
from typing import Dict, Any


class OllamaService:
    def __init__(self):
        self.base_url = "http://localhost:7869"

    def generate_response(self, prompt: str) -> Dict[str, Any]:
        """
        Generate a response from Ollama model.

        Args:
            prompt (str): The input prompt for the model

        Returns:
            Dict[str, Any]: The response from the model
        """
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={"prompt": prompt, "model": "tinyllama", "stream": False},
            )
            response.raise_for_status()
            return {"response": response.json().get("response", "")}
        except requests.RequestException as e:
            raise Exception(f"Error communicating with Ollama: {str(e)}")
