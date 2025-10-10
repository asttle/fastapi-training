# Day 5: FastAPI & React Integration

Welcome to Day 5 of the FastAPI Training! Today, you'll work on integrating a FastAPI backend with a React frontend.

## Project Structure

```
fastapi-training/
├── fastapi/   # FastAPI backend code
├── react/     # React frontend code
└── day-5/
    └── README.md
```

## Objectives

- Set up FastAPI as a REST API server.
- Build a React frontend to interact with the FastAPI backend.
- Connect the frontend and backend for full-stack development.

## Tasks

1. **FastAPI Backend**
   - Implement API endpoints for data retrieval and manipulation.
   - Enable CORS to allow requests from the React frontend.

2. **React Frontend**
   - Create components to fetch and display data from FastAPI.
   - Handle user interactions and send requests to the backend.

3. **Integration**
   - Test communication between React and FastAPI.
   - Debug and resolve any issues with API calls.

## Getting Started

1. Start the FastAPI server:
   ```bash
   cd fastapi
   uvicorn main:app --reload
   ```

2. Start the React development server:
   ```bash
   cd react
   npm start
   ```

3. Access the React app in your browser and verify backend connectivity.

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)

---

Happy coding!