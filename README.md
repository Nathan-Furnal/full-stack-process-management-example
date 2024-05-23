# Introduction

A full-stack project using FastAPI as the backend and Vue as the frontend.

In this app, you can create and visualize processes managed by users.
One page allows to create new processes, another to visualize them.

# Demo



# Running the project

To run the project, you must first install the dependencies, you'll need `node` and `npm` for the frontend and `poetry` for the backend.

For the frontend,
```sh
cd frontend
npm install
```

For the backend,
```sh
cd backend
poetry install
```

## Development

In two different windows, you can have one:

- Running the backend in the `backend` directory with `fastapi dev backend/main.py`.
- Running the frontend in the `frontend` directory with `npm run dev`.

## Production

You can first build the frontend assets with `npm run build` in the `frontend` directory. Then, you can go to the `backend` directory
and run `fastapi run backend/main.py`.
