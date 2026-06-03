# log

The `log()` source allows AQL to query log files using standard SQL-inspired syntax.

log files are treated as tabular data sources, making them accessible through the same query interface used for Aegis data, databases, and other supported formats.

---

## Discover the Source

List all available sources:

```bash
aegis query "SHOW sources"
```

Inspect a log file:

```bash
aegis query "SHOW log('data.log')"
```

---

## Inspect the Schema

View available columns:

```bash
aegis query "DESCRIBE log('data.log')"
```

Example output:

```text
line
line_number
```
AQL isn't trying to guess the structure.
It simply gives us the raw lines and their positions within the file.

By default log files will be parsed by newline. Future config file will allow custom parsing.

Examplle config:

```text
[source.logs.app]

path = "data.log"

pattern = "keyvalue"
```

---

## Query a log File

Return all rows:

```bash
aegis query "SELECT * FROM log('data.log')"
```

---

## Common Workflows

### Explore a New File

Inspect available columns:

```bash
aegis query "DESCRIBE log('data.log')"
```

Then query the contents:

```bash
aegis query "SELECT * FROM log('data.log')"
```

```

Useful when integrating AQL into shell scripts and automation workflows.

---

## Query Patterns

Select all columns:

```sql
SELECT * FROM log('data.log')
```

---

## Related Sources

* json()
* xml()
* csv()
* config builder

All file-based sources support the same AQL query patterns, allowing you to work with unstructured data regardless of format.
