import openai

my_openai.api_key = "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"
models = my_openai.Model.list()
print(models)




def generate_completion(prompt, model="text-davinci-002", temperature=0.5, max_tokens=50):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()







# import openai

# API_KEY = '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'
# openai.api_key = API_KEY

# model = 'text-davinci-003'

# response = openai.Completion.create(
#   engine=model,
#   prompt='How big is the moon',
# )

# print(response.choices[0].text)
