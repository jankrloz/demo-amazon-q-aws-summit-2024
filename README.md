# Amazon Q Demo

> At AWS Summit 2024 CDMX

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Taskfile](https://taskfile.dev/)
- [Mise](https://mise-cli.dev/)
- [Poetry](https://python-poetry.org/)

## Setup

1. Install the required tools by following the installation instructions from the links above.

2. Clone the repository:

   ```bash
   git clone git@github.com:jankrloz/demo-amazon-q-aws-summit-2024.git
   cd project
   ```

3. Install project dependencies:

   ```bash
   task install
   ```

## Development

To start the development server, run:

```bash
task dev
# or
task watch # This will start the server and watch for changes, automatically reloading the server when necessary.
```

To see container logs, run:

```bash
task run
```

To stop the container, run:

```bash
task stop
```

To clean the container, images, volumes, and networks, run:

```bash
task clean:containers
```

## Additional Tasks

The Taskfile provides additional tasks for common operations.

Run
`task --list-all`
to see all available tasks.

## Demo

### Instructions

1. run the app in MySQL 5.7
2. run the app in MySQL 8.0 (will fail)
3. go to a model (ex. app/models/user.py)
4. Use Amazon Q Chat to fix the model
5. Run again the app in MySQL 8.0 (will work)

### Amazon Q Prompts
