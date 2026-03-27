#!/bin/bash

if [ -f "boxplot.png" ]; then
    echo "boxplot.png exists."
else
    echo "boxplot.png does not exist."
    exit 1
fi