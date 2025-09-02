#!/bin/bash

# SAGE Unified Feed - Quick Setup Script
echo "🌊 SAGE Unified Feed - Setup Script"
echo "===================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
echo "✅ Virtual environment created"
echo ""

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Check if database exists, if not it will be created on first run
if [ ! -f "demo_data.db" ]; then
    echo "📊 Database will be created on first run"
else
    echo "✅ Database already exists"
fi
echo ""

echo "🎉 Setup complete!"
echo ""
echo "To start the application:"
echo "  1. Activate the virtual environment: source venv/bin/activate"
echo "  2. Run the application: python app.py"
echo "  3. Open your browser to: http://localhost:5532"
echo ""
echo "Or simply run: ./run.sh"
