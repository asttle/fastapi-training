# FastAPI Training Repository - Complete Overview

## Repository Purpose
This repository serves as a comprehensive 6-day FastAPI training program, progressively building from basic concepts to advanced full-stack development with various database integrations and template rendering. Each day introduces new concepts while building upon previous knowledge.

## Repository Structure

```
fastapi-training/
├── README.md                    # Complete project documentation
├── day-1/                      # In-memory CRUD operations
│   ├── books.py                # Simple FastAPI app with in-memory storage
│   └── README.md               # Day 1 documentation
├── day-2/                      # SQLite database integration
│   ├── books.py                # Books API with SQLAlchemy + SQLite
│   ├── database.py             # SQLite database configuration
│   ├── models.py               # SQLAlchemy ORM models
│   ├── books.db                # SQLite database file
│   └── README.md               # Day 2 documentation
├── day-3/                      # MongoDB integration & modular architecture
│   ├── main.py                 # FastAPI application entry point
│   ├── config/database.py      # MongoDB Atlas connection
│   ├── models/todos.py         # Pydantic data models
│   ├── routes/route.py         # API route handlers
│   ├── schema/schemas.py       # MongoDB serialization utilities
│   └── README.md               # Day 3 documentation
├── day-4/                      # PostgreSQL integration
│   ├── main.py                 # Quiz application with PostgreSQL
│   ├── database.py             # PostgreSQL connection setup
│   ├── models.py               # Question/Choice models for quiz
│   └── README.md               # Day 4 documentation
├── day-5/                      # Full-stack development (FastAPI + React)
│   ├── README.md               # Day 5 documentation
│   ├── fastapi/                # Backend API
│   │   ├── main.py             # Financial transactions API
│   │   ├── database.py         # SQLite configuration
│   │   └── models.py           # Transaction model
│   └── react/                  # React frontend application
│       └── finance-app/        # Complete React project
│           ├── package.json    # NPM dependencies
│           ├── src/            # React source code
│           └── public/         # Static assets
└── day-6/                      # Template rendering with Jinja2
    ├── main.py                 # FastAPI app with HTML templates
    ├── templates/              # Jinja2 templates
    │   └── home.html           # Homepage template
    └── README.md               # Day 6 documentation
```

## Learning Progression & Key Technologies

### Day 1: FastAPI Fundamentals
**Focus**: Basic API development with in-memory storage
- **Technologies**: FastAPI, Pydantic, Python lists
- **Concepts**: HTTP methods, request/response handling, data validation
- **API**: Books CRUD operations (Create, Read, Update, Delete)
- **Data Storage**: In-memory Python lists

### Day 2: Database Integration
**Focus**: Persistent data storage with relational database
- **Technologies**: FastAPI, SQLAlchemy ORM, SQLite
- **Concepts**: Database sessions, ORM models, dependency injection
- **API**: Enhanced Books API with database persistence
- **Data Storage**: SQLite database (`books.db`)
- **Architecture**: Separated database config, models, and main application

### Day 3: NoSQL & Modular Architecture
**Focus**: Document database and clean code organization
- **Technologies**: FastAPI, MongoDB Atlas, PyMongo, Python-dotenv
- **Concepts**: NoSQL documents, ObjectIds, environment variables, modular structure
- **API**: Todo management system
- **Data Storage**: MongoDB Atlas (cloud NoSQL database)
- **Architecture**: Fully modular with separate config, models, routes, and schemas
- **Security**: Environment-based credential management

### Day 4: Production Database
**Focus**: Enterprise-grade relational database
- **Technologies**: FastAPI, PostgreSQL, SQLAlchemy, Psycopg2
- **Concepts**: Production database setup, foreign keys, relational models
- **API**: Quiz application with questions and multiple-choice answers
- **Data Storage**: PostgreSQL with related tables (Questions → Choices)
- **Models**: Complex relational data with foreign key relationships

### Day 5: Full-Stack Development
**Focus**: Complete application with backend API and frontend
- **Technologies**: FastAPI, SQLite, React/TypeScript
- **Concepts**: Full-stack architecture, financial data management, CORS setup
- **API**: Financial transactions management system
- **Data Storage**: SQLite for financial transactions
- **Frontend**: Complete React application with components and API integration
- **Features**: Transaction tracking with amount, description, date, category, type, account

### Day 6: Template Rendering & Web UI
**Focus**: Server-side HTML rendering with Jinja2 templates
- **Technologies**: FastAPI, Jinja2Templates, HTML/CSS
- **Concepts**: Server-side rendering, template context, dynamic HTML generation
- **Application**: Web interface with template-driven pages
- **Templates**: Jinja2 template system for dynamic content
- **Features**: HTML responses, template inheritance, context passing

## Database Evolution Throughout Training

