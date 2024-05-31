# Introduction

A full-stack project using FastAPI as the backend and Vue as the frontend.

In this fake app, you can create and visualize processes managed by users.
One page allows to create new processes, another to visualize them.

# Demo

Here under you'll see a short demo with the main components and interactions available to the user.

[Screencast_20240523_195502.webm](https://github.com/Nathan-Furnal/full-stack-process-management-example/assets/45597572/e1f7ca5a-4be8-4541-99a7-096360115d82)


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
