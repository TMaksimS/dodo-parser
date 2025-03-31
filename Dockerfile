FROM python:3.12.3-slim
COPY poetry.lock pyproject.toml ./
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install --only main --no-interaction --no-ansi --no-root
COPY . .
RUN rm -rf .venv
WORKDIR .
# CMD ["poetry", "run", "python3", "main.py"]