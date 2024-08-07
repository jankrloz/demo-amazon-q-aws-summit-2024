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

task: Available tasks for this project:

- `install`: 📦 Install dependencies
- `lint`: 🎨 Lint the code
- `lint:fix`: 🎨 Lint and fix the code
- `test`: 🧪 Test the code
- `test:watch`: 🧪 Test the code in watch mode
- `run`: 🚀 Run the application in development mode (aliases: dev, start, up)
- `run:watch`: 🚀 Run the application in development mode, and watch for changes for reloading (aliases: watch, dev:watch, start:watch, up:watch)
- `run:build`: 🚀 Build and run the application (aliases: dev:build, start:build, up:build)
- `restart`: 🚀 Restart the application (aliases: refresh)
- `stop`: 🛑 Stop the application
- `down`: 🔻 Stop the application, and remove the containers
- `clean:containers`: 🧼 Clean the application, and associacted resources, like images, volumes and networks
- `logs`: 🪵 Show the application logs
- `logs:db`: 🪵 Show the database logs

## Demo

### Instructions

1. run the app in MySQL 5.7
2. run the app in MySQL 8.0 (will fail)
3. go to a model (ex. app/models/user.py)
4. Use Amazon Q Chat to fix the model
5. Run again the app in MySQL 8.0 (will work)

### Amazon Q Prompts

- > Fix my SQL code to be compatible with MySQL 8.0 without changing the schema names.

- > How would my code look with the suggested changes?
