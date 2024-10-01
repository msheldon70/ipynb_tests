#!/bin/bash

# Parse command line options.
if [ $# -ne 1 ]; then
    echo "Error: Only one argument is allowed." >&2
    exit 1
fi

case "$1" in
    -a|--apple)
        echo "You selected apple."
        ;;
    -b|--banana)
        echo "You selected banana."
        ;;
    -c|--cherry)
        echo "You selected cherry."
        ;;
    *)
        echo "Error: Unsupported argument $1" >&2
        exit 1
        ;;
esac
eval set -- "$PARAMS"