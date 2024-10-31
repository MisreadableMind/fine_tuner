#!/usr/bin/env python3
import os
import shutil
import stat
from pathlib import Path
import json

def create_file(filepath, content=''):
    """Create a file with given content."""
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(content)

def create_directory(dirpath):
    """Create a directory if it doesn't exist."""
    Path(dirpath).mkdir(parents=True, exist_ok=True)

def create_project_structure(base_path):
    """Create the full project structure with template files."""
    base_path = Path(base_path)
    
    # Create main project directory
    create_directory(base_path)

    # Create directory structure
    directories = [
        'data/raw',
        'data/processed',
        'data/results',
        'src/preparation',
        'src/training',
        'src/evaluation',
        'src/config',
        'scripts',
        'notebooks',
        'logs/fine_tuning',
        'logs/evaluation',
        'tests'
    ]

    for dir_path in directories:
        create_directory(base_path / dir_path)

    # Create template files
    files = {
        # Config files
        '.env.example': 'OPENAI_API_KEY=your-api-key-here\n',
        
        'requirements.txt': '''
openai>=1.0.0
numpy>=1.21.0
pandas>=1.3.0
pytest>=6.0.0
python-dotenv>=0.19.0
jupyter>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
'''.strip(),

        '.gitignore': '''
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Environment
.env
venv/
ENV/

# IDEs
.idea/
.vscode/
*.swp
*.swo

# Jupyter Notebook
.ipynb_checkpoints

# Project specific
data/raw/*
data/processed/*
logs/*
'''.strip(),

        # Source files
        'src/__init__.py': '',
        
        'src/preparation/__init__.py': '',
        'src/preparation/formatter.py': '''
import json

def convert_to_jsonl(input_file, output_file):
    """Convert input data to JSONL format for OpenAI fine-tuning."""
    # TODO: Implement conversion logic
    pass

def validate_format(file_path):
    """Validate if file follows OpenAI's JSONL format."""
    # TODO: Implement validation logic
    pass
'''.strip(),

        'src/training/__init__.py': '',
        'src/training/fine_tune.py': '''
from openai import OpenAI
from pathlib import Path

def create_fine_tune_job(training_file, validation_file=None, model="gpt-3.5-turbo"):
    """Create and start a fine-tuning job."""
    client = OpenAI()
    
    # TODO: Implement fine-tuning logic
    pass
'''.strip(),

        'src/config/openai_config.py': '''
# OpenAI API Configuration
DEFAULT_MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 4096
TEMPERATURE = 0.7

# Fine-tuning Configuration
TRAINING_PARAMS = {
    "n_epochs": 3,
    "batch_size": 8,
    "learning_rate": 1e-5
}
'''.strip(),

        # Scripts
        'scripts/prepare_data.py': '''
#!/usr/bin/env python3
import argparse
from pathlib import Path
from src.preparation.formatter import convert_to_jsonl

def main():
    parser = argparse.ArgumentParser(description='Prepare data for fine-tuning')
    parser.add_argument('--input', required=True, help='Input file path')
    parser.add_argument('--output', required=True, help='Output directory path')
    
    args = parser.parse_args()
    # TODO: Implement data preparation pipeline
    
if __name__ == '__main__':
    main()
'''.strip(),

        'scripts/run_fine_tuning.py': '''
#!/usr/bin/env python3
import argparse
from src.training.fine_tune import create_fine_tune_job

def main():
    parser = argparse.ArgumentParser(description='Run fine-tuning job')
    parser.add_argument('--training-file', required=True, help='Training data file path')
    parser.add_argument('--validation-file', help='Validation data file path')
    
    args = parser.parse_args()
    # TODO: Implement fine-tuning pipeline

if __name__ == '__main__':
    main()
'''.strip(),

        # Tests
        'tests/__init__.py': '',
        'tests/test_preparation.py': '''
import pytest
from src.preparation.formatter import convert_to_jsonl, validate_format

def test_convert_to_jsonl():
    # TODO: Implement test
    pass

def test_validate_format():
    # TODO: Implement test
    pass
'''.strip(),
    }

    # Create all files
    for file_path, content in files.items():
        create_file(base_path / file_path, content)

    # Make scripts executable
    for script in ['prepare_data.py', 'run_fine_tuning.py']:
        script_path = base_path / 'scripts' / script
        st = os.stat(script_path)
        os.chmod(script_path, st.st_mode | stat.S_IEXEC)

    # Create example notebook
    notebook_content = {
        "cells": [],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    for notebook in ['data_exploration.ipynb', 'format_checker.ipynb', 'results_analysis.ipynb']:
        create_file(base_path / 'notebooks' / notebook, json.dumps(notebook_content, indent=2))

    print(f"✨ Project structure created successfully at {base_path}")
    print("\nNext steps:")
    print("1. Create and activate a virtual environment:")
    print("   python -m venv venv")
    print("   source venv/bin/activate  # On Windows: .\\venv\\Scripts\\activate")
    print("2. Install dependencies:")
    print("   pip install -r requirements.txt")
    print("3. Copy .env.example to .env and add your OpenAI API key")
    print("4. Start with the notebooks in the notebooks/ directory")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Create OpenAI fine-tuning project structure')
    parser.add_argument('project_path', help='Path where the project should be created')
    
    args = parser.parse_args()
    create_project_structure(args.project_path)
