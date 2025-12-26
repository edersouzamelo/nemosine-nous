from config import settings
from services.state import get_state, get_previous_state, set_state
from services import lifecycle

def init(ticks=1):
    print(f"{settings.SYSTEM_NAME} v{settings.SYSTEM_VERSION}")

    print(f"Previous state: {get_previous_state()}")
    print(f"Current state: {get_state()}")

    set_state("READY")

    print(f"Previous state: {get_previous_state()}")
    print(f"Current state: {get_state()}")

    for _ in range(ticks):
        lifecycle.tick()

    print("Core inicializado")


