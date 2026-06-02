# CSV

The `csv()` source allows AQL to query CSV files using standard SQL-inspired syntax.

CSV files are treated as tabular data sources, making them accessible through the same query interface used for Aegis data, databases, and other supported formats.

---

## Discover the Source

List all available sources:

```bash
aegis query "SHOW sources"
```

Inspect a CSV file:

```bash
aegis query "SHOW csv('data.csv')"
```

---

## Inspect the Schema

View available columns:

```bash
aegis query "DESCRIBE csv('data.csv')"
```

Example output:

```text
id
name
email
department
created_at
```

Column names are automatically derived from the CSV header row.

---

## Query a CSV File

Return all rows:

```bash
aegis query "SELECT * FROM csv('data.csv')"
```

---

## Select Specific Columns

Retrieve only the columns you need:

```bash
aegis query "SELECT id FROM csv('data.csv')"
```

```bash
aegis query "SELECT id, name FROM csv('data.csv')"
```

---

## Filter Rows

Retrieve records matching a condition:

```bash
aegis query "SELECT * FROM csv('data.csv') WHERE id = 1"
```

Filter by multiple values:

```bash
aegis query "SELECT * FROM csv('data.csv') WHERE id IN [1, 5]"
```

---

## Query CSV Data from Standard Input

AQL can read CSV data directly from stdin.

Pipe a file into AQL:

```bash
cat data.csv | aegis query "SELECT *"
```

Explicitly reference stdin:

```bash
cat data.csv | aegis query "SELECT * FROM stdin"
```

Select specific columns:

```bash
cat data.csv | aegis query "SELECT id, name FROM stdin"
```

Apply filters:

```bash
cat data.csv | aegis query "SELECT * FROM stdin WHERE id = 1"
```

---

## Example CSV File

```csv
id,name,email
1,Alice,alice@example.com
2,Bob,bob@example.com
3,Carol,carol@example.com
```

Query:

```bash
aegis query "SELECT id, name FROM csv('data.csv')"
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
aegis query "DESCRIBE csv('data.csv')"
```

Then query the contents:

```bash
aegis query "SELECT * FROM csv('data.csv')"
```

---

### Extract Specific Data

```bash
aegis query "SELECT id, email FROM csv('data.csv')"
```

---

### Filter Records

```bash
aegis query "SELECT * FROM csv('data.csv') WHERE id = 1"
```

---

### Process Data in a Pipeline

```bash
cat data.csv | aegis query "SELECT * FROM stdin"
```

Useful when integrating AQL into shell scripts and automation workflows.

---

## Query Patterns

Select all columns:

```sql
SELECT * FROM csv('data.csv')
```

Select specific columns:

```sql
SELECT id, name
FROM csv('data.csv')
```

Filter records:

```sql
SELECT *
FROM csv('data.csv')
WHERE id = 1
```

Filter multiple values:

```sql
SELECT *
FROM csv('data.csv')
WHERE id IN [1, 5]
```

---

## Related Sources

* json()
* xml()
* yaml()
* stdin

All file-based sources support the same AQL query patterns, allowing you to work with structured data regardless of format.
