"""This module contains the views for the assistant app."""
import markdown2
from django.shortcuts import render
from openai import OpenAIError

from assistant.engine import chatgpt


def home(request):
    """This function renders the home page of the assistant app."""
    try:
        # Sample Markdown text
        markdown_text = """
        # Welcome to the Assistant App

        This app allows you to interact with an AI assistant.

        ## Features

        - Chat with the AI
        - Get responses to your queries
        - Enjoy a user-friendly interface

        **Note:** Make sure to check the documentation for more details.
        """

        html_content = markdown2.markdown(markdown_text)

        if request.method == 'POST':
            chats = chatgpt(request)
            context = {
                'prompt': chats['prompt'],
                'response': chats['response'],
                'html_content': html_content,
            }

            return render(request, 'assistant/home.html', context)

        context = {
            'html_content': html_content,
        }
        return render(request, 'assistant/home.html', context)

    except OpenAIError as e:
        # This block of code handles OpenAI API errors.
        error_message = f"OpenAI API Error: {e}"
        return render(request, 'assistant/error.html', {'error_message': error_message})

def error_handler(request):
    """This function renders the error page of the assistant app."""
    return render(request, 'assistant/error.html')
