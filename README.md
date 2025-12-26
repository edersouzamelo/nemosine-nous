# Nemosine Nous — Minimal Executable Architecture (AME)

This repository contains the **Minimal Executable Architecture (AME)** of **Nemosine Nous**.

The AME represents the **smallest runnable architectural core** required for the system to exist as an executable system, prior to any expansion into MVP features, persistence layers, autonomous agents, or optimization mechanisms.

It is intentionally minimal, explicit, and verifiable.

---

## Purpose

The purpose of this repository is to:

- Demonstrate that the architecture defined in **TR-004 — Arquitetura Mínima Executável (AME)** is **implemented and runnable**
- Provide a **public, time-stamped executable baseline**
- Enable external inspection and verification of the architectural core
- Serve as a **stable reference point** for future evolution toward an MVP

This repository is **not** intended to represent a complete product.

---

## Scope (What is included)

The AME includes only what is strictly necessary for architectural executability:

- **Governed system state** with explicit lifecycle transitions (`BOOTING → READY`)
- **Deterministic lifecycle execution**, controlled via CLI ticks
- **Observable execution loop**, producing runtime output
- **Runtime event logging** with timestamped records
- **Clear separation** between system state, lifecycle control, and execution flow

---

## Explicit Exclusions

By design, this repository does **not** include:

- Long-term or vector-based memory
- Autonomous agents or multi-agent systems
- Learning, optimization, or adaptation mechanisms
- External integrations or APIs
- Graphical or web interfaces
- Persistence layers or databases
- Production or deployment infrastructure

Any of the above belong to **future stages**, not to the AME.

---

## How to Run

### Requirements
- Python 3.9+

### Execution

```bash
python src/main.py --ticks 3

```

###Expected Output (example)

```bash
Nemosine Nous iniciado
Nemosine Nous v0.1.0
Previous state: None
Current state: BOOTING
Previous state: BOOTING
Current state: READY
[LIFECYCLE] Tick 1 | state=READY
[LIFECYCLE] Tick 2 | state=READY
[LIFECYCLE] Tick 3 | state=READY
Eventos registrados:
{'tick': 1, 'state': 'READY', 'timestamp': '...'}
{'tick': 2, 'state': 'READY', 'timestamp': '...'}
{'tick': 3, 'state': 'READY', 'timestamp': '...'}
Core inicializado
```

The exact timestamps may vary between executions.

## Architectural Status

- **Type:** Minimal Executable Architecture (AME)
- **Stage:** Pre-MVP
- **Maturity:** Non-production
- **Role:** Executable architectural baseline

This repository exists to satisfy the definition of **executability**, not completeness.

---

## Canonical References

- **GitHub (canonical source code):**  
  https://github.com/edersouzamelo/nemosine-nous

- **Zenodo (frozen archive / DOI):**  
  https://zenodo.org/communities/sistema-nemosine

- **OSF Project (engineering context):**  
  https://osf.io/r4yf8/

- **Related technical document:**  
  TR-004 — *Arquitetura Mínima Executável (AME)*

---

## Versioning

This repository follows explicit architectural versioning:

- **v0.1.1-AME** — First frozen executable baseline

Future releases may introduce additional layers (MVP, services, integrations), but this tag remains the **immutable reference** for the AME.

---

## License

Copyright © 2025  
**Edervaldo José de Souza Melo**

This repository is part of an ongoing research and engineering effort.  
Use, redistribution, or derivative work must respect the licensing terms defined in the associated documentation.

