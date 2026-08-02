from config import settings
from resume.models.gpt import GPTModels


prompt = """
You are provided with an image file of a resume. Extract all the informations listed below: \

1. Full Name [first name, middlename (if any), last name]
2. Phone [country-code, phone number]
3. Email
4. Qualifications [Degree, Grade/Score, Certificates]
5. Work Experience [Role, Period(Years/Months), Organization]
6. Skills [Technical Skills, Soft Skills]
7. Projects
8. Publications [Research Papers, Books]

NOTE: Follow the above format and extract informastion if and only if available.

"""
api_key = settings.openai_api_key


model = GPTModels(api_key=api_key)
response = model.run(prompt=prompt)
print(response)
