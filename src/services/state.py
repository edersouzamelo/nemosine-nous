SYSTEM_STATE = "BOOTING"
PREVIOUS_STATE = None

ALLOWED_TRANSITIONS = {
    "BOOTING": {"READY"},
    "READY": {"RUNNING"},
    "RUNNING": {"SHUTDOWN"},
}

def get_state():
    return SYSTEM_STATE

def get_previous_state():
    return PREVIOUS_STATE

def set_state(new_state):
    global SYSTEM_STATE, PREVIOUS_STATE
    current = SYSTEM_STATE
    allowed = ALLOWED_TRANSITIONS.get(current, set())

    if new_state not in allowed:
        print(f"[STATE] Transição inválida: {current} -> {new_state}")
        return False

    PREVIOUS_STATE = SYSTEM_STATE
    SYSTEM_STATE = new_state
    return True


