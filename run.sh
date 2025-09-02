#!/bin/bash

# SAGE Unified Feed - Run Script
echo "🌊 Starting SAGE Unified Feed..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Running setup..."
    ./setup.sh
fi

# Activate virtual environment
source venv/bin/activate

# Run the application
python app.py
