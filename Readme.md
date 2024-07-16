# OpenAI Web Assistant Demonstration

## Demonstration
This Django application is based on a excellent blog published by Jonathan Okah on [finxter](https://blog.finxter.com/how-i-built-an-openai-powered-web-assistant-with-django/)

![Sample Chat](https://github.com/ddeveloper72/OpenAI-WebAssistant/blob/main/images/2024-07-16_002726.png "Sample Chat")

During the process of re-creating the app, I've had to make some modifications so that it would continue to work with OpenAI.

The changes made were as follows:
- `from openai import OpenAI` referencing the [openAI docs](https://platform.openai.com/docs/quickstart)
- Where I had ChatCompletionMessage appear before and after the responses, I found a solution to specify just the content of the response `response.choices[0].message.content`
- The current OpenAI create model also requires messages as as on of the parameters:

```python
    response = client.chat.completions.create(
            model='gpt-3.5-turbo',
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

![Sample Error](https://github.com/ddeveloper72/OpenAI-WebAssistant/blob/main/images/2024-07-16_011015.png "Sample Error")