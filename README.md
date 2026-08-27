# Taller: Asistente de IA con google-genai

Implementación de un script en Python que utiliza la librería `google-genai`
para realizar peticiones, procesar textos y gestionar conversaciones
interactivas con roles definidos (Gemini API).

## 📂 Contenido del repositorio

```
├── 1_PeticionBasica.py     # Ejercicio 1: conexión y petición simple
├── 2_ProcesarTexto.py      # Ejercicio 2: procesador de textos (resumir / profesionalizar)
├── 3_ChatSoporte.py        # Ejercicio 3: chat de soporte con historial few-shot
├── .env.example            # Plantilla para la API key
├── .gitignore               # Excluye el archivo .env real
├── evidencias/               # Capturas de pantalla de la ejecución
└── README.md
```

## ✅ Requisitos previos

- Python 3.10 o superior.
- Una API key de Gemini (se obtiene gratis en [Google AI Studio](https://aistudio.google.com/apikey)).

## 🔧 Instalación

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
   - Copia el archivo `.env.example` y renómbralo a `.env`.
   - Abre `.env` y reemplaza el valor de ejemplo con tu API key real:
     ```
     GEMINI_API_KEY=tu_api_key_aqui
     ```
   - **Importante:** el archivo `.env` nunca se sube a GitHub (ya está
     excluido en `.gitignore`). Así se evita exponer la clave.

## ▶️ Ejecución de cada ejercicio

### Ejercicio 1 — Conexión y Petición Básica

Inicializa el cliente de Gemini y le pide que explique qué es la
"Inferencia en IA" en menos de 50 palabras.

```bash
python 1_PeticionBasica.py
```

**Salida esperada:** un párrafo corto (menos de 50 palabras) explicando el
concepto de inferencia en IA.

### Ejercicio 2 — Procesador de Textos Inteligente

Define la función `procesar_articulo(texto, tarea)`, que usa una
`system_instruction` (rol de "Editor Editorial de prestigio") para resumir
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

## 🐞 Solución de problemas comunes

- **`ValueError: No se encontró la variable de entorno GEMINI_API_KEY`**
  → Verifica que el archivo `.env` existe en la misma carpeta del script
  y que tiene el nombre exacto `.env` (no `.env.txt`).

- **`404 NOT_FOUND ... model is no longer available`**
  → El modelo usado en el script (`gemini-3.6-flash`) puede cambiar con
  el tiempo. Revisa la [documentación de modelos de Gemini](https://ai.google.dev/gemini-api/docs/models)
  para ver el nombre del modelo vigente y actualízalo en el script si es
  necesario.

## 📸 Evidencias de ejecución

Las capturas de pantalla con la ejecución y salida de cada ejercicio se
encuentran en la carpeta [`evidencias/`](./evidencias).

## 👤 Autor(es)

- Josel — Universidad Konrad Lorenz
