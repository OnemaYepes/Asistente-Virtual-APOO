from modulos.listen import Listener
import pywhatkit
from modulos.menus.brain import start_brain_mode
from modulos.talker.talk import Talker, TtsTalker
import requests
import typer
from rich import print
from rich.table import Table


def main():
    talker = Talker(TtsTalker())
    listener = Listener()
    try:
        print("[bold]Dile al asistente:[/bold]")
        
        table = Table("Comando", "Descripción")
        table.add_row("Reproduce", "Seguido del Artista y Título Canción")
        table.add_row("Temperatura", "Seguido de la Ciudad")
        table.add_row("Pregunta", "Para activar modo Sábelo Todo")
        print(table)
        
        user_prompt = listener.listen()
        
        if 'reproduce' in user_prompt:
            song = user_prompt.replace('reproduce', '')
            pywhatkit.playonyt(song)
        
        elif 'temperatura' in user_prompt:
            print(user_prompt)
            if user_prompt:
                ciudad = user_prompt.replace('temperatura', '')
                print(ciudad)
                url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=3030164fee6931ada696009c6e4aa19d&units=metric".format(ciudad)
                res = requests.get(url)
                data = res.json()
                temp = data["main"]["temp"]
                talker.talk(str(temp))
                print("[bold blue]Temperatura[/bold blue]", temp)
        elif 'Pregunta' in user_prompt:
            print("[bold green]🤓 Entrando a Sábelo todo[/bold green]")
            start_brain_mode()
        else:
            print(user_prompt)
            
    except Exception as e:
        print(f"Lo lamento, no te entendí debido a este error: {e}")
        print(e)

if __name__ == '__main__':
    typer.run(main)