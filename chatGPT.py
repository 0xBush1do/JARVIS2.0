import openai, vocalFunc

# insert here your own openai token
openai.api_key = ""

def askGPT(prompt):
  completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    temperature=0.5,
  )
  message = completions.choices[0].text
  return message
