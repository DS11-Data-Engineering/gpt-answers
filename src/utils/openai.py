import openai
import os

ENGINE = 'text-davinci-003'
MAX_TOKENS = 1000

# Openai key
openai.api_key = os.getenv('OPENAI_KEY')

def get_answer(question: str) -> str:
    answer = openai.Completion.create(
        engine=ENGINE,
        prompt=question,
        max_tokens=MAX_TOKENS)
    
    answer = answer.choices[0].text.strip()

    return answer