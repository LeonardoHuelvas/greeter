from datetime import datetime

class Greeter:
    """
    Una clase para saludar a las personas según la hora del día.

    La clase Greeter tiene un método `greet` que toma un nombre como entrada
    y devuelve un saludo adecuado dependiendo de la hora del día. Además, el
    método `greet` elimina los espacios en blanco al principio y al final del 
    nombre, capitaliza la primera letra del nombre y registra en la consola 
    cada vez que es llamado.

    Métodos:
        greet(name):
            Saluda a la persona según la hora del día y el nombre proporcionado.
    """

    def greet(self, name):
        """
        Saluda a la persona con un saludo adecuado según la hora del día.

        El método `greet` realiza las siguientes acciones:
        1. Elimina los espacios en blanco al principio y al final del nombre.
        2. Capitaliza la primera letra del nombre.
        3. Devuelve diferentes saludos según la hora del día:
           - "Good morning <nombre>" entre las 06:00 y las 12:00.
           - "Good evening <nombre>" entre las 18:00 y las 22:00.
           - "Good night <nombre>" entre las 22:00 y las 06:00.
           - "Hola <nombre>" en cualquier otra hora del día.
        4. Registra en la consola cada vez que es llamado.

        Args:
            name (str): El nombre de la persona a saludar.

        Returns:
            str: Un saludo adecuado según la hora del día y el nombre proporcionado.
        """
        name = name.strip().capitalize()
        current_hour = datetime.now().hour

        if 6 <= current_hour < 12:
            greeting = "Good morning"
        elif 18 <= current_hour < 22:
            greeting = "Good evening"
        elif 22 <= current_hour or current_hour < 6:
            greeting = "Good night"
        else:
            greeting = "Hola"

        print(f"Greet called with name: {name}")
        return f"{greeting} {name}"
