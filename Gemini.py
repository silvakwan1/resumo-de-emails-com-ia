from google import genai

class Gemini:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def resumir_email(self, email):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Resuma o seguinte email: {email}",
        )
        return response.text

