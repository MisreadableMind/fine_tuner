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