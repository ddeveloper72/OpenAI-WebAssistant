# OpenAI Web Assistant Demonstration

## Introduction

This Django application is based on a excellent blog published by Jonathan Okah on [finxter](https://blog.finxter.com/how-i-built-an-openai-powered-web-assistant-with-django/)

![Sample Chat being read back](https://github.com/ddeveloper72/OpenAI-WebAssistant/blob/main/images/2024-07-28_142604.png 'Sample Chat being read back')

### Setting up the OpenAI API_key in .env secrets

At the time of writing this document, I discovered that I needed to create a new OpenAI project API_Key. I also needed to setup a pay-as-you-go plan (since I'd run out of free credits as a new user) which provides me with credits to use the API service.  Once they run out, it's up to me to decide if I'd like to topup again. I was able to top-up by $5 and leave the auto-topup turned off. This should be plenty for anyone wanting to do something similar, so that they can experiment with connecting to the OpenAI API.

In order to use the API_Key in Django, I used [Django-environ](https://pypi.org/project/django-environ/). They provide excellent information published on how to setup your `.env` file in your project environment, where the API_key can then be imported by your settings.py file. From here the key can be made available to your component by importing it from your settings file. Remember, that API_Keys need to be kept secret, so ensure that this .env file is added to your `.gitignore` file. There is a very real risk of an API_key being copied from ones repository and then discovering tat your OpenAPI credits are being used up by someone else.

Another reminder, is that when setting up your `.env` file, ensure that it is in the same directory as your project `settings.py` file.

During the process of re-creating the app, I've had to make some modifications so that it would continue to work with OpenAI.

### Importing OpenAI API_Key to the component App

Here is sample code, used in this project. The .env file settings is made available to all components apps, using this method.
This is a matter of preference. Once could import the `.env` directly to the component app, rather than to the settings file.

```python
from webassistant.settings import env

# Import OpenAI API_KEY from the .env file and
# create an instance of the OpenAI class with the API_KEY.

OPENAI_API_KEY = env('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

```

The changes made were as follows:

- `from openai import OpenAI` referencing the [openAI docs](https://platform.openai.com/docs/quickstart)
- Where I had ChatCompletionMessage appear before and after the responses, I found a solution to specify just the content of the response `response.choices[0].message.content`
- The current OpenAI create model also requires messages as as on of the parameters:

```python
    stream = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=1000
        )
```

The error message was also updated to show the OpenAI error code whish is rendered in the html markup:

```python
    except OpenAIError as e:
            # This block of code handles OpenAI API errors.
            error_message = f"OpenAI API Error: {e}"
            return render(request, 'assistant/error.html', {
                'error_message': error_message})

```

![Sample Network Error](https://github.com/ddeveloper72/OpenAI-WebAssistant/blob/main/images/2024-07-16_011526.png 'Sample Network Error')
Image showing a Sample Network Error

![Sample Key Error](https://github.com/ddeveloper72/OpenAI-WebAssistant/blob/main/images/2024-07-16_011015.png 'Sample Key Error')
Image showing a sample Key Error

### Where things change

The longer I spent on working with this project, the more I've begun to enjoy it even more.  I made some changes that would then use speech synthesis to read back any text provided in the response out aloud.  I also added a toggle button to start/stop the speech synthesis as well as a custom alert to provide a visual indication (for 10s) that the text is being read out aloud.

Next, I added markdown to my project which I thought might improve the look of the responses.  What I was really trying to do though, was find away by using markdown to render any code snippets, like the ones above, to look like they've been styled in my code editor.

Lastly, I added a clear button, so one can clear the prompt as well as any response that may be in the window.

### Next steps

I plan to reproduce this app, or similar in a new framework and stack that I've never used before,  [Blazor](https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps/blazor) which leverages .NET and C#.  I then want to use the AI to search and work with specific datasets so that the responses will be specialized in specific subjects.
