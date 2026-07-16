# TaskFlow API v2

### Стек технологий
- **Backend**: Python + FastAPI (высокая производительность, авто-документация)
- **Валидация**: Pydantic (авто-валидация данных)
- **ORM**: SQLAlchemy + Alembic (схемы для БД, миграции)
- **БД**: PostgreSQL (реляционная СУБД)
- **Контейнеризация**: Docker + Docker Compose
- **Контроль версий**: Git
#### В будущих версиях
- **Хранение файлов**: S3/MinIO (облачное хранение файлов)
- **Аутентификация**: JWT + Keycloak (авторизация и аутентификация)
- **CI/CD**: GitLab CI/CD (автоматизация тестирования и деплоя)
### Структура проекта
```text
taskflow-api/
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │           ├── attachments.py
│   │           ├── projects.py
│   │           ├── tasks.py
│   │           ├── users.py
│   │       └── router.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── models/
│   │       ├── __init__.py
│   │       ├── attachments.py
│   │       ├── projects.py
│   │       ├── tasks.py
│   │       └── users.py
│   │   ├── base.py
│   │   └── session.py
│   ├── repositories/
│   │   ├── attachment_repository.py
│   │   ├── project_repository.py
│   │   ├── task_repository.py
│   │   └── user_repository.py
│   ├── schemas/
│   │   ├── attachments.py
│   │   ├── projects.py
│   │   ├── tasks.py
│   │   └── users.py
│   ├── services/
│   │   ├── attachment_service.py
│   │   ├── project_service.py
│   │   ├── task_service.py
│   │   └── user_service.py
│   └── main.py
├── docs/
├── .dockerignore
├── .env.example
├── .gitignore
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```
### Схема запуска
1. Клонируйте репозиторий
2. Запустите в консоли проекта `docker-compose up --build`
### Переменные окружения
### Команды для Docker
### Команды для миграций
### Описание основных API-модулей
#### tasks
| Метод   | Эндпоинт                   | Описание         |
|---------|----------------------------|------------------|
| `GET`   | `/tasks`                   | Вывод всех задач |
#### projects
#### users
#### auth - 
#### files -
#### storage -
#### database -
### Инструкция для локальной разработки -
