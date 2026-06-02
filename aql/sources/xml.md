# xml

The `xml()` source allows AQL to query xml files using standard SQL-inspired syntax.

xml files are treated as tabular data sources, making them accessible through the same query interface used for Aegis data, databases, and other supported formats.

---

## Discover the Source

List all available sources:

```bash
aegis query "SHOW sources"
```

Inspect a xml file:

```bash
aegis query "SHOW xml('data.xml')"
```

---

## Inspect the Schema

View available columns:

```bash
aegis query "DESCRIBE xml('data.xml')"
```

Example output:

```text
id
name
email
department
created_at
```

Column names are automatically derived from the xml header row.

---

## Query a xml File

Return all rows:

```bash
aegis query "SELECT * FROM xml('data.xml')"
```

---

## Select Specific Columns

Retrieve only the columns you need:

```bash
aegis query "SELECT id FROM xml('data.xml')"
```

```bash
aegis query "SELECT id, name FROM xml('data.xml')"
```

---

## Filter Rows

Retrieve records matching a condition:

```bash
aegis query "SELECT * FROM xml('data.xml') WHERE id = 1"
```

Filter by multiple values:

```bash
aegis query "SELECT * FROM xml('data.xml') WHERE id IN [1, 5]"
```

---

## Query xml Data from Standard Input

AQL can read xml data directly from stdin.

Pipe a file into AQL:

```bash
cat data.xml | aegis query "SELECT *"
```

Explicitly reference stdin:

```bash
cat data.xml | aegis query "SELECT * FROM stdin"
```

Select specific columns:

```bash
cat data.xml | aegis query "SELECT id, name FROM stdin"
```

Apply filters:

```bash
cat data.xml | aegis query "SELECT * FROM stdin WHERE id = 1"
```

---

## Example xml File

```xml
id,name,email
1,Alice,alice@example.com
2,Bob,bob@example.com
3,Carol,carol@example.com
```

Query:

```bash
aegis query "SELECT id, name FROM xml('data.xml')"
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
aegis query "DESCRIBE xml('data.xml')"
```

Then query the contents:

```bash
aegis query "SELECT * FROM xml('data.xml')"
```

---

### Extract Specific Data

```bash
aegis query "SELECT id, email FROM xml('data.xml')"
```

---

### Filter Records

```bash
aegis query "SELECT * FROM xml('data.xml') WHERE id = 1"
```

---

### Process Data in a Pipeline

```bash
cat data.xml | aegis query "SELECT * FROM stdin"
```

Useful when integrating AQL into shell scripts and automation workflows.

---

## Query Patterns

Select all columns:

```sql
SELECT * FROM xml('data.xml')
```

Select specific columns:

```sql
SELECT id, name
FROM xml('data.xml')
```

Filter records:

```sql
SELECT *
FROM xml('data.xml')
WHERE id = 1
```

Filter multiple values:

```sql
SELECT *
FROM xml('data.xml')
WHERE id IN [1, 5]
```

---

## Related Sources

* json()
* csv()
* yaml()
* stdin

All file-based sources support the same AQL query patterns, allowing you to work with structured data regardless of format.
