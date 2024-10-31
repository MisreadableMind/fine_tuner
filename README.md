# Fine-Tuner: OpenAI Model Fine-Tuning Pipeline

A toolkit for fine-tuning models with robust data preparation, training, and evaluation workflows.

## 🎯 Features

- Data preparation and validation for JSONL format
- Automated fine-tuning pipeline with API integration
- Evaluation metrics and visualization tools
- Configurable parameters for various use cases
- Detailed logging and experiment tracking

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fine_tuner.git
cd fine_tuner
```

2. Set up your environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure OpenAI credentials:
```bash
cp .env.example .env
# Edit .env with your OpenAI API key
```

4. Prepare your data:
```bash
python scripts/prepare_data.py --input data/raw/your_data.csv --output data/processed/
```

5. Run fine-tuning:
```bash
python scripts/run_fine_tuning.py --training-file data/processed/training.jsonl
```

## 📁 Project Structure

```
fine_tuner/
├── data/                       # Data storage
├── src/                       # Source code
├── scripts/                   # Pipeline scripts
├── notebooks/                 # Jupyter notebooks
├── logs/                      # Training logs
└── tests/                     # Unit tests
```

## 🛠️ Main Components

### Data Preparation (`src/preparation/`)
- Format conversion to JSONL
- Data cleaning and preprocessing
- Format validation
- Dataset splitting

### Training (`src/training/`)
- OpenAI API integration
- Fine-tuning job management
- Training monitoring
- Checkpoint handling

### Evaluation (`src/evaluation/`)
- Performance metrics calculation
- Results visualization
- Model comparison tools
- Error analysis

## 📊 Data Format

Your input data should be structured as follows:

```json
{
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a story about a cat."},
        {"role": "assistant", "content": "Once upon a time..."}
    ]
}
```

## ⚙️ Configuration

Edit `src/config/openai_config.py` to customize:
- Model parameters
- Training settings
- Evaluation metrics
- API configurations

## 📝 Usage Examples

### Data Preparation
```python
from src.preparation import formatter

# Convert your data to JSONL format
formatter.convert_to_jsonl(
    input_file="data/raw/conversations.csv",
    output_file="data/processed/training.jsonl"
)
```

### Fine-Tuning
```python
from src.training import fine_tune

# Start fine-tuning
job = fine_tune.create_job(
    training_file="data/processed/training.jsonl",
    validation_file="data/processed/validation.jsonl",
    model="gpt-3.5-turbo"
)
```

### Evaluation
```python
from src.evaluation import metrics

# Evaluate model performance
results = metrics.evaluate_model(
    model_id="your-fine-tuned-model",
    test_file="data/processed/test.jsonl"
)
```

## 📊 Monitoring & Visualization

Use the provided notebooks to:
- Explore your dataset
- Verify data format
- Analyze training results
- Visualize model performance

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/
```

## 📈 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Support

For support and questions:
- Open an issue
- Check existing [documentation](docs/)
- Review closed issues for solutions

## ✨ Acknowledgments

- Contributors to this project
- The open-source community

---
Made with ❤️ by Vitalii Ratushnyi
