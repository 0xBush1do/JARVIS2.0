import openai, vocalFunc

openai.api_key = "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"

def askGPT(prompt):
  completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    temperature=0.5,
  )
  message = completions.choices[0].text
  return message
