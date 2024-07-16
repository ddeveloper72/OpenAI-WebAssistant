""" engine.py is a file that contains the model function
that takes the user input and returns the chatbot response. """
from openai import OpenAI
from webassistant.settings import env

# Import OpenAI API_KEY from the .env file and 
# create an instance of the OpenAI class with the API_KEY.

OPENAI_API_KEY = env('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

def chatgpt(request):
    """ This function takes the user input and returns the chatbot response. """
    prompt = request.POST.get('prompt')
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=1000
    )
    response = response.choices[0].message.content

    chats = {
        'prompt': prompt,
        'response': response
    }

    print(chats)
    return chats
