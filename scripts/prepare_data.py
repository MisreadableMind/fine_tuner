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