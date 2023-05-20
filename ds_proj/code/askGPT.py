import openai
openai.api_key = "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"

def prompt(text):
    prompt = text
    model = "text-davinci-002"  # this is the model used for generating text
    response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1024, temperature=0.5, format="text")
    info = response.choices[0].text.strip()
    return info
