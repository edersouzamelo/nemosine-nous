from config import settings
from services import state

def init():
    print(f"{settings.SYSTEM_NAME} v{settings.SYSTEM_VERSION}")
    print(f"System state: {state.get_state()}")
    print("Core inicializado")
