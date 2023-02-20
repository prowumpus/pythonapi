import openai

openai.api_key = "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"
models = openai.Model.list()
print(models)



curl https://api.openai.com/v1/completions \
-H "Content-Type: application/json" \
-H "Authorization: "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" \
-d '{"model": "text-davinci-003", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 7}'





# import openai

# API_KEY = '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'
# openai.api_key = API_KEY

# model = 'text-davinci-003'

# response = openai.Completion.create(
#   engine=model,
#   prompt='How big is the moon',
# )

# print(response.choices[0].text)
