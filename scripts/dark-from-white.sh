#!/bin/bash

# generate dark icon set by replacing white --> black

scriptdir=$(dirname "$0")
cd "$scriptdir"

mkdir -p ../svg-dark
cp ../svg-white/*.svg ../svg-dark

for svg in ../svg-dark/*.svg; do
    # replace white --> black
    sed -i 's/fill:#ffffff/fill:#202020/g' "$svg"
    # replace green
    sed -i 's/#87deaa/#008033/g' "$svg"
    # replace blue
    sed -i 's/#87aade/#3771c8/g' "$svg"
    # replace yellow
    sed -i 's/#ffcc00/#aa8800/g' "$svg"
done
