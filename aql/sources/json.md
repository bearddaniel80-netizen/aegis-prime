# json

The `json()` source allows AQL to query json files using standard SQL-inspired syntax.

json files are treated as tabular data sources, making them accessible through the same query interface used for Aegis data, databases, and other supported formats.

---

## Discover the Source

List all available sources:

```bash
aegis query "SHOW sources"
```

Inspect a json file:

```bash
aegis query "SHOW json('data.json')"
```

---

## Inspect the Schema

View available columns:

```bash
aegis query "DESCRIBE json('data.json')"
```

Example output:

```text
id
name
email
department
created_at
```

Column names are automatically derived from the json header row.

---

## Query a json File

Return all rows:

```bash
aegis query "SELECT * FROM json('data.json')"
```

---

## Select Specific Columns

Retrieve only the columns you need:

```bash
aegis query "SELECT id FROM json('data.json')"
```

```bash
aegis query "SELECT id, name FROM json('data.json')"
```

---

## Filter Rows

Retrieve records matching a condition:

```bash
aegis query "SELECT * FROM json('data.json') WHERE id = 1"
```

Filter by multiple values:

```bash
aegis query "SELECT * FROM json('data.json') WHERE id IN [1, 5]"
```

---

## Query json Data from Standard Input

AQL can read json data directly from stdin.

Pipe a file into AQL:

```bash
cat data.json | aegis query "SELECT *"
```

Explicitly reference stdin:

```bash
cat data.json | aegis query "SELECT * FROM stdin"
```

Select specific columns:

```bash
cat data.json | aegis query "SELECT id, name FROM stdin"
```

Apply filters:

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id = 1"
```

---

## Example json File

```json
id,name,email
1,Alice,alice@example.com
2,Bob,bob@example.com
3,Carol,carol@example.com
```

Query:

```bash
aegis query "SELECT id, name FROM json('data.json')"
```

Result:

```text
1 Alice
2 Bob
3 Carol
```

---

## Common Workflows

### Explore a New File

Inspect available columns:

```bash
aegis query "DESCRIBE json('data.json')"
```

Then query the contents:

```bash
aegis query "SELECT * FROM json('data.json')"
```

---

### Extract Specific Data

```bash
aegis query "SELECT id, email FROM json('data.json')"
```

---

### Filter Records

```bash
aegis query "SELECT * FROM json('data.json') WHERE id = 1"
```

---

### Process Data in a Pipeline

```bash
cat data.json | aegis query "SELECT * FROM stdin"
```

Useful when integrating AQL into shell scripts and automation workflows.

---

## Query Patterns

Select all columns:

```sql
SELECT * FROM json('data.json')
```

Select specific columns:

```sql
SELECT id, name
FROM json('data.json')
```

Filter records:

```sql
SELECT *
FROM json('data.json')
WHERE id = 1
```

Filter multiple values:

```sql
SELECT *
FROM json('data.json')
WHERE id IN [1, 5]
```

---

## Related Sources

* csv()
* xml()
* yaml()
* stdin

All file-based sources support the same AQL query patterns, allowing you to work with structured data regardless of format.
