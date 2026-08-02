from openai import OpenAI

from config import settings


class GPTModels:
    def __init__(self, api_key, model=settings.models.name):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def run(
        self,
        prompt,
        system_prompt="Act as an assistant that extracts revelent information from resume.",
    ):
        response = self.client.responses.create(
            model=self.model,
            input=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return response.output_text
