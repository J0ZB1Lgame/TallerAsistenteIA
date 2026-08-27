import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar el cliente
client = genai.Client(api_key=API_KEY)

configuration = types.GenerateContentConfig(
    max_output_tokens=2048,
    temperature=0,
    system_instruction="""Eres un Vendedor de una tienda de tecnologia realmente amable al momento de atender y el cliente te hace diferentes preguntas acerca de los productos o servicios tu objetivo es ayudarle. 
Aqui hay unos ejemplos de como deberian ser las interacciones:

Cliente: Hola, compre este monitor pero no esta funcionando
Respuesta: Hola, muy buenos dias, ¿tienes el numero de recibo para poder ayudarte?

Cliente: Buenos dias, donde puedo pagar mis productos que ya tengo en el carro
Respuesta: Buenos dias los puedes pagar yengo al carrito y en el boton inferior hacer click sobre pagar

Cliente: Hola, mi celular no esta prendiendo
Respuesta: Buenos dias, si el celular lo compraste en nuestra tienda acercate a ella para solicitar una inspeccion
"""
)

MODEL = "gemini-3.1-flash-lite"

# Historial para simular la memoria del agente durante esta ejecución.
conversation_history = []

print("--- Chat de Tienda  ---")
print("(Escribe 'salir' para terminar)\n")

while True:
        user_input = input("Cliente: ")
        
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("Asistente: ¡Hasta pronto! Espero verte pronto.")
            break

        try:
            conversation_history.append({
                "role": "user",
                "parts": [{"text": user_input}]
            })

            response = client.models.generate_content(
                model=MODEL,
                contents=conversation_history,
                config=configuration
            )
            
            assistant_message = response.text
            conversation_history.append({
                "role": "model",
                "parts": [{"text": assistant_message}]
            })

            print(f"\nAsistente: {assistant_message}\n")

        except Exception as e:            
            print(f"Error al procesar la solicitud: {e}")
