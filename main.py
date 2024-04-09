from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-3.5"

# No sistema vc coloca parametros pra IA usar e no usuario voce coloca oque deseja
prompt_sistema =  "Listar nome dos atletas, e por como descrição apenas o esporte e nada mais"
prompt_usuario =  "Liste os 10 atletas mais bem pagos do atual ano"

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": prompt_sistema
        },
        {
            "role": "user",
            "content": prompt_usuario
         }
    ],
    model=modelo
)

print(resposta.choices[0].message.content)