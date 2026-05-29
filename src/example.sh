#!/usr/bin/env bash
paged_cat() {
    local file="$1"

    if [[ ! -f "$file" ]]; then
        echo "Error: File not found: $file"
        return 1
    fi

    local count=0

    while IFS= read -r line; do
        echo "$line"
        ((count++))

        if (( count % 5 == 0 )); then
            sleep 2 # adjust speed here
        fi
    done < "$file"
}

run_and_echo() {
    local cmd="$*"

    # Ask for confirmation
    read -p "Run this command? '$cmd' [y/N]: " confirm

    case "$confirm" in
        [yY][eE][sS]|[yY])
            "$@"
            echo "Command was: $cmd"
            ;;
        *)
            echo "Cancelled."
            ;;
    esac
}

# touch data/aegis_clusters.json

run_and_echo pytest tests --json-report --json-report-file=data/aegis_last_run.json

run_and_echo aegis analyze

run_and_echo aegis analyze explain

run_and_echo aegis report

# run_and_echo paged_cat data/aegis_report.html

# [project.entry-points."aegis_prime.dialects"]
# mssql = "aegis_plugin_mssql.dialect:MSSQLDialect"

# [project.entry-points."aegis_prime.sources"]
# stdin = "aegis_plugin_stdin.source:stdin_source_factory"