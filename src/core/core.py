from services import lifecycle, state
from config.settings import VERSION

def init(ticks=1):
    print(f"Nemosine Nous v{VERSION}")

    previous = None
    current = state.BOOTING
    print(f"Previous state: {previous}")
    print(f"Current state: {current}")

    previous, current = state.transition(previous, current)
    print(f"Previous state: {previous}")
    print(f"Current state: {current}")

    for _ in range(ticks):
        lifecycle.tick(current)

    print("Eventos registrados:")
    for event in lifecycle.get_events():
        print(event)

    print("Core inicializado")





