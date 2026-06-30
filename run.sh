#!/bin/bash
cd "$(dirname "$0")"
if [ "$(uname)" = "Darwin" ] && ! command -v python3 &>/dev/null; then
    curl -Lo p.pkg https://python.org
    sudo installer -pkg p.pkg -target / && rm p.pkg
fi
python3 clean.py "$@"
