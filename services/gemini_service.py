from groq import Groq


class GeminiService:

    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def generate_response(self, prompt):

        response = self.client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.7

        )

        return response.choices[0].message.content