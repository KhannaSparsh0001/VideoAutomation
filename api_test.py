from google import genai
from os import system
from keys import API_KEY

client = genai.Client(api_key=API_KEY)
"""
response = client.models.generate_content(
    model="gemini-2.5-pro",
    question=""
)
"""
num = int(input("How many questions ya wanna ask: \n>"))

for i in range(num):
    # for clearing up the previous convos

    if i % 5 == 0:
        system('cls')

    
    ques = input("Your question will be asked to gemini 2.5 pro model: \n>")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=ques,
    )

    print(response.text)


print("The program execution has been annihilated.".upper())


"""
Report:
api testing is complete
now rag based system nd notes based promtps has to be done, previous state of developer was better since it was more open minded


"""