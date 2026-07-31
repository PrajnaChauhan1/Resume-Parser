from openai import OpenAI


class GPTModels:
    def __init__(self, api_key, model="gpt-5.5"):
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
                {"role": "developer", "content": "Talk like a pirate."},
                {
                    "role": "user",
                    "content": "How do I check if a Python object is an instance of a class?",
                },
            ],
        )

        return response.output_text
