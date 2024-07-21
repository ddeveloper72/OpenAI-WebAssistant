"""This module contains the views for the assistant app."""
from django.shortcuts import render
from openai import OpenAIError

from assistant.engine import chatgpt


def home(request):
    """This function renders the home page of the assistant app."""
    try:

        if request.method == 'POST':
            chats = chatgpt(request)
            context = {
                'prompt': chats['prompt'],
                'response': chats['response'],       
                }
           
            return render(request, 'assistant/home.html', context)
        return render(request, 'assistant/home.html' )
    
    except OpenAIError as e:
        # This block of code handles OpenAI API errors.
        error_message = f"OpenAI API Error: {e}"
        return render(request, 'assistant/error.html', {'error_message': error_message})
    

def error_handler(request):
    """This function renders the error page of the assistant app."""
    return render(request, 'assistant/error.html')