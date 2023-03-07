import openai
import os

ENGINE = 'text-davinci-003'
MAX_TOKENS = 2500
CONTEXT_SIZE = 5
PROMPT_ENGINEERING = '''
    You will be provided with a prompt that will be everything after the first 
    'Prompt: ' that you encounter in this text. You must answer with the 
    requested information following these rules:

        - You must answer in the same language as the prompt.
        - If the prompt doesn't contain any question or request, just mention that and provide a relevant response.
        - Don't provide an answer for something you weren't asked.
        - Act as if it's a conversation between two people.
        - You must not specify you are giving an 'Answer: '.
'''

# Openai key
openai.api_key = os.getenv('OPENAI_KEY')

def get_answer(question: str, context: str='') -> str:
    context = '\nContext:' + str(context[-CONTEXT_SIZE * 2:])
    prompt = PROMPT_ENGINEERING + context + '\nPrompt: ' + question

    answer = openai.Completion.create(
        engine=ENGINE,
        prompt=prompt,
        max_tokens=MAX_TOKENS)
    
    answer = answer.choices[0].text.strip()

    return answer