| Day | Database | Type | Use Case | Key Features |
|-----|----------|------|----------|--------------|
| 1 | In-Memory | Lists | Learning basics | Simple, no persistence |
| 2 | SQLite | Relational | Local development | File-based, SQL, ORM |
| 3 | MongoDB Atlas | NoSQL | Cloud/Document | Cloud-hosted, flexible schema |
| 4 | PostgreSQL | Relational | Production | Enterprise-grade, complex relations |
| 5 | SQLite | Relational | Full-stack app | Simple backend for frontend integration |
| 6 | None | Templates | Web UI | Server-side rendering, no database |

## API Patterns & Architecture Evolution

### Day 1-2: Monolithic Structure
- Single file applications
- Direct route handlers
- Basic error handling

### Day 3-4: Modular Architecture
- Separated concerns (config, models, routes, schemas)
- Environment-based configuration
- Router organization
- Advanced error handling

### Day 5: Full-Stack Architecture
- Backend API separation
- Frontend integration with React
- CORS configuration for cross-origin requests
- Transaction-based business logic

### Day 6: Template-Driven Architecture
- Server-side HTML rendering
- Jinja2 template integration
- Template context management
- Web UI development patterns

## Complete Training Program Status

### Day 1-4: Core Concepts (Complete)
All fundamental FastAPI concepts are implemented and documented:
- ✅ Basic CRUD operations with in-memory storage
- ✅ SQLite integration with SQLAlchemy ORM
- ✅ MongoDB Atlas with modular architecture
- ✅ PostgreSQL with complex relational models

### Day 5: Full-Stack Development (Complete)
- ✅ **Backend API**: FastAPI with financial transactions
- ✅ **Frontend**: Complete React application with component structure
- ✅ **Integration**: Full-stack communication setup
- ✅ **Database**: SQLite with Transaction model

### Day 6: Template Rendering (Current)
- ✅ **FastAPI Setup**: Basic application with Jinja2Templates
- ✅ **Templates**: HTML template system with context passing
- ✅ **Web UI**: Server-side rendered homepage

## Repository Evolution (Git History)

Based on recent commits, the repository has evolved through:

1. **Initial Setup**: Basic FastAPI structure
2. **Database Integration**: Progressive database complexity
3. **Modular Architecture**: Clean code organization in Day 3
4. **Production Readiness**: PostgreSQL integration in Day 4
5. **Full-Stack Preparation**: Current work on Day 5

## Skills & Technologies Mastered

Upon completing this 6-day training program, developers will have hands-on experience with:

### Backend Development
- **FastAPI Framework**: Complete API development from basics to advanced patterns
- **Database Technologies**: SQLite, PostgreSQL, MongoDB Atlas - covering relational and NoSQL paradigms
- **ORM & ODM**: SQLAlchemy for relational databases, PyMongo for MongoDB
- **Data Validation**: Pydantic models for request/response validation
- **Architecture Patterns**: From monolithic to modular, clean architecture principles

### Frontend & Full-Stack
- **React Integration**: Complete frontend development with API communication
- **Template Rendering**: Server-side HTML generation with Jinja2
- **CORS Configuration**: Cross-origin resource sharing for API access
- **Full-Stack Architecture**: End-to-end application development

### Database Expertise
- **Multiple Database Types**: Experience with file-based, cloud, and production databases
- **Data Modeling**: Simple to complex relational models with foreign keys
- **Document Storage**: NoSQL document design and BSON handling
- **Environment Management**: Secure credential handling and configuration

### Development Practices
- **Modular Code Organization**: Clean separation of concerns
- **Environment Variables**: Secure configuration management
- **Error Handling**: Proper HTTP exception handling patterns
- **API Design**: RESTful endpoint design and implementation

## Applications Built

1. **Books API** (Day 1-2): CRUD operations with in-memory and persistent storage
2. **Todo Management** (Day 3): Document-based task management with MongoDB
3. **Quiz System** (Day 4): Relational quiz application with PostgreSQL
4. **Financial Tracker** (Day 5): Full-stack transaction management
5. **Web Interface** (Day 6): Template-driven web application

## Getting Started with Any Day

Each day is self-contained with its own README and can be run independently:

```bash
# Day 1-2: Books API
cd day-1  # or day-2
uvicorn books:app --reload

# Day 3: Todo Management
cd day-3
uvicorn main:app --reload

# Day 4: Quiz System
cd day-4
uvicorn main:app --reload

# Day 5: Full-Stack (Backend)
cd day-5/fastapi
uvicorn main:app --reload

# Day 5: Full-Stack (Frontend)
cd day-5/react/finance-app
npm start

# Day 6: Template Rendering
cd day-6
uvicorn main:app --reload
```

This repository represents a complete learning journey from FastAPI basics to production-ready full-stack applications with multiple database technologies and architectural patterns.