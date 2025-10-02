# FastAPI Clean Architecture Project

This project is built using **Clean Architecture**, with layers: `core`, `use_cases`, `infrastructure`, and `api`.  
In this example it uses **FastAPI** for creating APIs, **SQLAlchemy** for PostgreSQL database access, and **Pydantic** for data validation.

---

## Project Structure
```
src/
├── api/ # Presentation layer / FastAPI
│ └── fast_api/
│ └── routes/ # Endpoints (user, address)
├── core/ # Domain business entities
│ └── entities/ # Entities (User, Address)
├── infrastructure/ # Repositories, database configuration, exceptions
│ ├── database.py
│ └── entity_configuration/
├── use_cases/ # Business logic / use cases
│ └── user/create_user/
│   ├── create_user_command.py
│   └── create_user_use_case.py
```

---

## Layers Examples

### 1. Core
- `User` – user entity (`firstname`, `lastname`, related addresses)
- `Address` – address entity (`street`, `city`, linked to user)
- `EntityBase` – base class for entities with an `id` field

### 2. Use Cases
- `CreateUserUseCase` – logic for creating a new user
- `CreateUserCommand` – DTO to pass data to the use case

### 3. Infrastructure
- `SqlAlchemyRepository` – generic repository for SQLAlchemy entities
- `get_db` – SQLAlchemy session generator
- Entity-to-table mapping (`user_model.py`, `address_model.py`)

### 4. API
- FastAPI endpoints in `api/fast_api/routes/`
- DTOs:
  - `CreateUserRequestDto` – request for creating a user
  - `CreateUserResponseDto` – response with the new user's ID

---

## Example Endpoint

**POST /users/**

Request:

```json
{
    "firstname": "Jan",
    "lastname": "Kowalski"
}
```

Response:

```json
{
    "id": 1,
    "firstname": "Jan",
    "lastname": "Kowalski",
    "addresses": []
}
```

## Running the Project

- Configure the database connection in infrastructure/database.py:
```python
import os
from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
```
- Install dependencies::
```python
pip install -r requirements.txt
```
- Run the FastAPI server::
```python
uvicorn src.api.fast_api.main:app --reload
```


## Project features
- Alembic - for managing migrations
- Clean Architecture – clear separation of responsibilities
- SQLAlchemy – entity-to-table mapping and repositories
- FastAPI + Pydantic – modern API with request validation
- Modularity – easy to add new use cases and entities
