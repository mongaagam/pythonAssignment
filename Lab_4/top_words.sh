FILE=$1

tr '[:upper:]' '[:lower:]' < "$FILE" \
| tr -cs '[:alpha:]' '\n' \
| sort \
| uniq -c \
| sort -nr \
| head
