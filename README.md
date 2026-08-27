# Taller Práctico | Asistente de IA

Implementación de un script en Python que utiliza la librería `google-genai`
para realizar peticiones, procesar textos y gestionar conversaciones
interactivas con roles definidos (Gemini API).

## Requisitos previos

- Python 3.10 o superior.
- Una API key de Gemini (se obtiene gratis en [Google AI Studio](https://aistudio.google.com/apikey)).

## Instalación

1. Clona el repositorio y entra a la carpeta:
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-carpeta>
   ```

2. Instala las dependencias:
   ```bash
   pip install google-genai python-dotenv
   ```

3. Configura tu API key:
   - crea `.env` y reemplaza el valor con tu API key real:
     ```
     GEMINI_API_KEY=tu_api_key_aqui
     ```

## Ejecución de cada ejercicio

### Ejercicio 1 — Conexión y Petición Básica

Inicializa el cliente de Gemini y le pide que explique qué es la
"Inferencia en IA" en menos de 50 palabras.

```bash
python 1_CreacionPeticion.py
```

**Salida esperada:** un párrafo corto (menos de 50 palabras) explicando el
concepto de inferencia en IA.

### Ejercicio 2 — Procesador de Textos Inteligente

Define la función `2_Procesar_articulo(texto, tarea)`, que usa una
`system_instruction` (rol de "Editorial de prestigio") para resumir
o profesionalizar un texto de ejemplo incluido en el propio script.

```bash
python 2_ProcesarTexto.py
```

**Salida esperada:** primero un resumen ejecutivo del artículo de ejemplo,
luego una versión reescrita en tono formal/técnico del mismo texto.

Si quieres probar con tu propio texto, edita la variable
`articulo_ejemplo` al final del script, o importa la función desde otro
archivo:

```python
from procesar_texto import procesar_articulo

resultado = procesar_articulo("tu texto aquí", "resumir")
print(resultado)
```

### Ejercicio 3 — Chat de Soporte con Historial (Few-Shot)

Simula el chat de una tienda de tecnología. La IA actúa como un vendedor
amable (definido vía `system_instruction`), con un historial pre-cargado
de 2 ejemplos de interacción (few-shot) para guiar el estilo de respuesta.

```bash
python 3_ChatSoporte.py
```

**Uso:**
- El programa abre un bucle interactivo en la terminal.
- Escribe tus preguntas sobre productos y presiona Enter.
- Escribe `finalizar` para terminar la conversación.

**Salida esperada:** respuestas del "vendedor" con especificaciones de
producto, manteniendo el hilo de la conversación (recuerda lo que
preguntaste antes).


## Evidencias de ejecución

Las capturas de pantalla con la ejecución y salida de cada ejercicio:

Ejercicio 1

Ejercicio 2

Ejercicio 3

## Autores

- Josel Patiño | Jordi Madrid
- Desarrollo de Aplicaciones con IA | Universidad Konrad Lorenz
