import string
from fastapi import FastAPI
import openai

app = FastAPI()
openai.api_key = "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"

@app.get("/")
def fun():
    return "Hello world"

@app.get("/{data}")
def gpt3(data):  # type: ignore
    response=openai.Completion.create(
        model="davinci:ft-vnr-vignana-jyothi-institute-of-engineering-and-technology-2022-09-27-09-46-35",
        prompt="prompt: \nTake the following points and generate a professional paragraph: \n1) Developed \"E-complaint box\" - a mobile application to route complaints from rural areas to relevant departments.\n2) Used \"Web technologies\" and \"Android Studio\" to develop the backend of the application.\n3) Developed an \"E-vote\" mobile application to digitize student elections.\n4) Used two-factor authentication to eliminate electoral frauds. \ngeneration:\nAs part of the 36 Hours Rural development Hackathon conducted by JNTU, our team was tasked to develop an \"E-complaint box\" - a mobile application to route complaints from rural areas to relevant departments. I was able to comprehensively apply “Web technologies” and “Android Studio” skills that I learned in the 5th semester to develop the backend of the application flawlessly. The application also features a way to directly share complaints on social media. I also participated in a 24 hour Hackathon for the top 20 coders of our college to develop an \"E-vote\" mobile application to digitize student elections. I engineered a solution using two-factor authentication. To eliminate electoral frauds, especially vote tampering.\n\nprompt:\nTake the following points and generate a professional paragraph: "+data+"\ngeneration:\n",  # type: ignore
        temperature=0.65,
        max_tokens=500,
        top_p=1,
        best_of=3,
        frequency_penalty=0.05,
        presence_penalty=0.2,
        stop=["\n"]
    )
    return response.choices[0]['text']  # type: ignore