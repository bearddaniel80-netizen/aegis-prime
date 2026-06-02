# STDIN

The `stdin` source allows AQL to query data streamed through standard input.

Unlike file-based sources such as `json()`, `csv()`, `xml()`, and `yaml()`, the `stdin` source reads data directly from a Unix pipeline.

Supported formats include:

* JSON
* CSV
* XML
* YAML

AQL automatically detects and parses supported input formats.

---

## When to Use STDIN

Use `stdin` when data is being streamed from another command or when integrating AQL into shell scripts and automation workflows.

Examples:

```bash
cat data.json | aegis query "SELECT *"
```

```bash
curl https://example.com/data.json | aegis query "SELECT *"
```

```bash
echo '{"id":1,"name":"Alice"}' | aegis query "SELECT *"
```

---

## Supported Query Patterns

### Discover Available Fields

```bash
cat data.json | aegis query "SHOW stdin"
```

### Inspect the Schema

```bash
cat data.json | aegis query "DESCRIBE stdin"
```

### Query All Data

```bash
cat data.json | aegis query "SELECT *"
```

```bash
cat data.json | aegis query "SELECT * FROM stdin"
```

### Select Specific Fields

```bash
cat data.json | aegis query "SELECT id, name"
```

```bash
cat data.json | aegis query "SELECT id, name FROM stdin"
```

### Filter Results

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id = 1"
```

### Select and Filter

```bash
cat data.json | aegis query "SELECT name FROM stdin WHERE id = 1"
```

---

## Query Grammar

The following query patterns are supported:

```sql
SHOW stdin
```

```sql
DESCRIBE stdin
```

```sql
SELECT *
```

```sql
SELECT * FROM stdin
```

```sql
SELECT field1, field2
```

```sql
SELECT field1, field2 FROM stdin
```

```sql
SELECT *
FROM stdin
WHERE condition
```

```sql
SELECT field1, field2
FROM stdin
WHERE condition
```

---

## JSON Example

Input:

```bash
cat users.json
```

```json
[
  {
    "id": 1,
    "name": "Alice"
  },
  {
    "id": 2,
    "name": "Bob"
  }
]
```

Query:

```bash
cat users.json | aegis query "SELECT id, name"
```

---

## CSV Example

Input:

```csv
id,name
1,Alice
2,Bob
```

Query:

```bash
cat users.csv | aegis query "SELECT *"
```

---

## XML Example

Query:

```bash
cat users.xml | aegis query "SELECT *"
```

---

## YAML Example

Query:

```bash
cat users.yml | aegis query "SELECT *"
```

---

## Using Echo

AQL can query inline data streamed directly from the shell.

JSON:

```bash
echo '{"id":1,"name":"Alice"}' | aegis query "SELECT *"
```

CSV:

```bash
echo 'id,name
1,Alice' | aegis query "SELECT *"
```

YAML:

```bash
echo 'id: 1
name: Alice' | aegis query "SELECT *"
```

---

## Common Workflows

### Inspect Incoming Data

```bash
cat data.json | aegis query "DESCRIBE stdin"
```

Useful when exploring an unfamiliar dataset.

---

### Filter Streamed Data

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id = 1"
```

Useful for extracting specific records from larger datasets.

---

### Select Only Required Fields

```bash
cat data.json | aegis query "SELECT id, name FROM stdin"
```

Useful for reducing output and focusing on relevant data.

---

### Use AQL in Shell Pipelines

```bash
curl https://example.com/users.json \
| aegis query "SELECT id, name FROM stdin"
```

Useful for automation and command-line workflows.

---

## Related Sources

* json()
* csv()
* xml()
* yaml()

Use file-based sources when querying data stored on disk, and use `stdin` when data is streamed from another command or pipeline.
