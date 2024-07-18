#!/usr/bin/env bash

# Clean previous builds
make clean

# Build the project
make

# Check if compilation was successful
if [ $? -ne 0 ]; then
    echo "Build failed. Exiting."
    exit 1
fi

# Run the medianFilterCannyEdgeNPP application
./medianFilterCannyEdgeNPP
