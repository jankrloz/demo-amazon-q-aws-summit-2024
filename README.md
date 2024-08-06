# Project Name

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Taskfile](https://taskfile.dev/)
- [Mise](https://mise-cli.dev/)
- [Poetry](https://python-poetry.org/)

## Setup

1. Install the required tools by following the installation instructions from the links above.

2. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/project.git
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
```

This will start the server and watch for changes, automatically reloading the server when necessary.

## Additional Tasks

The Taskfile provides additional tasks for common operations. Run
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
