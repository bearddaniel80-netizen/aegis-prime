# -------- Stage 1: Builder --------
FROM python:3.12-slim AS builder

WORKDIR /app

# Copy only requirements first (better caching)
COPY src/requirements.txt .

# Install Python deps into a separate location
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# -------- Stage 2: Final Runtime --------
FROM python:3.12-slim

ENV PYTHONPATH=/usr/local/lib/python3.12/site-packages

# Copy installed Python packages
COPY --from=builder /install /usr/local

WORKDIR /app

# Copy application code
COPY src/ .

RUN python -m build

RUN pip install /app/dist/*.whl

RUN chmod -R +x *

# RUN mkdir -p data \
#     && touch data/production.log \
#     && pytest tests > data/.aegis_last_run.txt