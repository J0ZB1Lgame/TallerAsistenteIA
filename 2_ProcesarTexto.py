import os
from google import genai
from google.genai import types

# Inicialización del cliente
def crear_cliente() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "No se encontró la variable de entorno GEMINI_API_KEY. "
            "Configúrala antes de ejecutar el script."
        )
    return genai.Client(api_key=api_key)


# System instructions para cada tarea:

# Instrucción base: define el rol/persona de la IA para todo el ejercicio.
ROL_EDITOR = (
    "Eres un Editor Editorial de prestigio, con décadas de experiencia "
    "en publicaciones de alto nivel. Tu trabajo debe reflejar precisión, "
    "claridad y un dominio impecable del idioma."
)

# Instrucciones específicas por tarea, que se agregan al rol base.
INSTRUCCIONES_TAREA = {
    "resumir": (
        f"{ROL_EDITOR} Tu tarea es leer el artículo proporcionado y "
        "generar un resumen ejecutivo: claro, conciso, que capture las "
        "ideas y conclusiones principales, sin opiniones propias ni "
        "información inventada. Usa como máximo 3 a 5 frases."
    ),
    "profesionalizar": (
        f"{ROL_EDITOR} Tu tarea es reescribir el texto proporcionado "
        "para que suene formal, técnico y profesional, corrigiendo "
        "errores gramaticales y mejorando la redacción, mantenendo el "
        "significado original. No agregues información nueva."
    ),
}

# Función principal
def procesar_articulo(texto: str, tarea: str) -> str:
    """
    Procesa un texto largo según la tarea indicada, usando Gemini con
    el system_instruction que define a la IA como una Editorial
    de prestigio.

    Parámetros:
        texto (str): El artículo o texto largo a procesar.
        tarea (str): "resumir" o "profesionalizar".

    Retorna:
        str: El texto procesado por el modelo.
    """
    tarea = tarea.strip().lower()

    if tarea not in INSTRUCCIONES_TAREA:
        raise ValueError(
            f"Tarea '{tarea}' no soportada. Usa 'resumir' o 'profesionalizar'."
        )

    if not texto or not texto.strip():
        raise ValueError("El texto proporcionado está vacío.")

    cliente = crear_cliente()
    system_instruction = INSTRUCCIONES_TAREA[tarea]

    respuesta = cliente.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=texto,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.3,  # baja temperatura para respuestas más consistentes
        ),
    )
    return respuesta.text


# Punto de entrada
if __name__ == "__main__":
    articulo_ejemplo = """
    La inteligencia artificial ha crecido muchísimo en los últimos años,
    la gente la usa para todo, desde escribir correos hasta programar
    aplicaciones enteras. Muchas empresas están metiendo IA en sus
    productos porque creen que así van a vender más y ser más modernas,
    aunque a veces ni saben bien para qué la están usando. De todas
    formas, parece que esto va a seguir creciendo porque cada vez hay
    más herramientas y son más fáciles de usar.
    """

    print("=== RESUMEN EJECUTIVO ===")
    resumen = procesar_articulo(articulo_ejemplo, "resumir")
    print(resumen)

    print("\n=== VERSIÓN PROFESIONALIZADA ===")
    version_formal = procesar_articulo(articulo_ejemplo, "profesionalizar")
    print(version_formal)
