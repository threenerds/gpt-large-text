import openai
import os
from .text import num_tokens_from_string

openai.api_key = os.getenv("OPENAI_API_KEY")

# max tokens 4096
def completion(prompt_request):
    # Calcular Tokens
    prompt_token_count = num_tokens_from_string(prompt_request)
    remaining_response_tokens = 4096 - prompt_token_count
    
    
    # Definir el modelo y la configuración de la solicitud
    modelo = "text-davinci-003"
    configuracion = {
        "engine": modelo,
        "max_tokens": remaining_response_tokens,
        "top_p":0.1,
        "frequency_penalty":0,
        "presence_penalty":0
    }

    respuesta = openai.Completion.create(prompt=prompt_request, **configuracion)

    return respuesta    


def chat_completion(prompt_request):
    messages = [{"role": "system", "content": "This is text summarization."}]    
    messages.append({"role": "user", "content": prompt_request})
    return openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
    )
    
    