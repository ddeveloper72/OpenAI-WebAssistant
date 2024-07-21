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
    stream = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=1000,
    )

    response = stream.choices[0].message.content

    # Prepare the chat information to return as JSON
    chats = {
        'prompt': prompt,
        'response': response,      
    }

    return chats