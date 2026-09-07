# FastAPI Backend Engineering

> A hands-on progression from FastAPI fundamentals to production-oriented backend architecture — covering REST APIs, validation, persistence, ORM design, dependency injection, and asynchronous Python.

This repository documents my practical journey into **modern backend engineering with FastAPI**. Rather than treating FastAPI as a collection of tutorials, I’m using the project to progressively build and refactor backend systems using patterns that scale beyond a single script or demo application.

The focus is on understanding **why backend systems are structured the way they are**, while continuously improving implementation quality as the project evolves.

---

## ⚡ What This Repository Demonstrates

**API Design**

* RESTful CRUD endpoints using `GET`, `POST`, `PUT`, and `DELETE`
* Path and query parameter handling
* Structured request and response models

**Validation & Data Modeling**

* Pydantic schemas with explicit type validation
* Separation between API schemas and database models
* Automatic serialization and response validation

**Persistence & ORM**

* SQLAlchemy-based database integration
* Engine, session, and model configuration
* Transition from in-memory state to persistent storage
* Programmatic database initialization and seeding

**Backend Architecture**

* FastAPI dependency injection with `Depends`
* Separation of API, validation, and persistence concerns
* Reusable database-session patterns
* Progressive refactoring toward maintainable backend structure

**Python Backend Development**

* Modern Python type hints
* ASGI-based application serving
* Exploration of asynchronous programming patterns
* API development with FastAPI and Uvicorn

---

### Phase 01 — API Fundamentals

**Status: Completed**

Built the foundation of a REST API and developed an understanding of how HTTP requests move through a FastAPI application.

* Implemented complete CRUD workflows
* Designed routes using path and query parameters
* Created structured request models with Pydantic
* Added validation at the API boundary
* Worked with FastAPI's automatic API documentation

### Phase 02 — Persistence & ORM

**Status: In Progress**

Moving beyond transient in-memory data toward a persistent backend.

* Integrating SQLAlchemy as the ORM layer
* Configuring database engines and sessions
* Defining database models and table structures
* Introducing programmatic database initialization
* Refactoring CRUD operations around persistent data

### Phase 03 — Backend Architecture

**Status: Upcoming**

The next stage focuses on writing backend code that remains understandable and maintainable as complexity increases.

* FastAPI dependency injection with `Depends`
* Reusable database-session management
* Cleaner separation of API and persistence concerns
* Transaction-aware CRUD operations
* More modular application structure
* Preparing APIs for full-stack consumption

---

## 🧰 Technology Stack

| Technology       | Purpose                                  |
| ---------------- | ---------------------------------------- |
| **FastAPI**      | REST API framework and application layer |
| **Python**       | Backend implementation                   |
| **Pydantic**     | Request validation and data schemas      |
| **SQLAlchemy**   | ORM and database interaction             |
| **Uvicorn**      | ASGI application server                  |
| **Git / GitHub** | Version control and project progression  |

---

## 🔍 Engineering Principles

This project is also a deliberate exercise in developing good engineering habits.

### Learn → Implement → Refactor

I don't want to stop at getting an endpoint to work.

Each stage is an opportunity to understand the underlying mechanism, implement it, identify architectural limitations, and improve the design in the next iteration.

### Explicit Data Contracts

API boundaries should be predictable.

Pydantic models are used to make request and response structures explicit rather than relying on loosely structured dictionaries or implicit assumptions.

### Separation of Concerns

As the project grows, API routing, validation, database access, and application logic are being progressively separated.

The goal is to make individual components easier to understand, test, replace, and extend.

### Build for Understanding

The repository intentionally shows the progression from simpler implementations to more structured ones. The intermediate implementations are part of the learning process rather than being hidden behind a single polished final state.

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/ManjunathAnde/FASTAPI-Project
cd fastapi-project
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the development server

```bash
uvicorn main:app --reload
```

The API will be available locally at:

```text
http://127.0.0.1:8000
```

---

## 📖 Explore the API

FastAPI automatically generates interactive API documentation.

**Swagger UI**

```text
http://127.0.0.1:8000/docs
```

**ReDoc**

```text
http://127.0.0.1:8000/redoc
```

These interfaces can be used to inspect available endpoints and send requests directly to the running application.

---

## 📈 Current Focus

I'm currently extending the project from **functional API development toward backend engineering practices**:

```text
Basic Routes
     ↓
CRUD APIs
     ↓
Validation & Schemas
     ↓
Database Persistence
     ↓
ORM Architecture
     ↓
Dependency Injection
     ↓
Modular Backend
     ↓
Full-Stack Ready APIs
```

The objective is not simply to become familiar with FastAPI syntax, but to develop the ability to **design, reason about, and continuously improve backend systems**.


---

## 👋 Why This Repository Exists

I'm using this repository to turn backend concepts into **working systems**, document what I learn, and progressively raise the engineering standard of the code.



---

**Built with Python, FastAPI, and a bias toward learning by building.**
