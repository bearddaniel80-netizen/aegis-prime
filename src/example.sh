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
    cmd="$*"

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

run_and_echo paged_cat data/aegis_last_run.json

sleep 2

run_and_echo aegis analyze

sleep 2

clear

# run_and_echo paged_cat data/aegis_production.json

# run_and_echo paged_cat data/aegis_clusters.json

run_and_echo aegis analyze explain

sleep 3

run_and_echo aegis report

# run_and_echo paged_cat data/aegis_report.html