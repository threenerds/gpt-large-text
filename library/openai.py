import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")


def completion(prompt_request):
    # Definir el modelo y la configuración de la solicitud
    modelo = "text-davinci-003"
    configuracion = {
        "engine": modelo,
        "max_tokens": 1024,
        "temperature": 0,
        "top_p":1,
        "frequency_penalty":0,
        "presence_penalty":0
    }

    respuesta = openai.Completion.create(prompt=prompt_request, **configuracion)

    return respuesta    


def chat_completion(prompt_request):
    messages = [{"role": "system", "content": "This is text summarization."}]    
    messages.append({"role": "user", "content": prompt_request})

    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=.5,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
    )
    
    response["choices"][0]["message"]['content'].strip()