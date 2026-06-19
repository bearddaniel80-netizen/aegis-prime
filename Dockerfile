# ---------- deps ----------
FROM python:3.12-slim AS deps

WORKDIR /build

COPY requirements.txt .

RUN pip install --no-cache-dir \
    --prefix=/install \
    -r requirements.txt

# ---------- traceplan ----------
FROM deps AS traceplan

COPY --from=deps /install /usr/local

COPY src-traceplan/ .

RUN python -m build

RUN mv dist/*.whl /tmp/

RUN pip install /tmp/*.whl

WORKDIR /app

COPY traceplan-data .

# ---------- aql compliance ----------
FROM deps AS compliance

COPY --from=deps /install /usr/local

COPY src-aql-compliance .

RUN python -m build

RUN mv dist/*.whl /tmp/

RUN pip install /tmp/*.whl

WORKDIR /app

COPY aql-test .

# ---------- aegis ----------
FROM deps AS aegis

COPY --from=deps /install /usr/local

COPY src .

RUN python -m build

RUN mv dist/*.whl /tmp/

RUN pip install /tmp/*.whl

WORKDIR /app

COPY aegis .

# ---------- runtime ----------
FROM python:3.12-slim AS runtime

COPY --from=deps /install /usr/local

COPY --from=compliance /tmp/*.whl /tmp
RUN pip install /tmp/*.whl

COPY --from=aegis /tmp/*.whl /tmp/
RUN pip install /tmp/*.whl

WORKDIR /app

COPY --from=compliance /app .

COPY --from=aegis /app .

# CMD ["aegis"]