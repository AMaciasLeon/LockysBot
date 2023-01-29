# APUNTES DE LOCKY'S BOT

[![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
>Made by @LexDev 
## **TOKEN**
<p>Un token de Discord es una clave secreta utilizada para autenticar y autorizar un bot para conectarse y interactuar con un servidor de Discord. Es esencial para que el bot pueda enviar y recibir mensajes, modificar canales y realizar otras acciones en el servidor. El token debe mantenerse privado y no debe compartirse con nadie, ya que cualquier persona que lo tenga podría utilizarlo para controlar el bot.</p>

```py
token = "TOKEN"
```

## **INTENTS**
<p>Este código se refiere a la creación de un bot de Discord utilizando un paquete “discord.py” y la clase “commands.Bot”. El código tiene dos líneas:</p>

* <p>1. La primera línea establece que se van a utilizar todas las intenciones disponibles en Discord. Las intenciones especifican qué tipos de eventos o acciones puede ver y manejar el bot. Por ejemplo, la intención de mensajes permite al bot ver y responder a los mensajes enviados en un servidor.</p>

* <p>2. La segunda línea crea una instancia de la clase “commands.Bot” y la asigna a la variable “bot”. El prefijo de comandos se establece “/” y se pasan las intenciones especificadas anteriormente como un argumento. Esto significa que cuando el bot reciba un mensaje que comience con “/”, lo interpretará como un comando.</p>

```py
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)
```

<p>En resumen, este código está configurando el bot para utilizar todas las intenciones de Discord y estableciendo el prefijo de comandos “/”. Esto permite al bot ver y responder a eventos específicos en un servidor de Discord, y ejecutar comandos específicos cuando se le envíen mensajes que comiencen con “/”.</p>

## **SUMA**
<p>Este código es una función de comando para un bot de Discord que se utiliza para sumar dos números. La función tiene tres partes principales:</p>  

* <p>1. La primera línea es un decorador de la clase bot.command() que indica que esta función es un comando. El bot ejecutará esta función cuando se envíe un mensaje que comience con el prefijo de comando establecido anteriormente (en este caso, “/”) seguido del nombre del comando “suma” y los dos números a sumar.</p>

* <p>2. La segunda línea es la declaración de la función “suma()”, que toma dos argumentos: “ctx” y “num1” y “num2”. “ctx” es un objeto que contiene información sobre el contexto del comando, como el usuario que lo envió y el servidor en el que se envió. “num1” y “num2” son los dos números que se van a sumar.</p> 
    
* <p>3. El resto de las líneas, se verifica si los valores son numéricos y si no son, se lanza una excepción ValueError, luego se suman los valores y se verifica si son enteros o flotante, y si son enteros se muestra el resultado con el formato: “{int(num1)} + {int(num2)} = {int(resultado)}”.</p>

```py
@bot.command()
async def suma(ctx, num1: str, num2: str):
    try:
        num1 = int(num1)
    except ValueError:
        num1 = float(num1)
    try:
        num2 = int(num2)
    except ValueError:
        num2 = float(num2)
    resultado = num1 + num2
    if isinstance(num1, Integral) and isinstance(num2, Integral):
        await ctx.send(f"{int(num1)} + {int(num2)} = {int(resultado)}")
    else:
        await ctx.send(f"{num1} + {num2} = {resultado}")
```

<p>En resumen, este código crea un comando “suma” para un bot de Discord que permite sumar dos números y mostrar el resultado en un formato adecuado, dependiendo si son numéricos enteros o flotantes.</p>

## **RESTA**

<p>Este código es el mismo que el de la suma, pero variando las operaciones. En resumen, este código crea un comando "resta" para un bot de Discord que permite restar dos números y mostrar el resultado en un formato adecuado, dependiendo si son numéricos enteros o flotantes.</p>

```py
@bot.command()
async def resta(ctx, num1: str, num2: str):
    try:
        num1 = int(num1)
    except ValueError:
        num1 = float(num1)
    try:
        num2 = int(num2)
    except ValueError:
        num2 = float(num2)
    resultado = num1 - num2
    if isinstance(num1, Integral) and isinstance(num2, Integral):
        await ctx.send(f"{int(num1)} - {int(num2)} = {int(resultado)}")
    else:
        await ctx.send(f"{num1} - {num2} = {resultado}")
```

## **MULTIPLICACIÓN**

<p>Este código es una función de comando de Discord para un bot de Discord escrito en Python. La función se llama “multiplicación” y se activa cuando alguien escribe el prefijo de comando especificado (por ejemplo “/”) seguido de “multiplicación” en un servidor donde se ha agegado el bot.</p>
<p>La función toma dos argumentos, “num1” y “num2”, que son los números a multiplicar. Los argumentos se asignan como una cadena, pero luego se intenta convertir a un entero y si falla se intenta convertir a un número de punto flotante.</p>
<p>Luego, se multiplican ambos números y se almacena el resultado en una variable “resultado”. Se comprueba si los dos números son enteros, y si es así, se envía un mensaje al canal de Discord con el formato “num1 x num2 = resultado”, si es un decimal se envía el mismo mensaje pero con el formato decimal.</p>

```py
@bot.command()
async def multiplicacion(ctx, num1: str, num2: str):
    try:
        num1 = int(num1)
    except ValueError:
        num1 = float(num1)
    try:
        num2 = int(num2)
    except ValueError:
        num2 = float(num2)
    resultado = num1 * num2
    if isinstance(num1, Integral) and isinstance(num2, Integral):
        await ctx.send(f"{int(num1)} x {int(num2)} = {int(resultado)}")
    else:
        await ctx.send(f"{num1} x {num2} = {resultado}")
```

## **DIVISIÓN** 

<p>Este código es una función de comando de Discord para un bot. La funcón es “división”, y se ejecuta cuando un usuario escribe el prefijo de comano “/division” seguido de dos argumentos numéricos en un canal de Discord donde el bot está presente.
Paso a paso, el código hace lo siguiente:</p>

* <p>1.	Utiliza el decorador “@bot.command()” para indicar que esta función es un comando del bot.</p>
* <p>2.	Utiliza el contexto “ctx” para acceder al canal de Discord donde el comando fue ejecutado.</p>
* <p>3.	Utiliza los argumentos “num1” y “num2” para obtener los números que el usuario ingresó después del comando.</p>
* <p>4.	Utiliza bloques try-except para convertir los argumentos “num1” y “num2” a tipos flotantes.</p>
* <p>5.	Verifica si “num2” es distinto de 0, si es así, realiza la división y guarda el resultado en una variable “resultado”.</p>
* <p>6.	Utiliza una comparación “if-else” para determinar si el resultado es un número entero o no, y envía un mensaje al canal de Discord con el resultado.</p>
* <p>7.	Si num2 es igual a cero, envía un mensaje “No se puede dividir para 0”</p>
* <p>8.	Fin.</p>

```py
@bot.command()
async def division(ctx, num1: str, num2: str):
    try:
        num1 = float(num1)
    except ValueError:
        num1 = float(num1)
    try:
        num2 = float(num2)
    except ValueError:
        num2 = float(num2)
    if num2 != 0:
        resultado = num1 / num2
        if isinstance(num1, Integral) and isinstance(num2, Integral) and resultado.is_integer():
            await ctx.send(f"{float(num1)} / {float(num2)} = {int(resultado)}")
        else:
            await ctx.send(f"{num1} / {num2} = {resultado}")
    else:
        await ctx.send("No se puede dividir para 0")
```

## **RAÍZ CUADRADA**

<p>Este código define un comando de Discord llamado “raíz” que se ejecuta cuando un usuario escribe “/raíz” seguido de un número en un servidor donde el bot está conectado. El comando toma un argumento “num” que se espera sea un número en formato de cadena.</p>

<p>Primero se intenta convertir “num” a un número de punto flotante utilizando la función “float()”. Si la conversión falla (por ejemplo, si “num” no es un número válido), se utiliza el valor actual de “num” (que seguiría siendo una cadena).
Luego se utiliza la función “math.sqrt(num)” para calcular la raíz cuadrada de “num”. El resultado se almacena en una variable “resultado”.</p>

<p>Finalmente, se verifica si “num” es un número entero y si “resultado” es un número entero. Si ambas condiciones son verdaderas, e envía un mensaje al canal de Discord donde se ejecutó el comando indicando que “La raíz cuadrada de (num) es (resultado)”. Si alguna de las condiciones es falsa, se envía un mensaje indicando “La raíz cuadrada de (num) es (resultado)”.
</p>

```py
@bot.command()
async def raiz(ctx, num: str):
    try:
        num = float(num)
    except ValueError:
        num = float(num)
    resultado = math.sqrt(num)
    if isinstance(num, Integral) and resultado.is_integer():
        await ctx.send(f"La raíz cuadrada de {int(num)} es {int(resultado)}")
    else:
        await ctx.send(f"La raíz cuadrada de {num} es {resultado}")
```

## **HOLA**

<p>El bot tiene un comando llamado “hola” que es activado cuando alguien escribe “/hola” en un canal de Discord donde el bot está presente. Cuando el comando es activado, el  bot elige una respuesta al azar de una lista de respuestas predefinidas y la envía al canal de Discord, incluyendo una mención al usuario que activó el comando usando el formato “{}”.</p>

```py
@bot.command()
async def hola(ctx):
    respuestas = ["¡Hola, {}! ¿Cómo estás?", "¡Saludos, {}! ¿Cómo te va?", "¡Hola de nuevo, {}! ¿Qué hay de nuevo?", "¡Hola, {}! ¿Qué tal tu día?", "¡Hola, {}! ¿Programamos algo hoy?"]
    respuesta_elegida = random.choice(respuestas)
    await ctx.send(respuesta_elegida.format(ctx.author.mention))
```

## **ELIMINA MENSAJES Y FUNCIÓN RUN()**

<p>El bot tiene un comando llamado “elimina” que se activa cuando alguien escribe “/elimina x” en un canal de Discord donde el bot está presente, donde “x” es un número entero que representa la cantidad de mensajes a eliminar. Cuando el comando es activado, el bot busca los útimos “x” mensajes en el canal de Discord y los elimina. Además el bot guarda los contenidos de los mensajes eliminados en una lista, y luego envía al canal de Discord un mensaje que contiene los contenidos de los mensajes eliminados. Al final se ejecuta bot.run(token) para iniciar la conexión del bot con el servidor de Discord.</p>

```py
@bot.command()
async def elimina(ctx, cantidad: int):
    deleted_messages = []
    async for message in ctx.channel.history(limit=cantidad):
        deleted_messages.append(message.content)
        await message.delete()
    await ctx.send(f"Los siguiente mensajes fueron eliminados: {deleted_messages}")    
bot.run(token)
```
