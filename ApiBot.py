pip install openai

#Utilitario de conexión al servicio de Azure OpenAI
from openai import AzureOpenAI

#Conexión al servicio de Azure OpenAI
servicio = AzureOpenAI(
    api_version = "",
    azure_endpoint = "h",
    api_key = ""
)

#Modelo desplegado
modelo = "pt-4o"

#"Personalidad" (contexto general) del modelo
contextoGeneral = """
  Eres un asistente virtual del Hotel Valle del Volcán. Tu objetivo es responder todas las dudas de los clientes para lograr que realicen una reserva. Las respuestas a los clientes deben ser amables e incluir emojis apropiados.
  Tus respuestas deben estar en el mismo idioma que la pregunta del usuario.
  Los Metodos de pago son por visa bcp y yape.
"""
#"Personalidad" (contexto general) del modelo
contextoGeneral = """
  Eres un asistente virtual del Hotel Valle del Volcán. Tu objetivo es responder todas las dudas de los clientes para lograr que realicen una reserva. Las respuestas a los clientes deben ser amables e incluir emojis apropiados.
  Tus respuestas deben estar en el mismo idioma que la pregunta del usuario.
  Los Metodos de pago son por visa bcp y yape.
"""
#Memoria a corto plazo para recordar todas las preguntas y respuestas
memoria = []

#Agregamos a la memoria la "personalidad"
memoria.append({"role": "system", "content": contextoGeneral})

#Definimos el mensaje
mensaje = """
Muy buenos días, estoy interesado en alquilar una habitacion.
¿Qué metodos de pago tiene?
"""
#Agregamos el mensaje a la memoria de corto plazo
memoria.append({"role": "user", "content": mensaje})

#Enviamos el mensaje para obtener la respuesta
respuesta = servicio.chat.completions.create(
    model = modelo,
    messages = memoria
)
#Enviamos el mensaje para obtener la respuesta
respuesta = servicio.chat.completions.create(
    model = modelo,
    messages = memoria
)

#Verificamos la respuesta
respuesta

#Obtenemos solo la respuesta
print(respuesta.choices[0].message.content)

#Definimos el mensaje
mensaje = """
Dame un dato interesante del fútbol
"""

#Agregamos el mensaje a la memoria de corto plazo
memoria.append({"role": "user", "content": mensaje})
#Verificamos la memoria
memoria

#Enviamos el mensaje para obtener la respuesta
respuesta = servicio.chat.completions.create(
    model = modelo,
    messages = memoria
)

#Obtenemos solo la respuesta
print(respuesta.choices[0].message.content)

