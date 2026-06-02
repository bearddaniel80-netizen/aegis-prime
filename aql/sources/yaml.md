# yml

The `yaml()` source allows AQL to query yml files using standard SQL-inspired syntax.

yml files are treated as tabular data sources, making them accessible through the same query interface used for Aegis data, databases, and other supported formats.

---

## Discover the Source

List all available sources:

```bash
aegis query "SHOW sources"
```

Inspect a yml file:

```bash
aegis query "SHOW yaml('data.yml')"
```

---

## Inspect the Schema

View available columns:

```bash
aegis query "DESCRIBE yaml('data.yml')"
```

Example output:

```text
id
name
email
department
created_at
```

Column names are automatically derived from the yml header row.

---

## Query a yml File

Return all rows:

```bash
aegis query "SELECT * FROM yaml('data.yml')"
```

---

## Select Specific Columns

Retrieve only the columns you need:

```bash
aegis query "SELECT id FROM yaml('data.yml')"
```

```bash
aegis query "SELECT id, name FROM yaml('data.yml')"
```

---

## Filter Rows

Retrieve records matching a condition:

```bash
aegis query "SELECT * FROM yaml('data.yml') WHERE id = 1"
```

Filter by multiple values:

```bash
aegis query "SELECT * FROM yaml('data.yml') WHERE id IN [1, 5]"
```

---

## Query yml Data from Standard Input

AQL can read yml data directly from stdin.

Pipe a file into AQL:

```bash
cat data.yml | aegis query "SELECT *"
```

Explicitly reference stdin:

```bash
cat data.yml | aegis query "SELECT * FROM stdin"
```

Select specific columns:

```bash
cat data.yml | aegis query "SELECT id, name FROM stdin"
```

Apply filters:

```bash
cat data.yml | aegis query "SELECT * FROM stdin WHERE id = 1"
```

---

## Example yml File

```yml
id,name,email
1,Alice,alice@example.com
2,Bob,bob@example.com
3,Carol,carol@example.com
```

Query:

```bash
aegis query "SELECT id, name FROM yaml('data.yml')"
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
aegis query "DESCRIBE yaml('data.yml')"
```

Then query the contents:

```bash
aegis query "SELECT * FROM yaml('data.yml')"
```

---

### Extract Specific Data

```bash
aegis query "SELECT id, email FROM yaml('data.yml')"
```

---

### Filter Records

```bash
aegis query "SELECT * FROM yaml('data.yml') WHERE id = 1"
```

---

### Process Data in a Pipeline

```bash
cat data.yml | aegis query "SELECT * FROM stdin"
```

Useful when integrating AQL into shell scripts and automation workflows.

---

## Query Patterns

Select all columns:

```sql
SELECT * FROM yaml('data.yml')
```

Select specific columns:

```sql
SELECT id, name
FROM yaml('data.yml')
```

Filter records:

```sql
SELECT *
FROM yaml('data.yml')
WHERE id = 1
```

Filter multiple values:

```sql
SELECT *
FROM yaml('data.yml')
WHERE id IN [1, 5]
```

---

## Related Sources

* json()
* xml()
* csv()
* stdin

All file-based sources support the same AQL query patterns, allowing you to work with structured data regardless of format.
