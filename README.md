# PleasQLarify: SQL Query Clarification System

This repository contains the code accompanying our CHI'26 publication.

## Overview

PleasQLarify is a system designed to help users clarify and understand SQL queries through interactive explanations and visualizations.

## Publication

If you use this code in your research, please cite our paper:

```bibtex
@inproceedings{pleasqlarify2026,
  title={PleasQLarify: Interactive SQL Query Clarification for End Users},
  author={Chan, Robin Shing Moon and others},
  booktitle={Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems},
  year={2026},
  publisher={ACM}
}
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/chanr0/pleasqlarify.git
cd pleasqlarify
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install the package:
```bash
pip install -e .
```

## Usage

### Basic Example

```python
from pleasqlarify import SQLClarifier

# Initialize the clarifier
clarifier = SQLClarifier()

# Clarify a SQL query
query = "SELECT * FROM users WHERE age > 25"
explanation = clarifier.clarify(query)
print(explanation)
```

### Command Line Interface

```bash
# Clarify a SQL query from command line
python -m pleasqlarify --query "SELECT * FROM users WHERE age > 25"

# Load query from file
python -m pleasqlarify --file query.sql
```

## Project Structure

```
pleasqlarify/
├── src/
│   └── pleasqlarify/       # Main package
│       ├── __init__.py
│       ├── clarifier.py    # Core clarification logic
│       ├── parser.py       # SQL parsing
│       └── visualizer.py   # Visualization components
├── examples/               # Example scripts and queries
├── data/                   # Sample datasets
├── tests/                  # Test suite
├── docs/                   # Documentation
├── requirements.txt        # Python dependencies
├── setup.py               # Package setup
├── LICENSE                # License file
└── README.md              # This file
```

## Features

- **Interactive Query Clarification**: Break down complex SQL queries into understandable components
- **Visual Explanations**: Generate visual representations of query structure and data flow
- **Natural Language Translation**: Convert SQL queries to natural language descriptions
- **Query Optimization Suggestions**: Provide recommendations for query improvements

## Examples

See the `examples/` directory for more detailed usage examples:

- `examples/basic_clarification.py` - Basic query clarification
- `examples/complex_queries.py` - Handling complex queries with joins and subqueries
- `examples/visualization.py` - Generating visual explanations

## Testing

Run the test suite:

```bash
pytest tests/
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or issues, please open an issue on GitHub or contact the authors.

## Acknowledgments

This work was supported by [funding sources]. We thank the participants in our user studies and the CHI community for their valuable feedback.