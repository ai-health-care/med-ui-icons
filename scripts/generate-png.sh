#!/bin/bash

# generate dark icon set by replacing white --> black

scriptdir=$(dirname "$0")
cd "$scriptdir"

./dark-from-white.sh

mkdir -p ../png-white
mkdir -p ../png-dark

for svg in ../svg-white/*.svg; do
    png=../png-white/$(basename "$svg")
    inkscape "$svg" --export-type=png --export-filename="$png"
done

for svg in ../svg-dark/*.svg; do
    png=../png-dark/$(basename "$svg")
    inkscape "$svg" --export-type=png --export-filename="$png"
done
