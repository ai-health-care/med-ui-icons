#!/bin/bash

# generate dark icon set by replacing white --> black

scriptdir=$(dirname "$0")
cd "$scriptdir"

mkdir -p ../svg-dark
cp ../svg-white/*.svg ../svg-dark

for svg in ../svg-dark/*.svg; do
    sed -i 's/fill:#ffffff/#202020/g' "$svg"
done
