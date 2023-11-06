from modulos.talker.talk import Talker, TtsTalker
from modulos.listen import Listener
from modulos.langchain_assistant.langchain_brain import LangChainBrainAssistant
import typer
from rich import print

talker = Talker(TtsTalker())
listener = Listener()
langchain_assistant = LangChainBrainAssistant()

def say_welcome():
    talker.talk(
        "Hola, bienvenido al modo sábelo todo, hazme cualquier pregunta"
    )
    print("[bold red]Hola, bienvenido al modo sábelo todo, hazme cualquier pregunta[/bold red]")
    
def listen_to_response():
    return listener.listen()

def generate_response():
    response = langchain_assistant.chat(listen_to_response())
    return response

def start_brain_mode():
    say_welcome()
    assistant_response= generate_response()
    print(f"[bold red]{assistant_response}[/bold red]")
    talker.talk(assistant_response)