# Sheet-Agent

A generalist agent for spreadsheet reasoning and manipulation powered by Large Language Models (LLMs). Sheet-Agent enables intelligent automation of complex spreadsheet tasks through natural language processing and multi-step reasoning capabilities.

## 🚀 Features

- **Natural Language Processing**: Interact with spreadsheets using plain English commands
- **Multi-step Reasoning**: Handle complex, long-horizon manipulation tasks that require logical reasoning
- **Cross-format Support**: Work with various spreadsheet formats (Excel, Google Sheets, CSV)
- **Intelligent Data Analysis**: Automatically analyze and understand spreadsheet structure and content
- **Automated Calculations**: Perform complex calculations and data transformations
- **Error Detection**: Identify and suggest fixes for common spreadsheet errors
- **Template Generation**: Create spreadsheet templates based on requirements

## 📋 Prerequisites

- Python 3.8 or higher
- API access to a supported LLM (OpenAI GPT, Claude, etc.)
- Required Python packages (see requirements.txt)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/debraj-m/Sheet-Agent.git
cd Sheet-Agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
export OPENAI_API_KEY="your-api-key-here"
# or create a .env file with your API keys
```

## 🎯 Quick Start

### Basic Usage

```python
from sheet_agent import SheetAgent

# Initialize the agent
agent = SheetAgent()

# Load a spreadsheet
agent.load_spreadsheet("data.xlsx")

# Perform operations using natural language
result = agent.execute("Calculate the average sales for each region and create a summary table")

# Save the results
agent.save("output.xlsx")
```

### Command Line Interface

```bash
# Process a single command
python sheet_agent.py --file "data.xlsx" --command "Sort data by date and remove duplicates"

# Interactive mode
python sheet_agent.py --interactive
```

## 📖 Usage Examples

### Data Analysis
```python
# Analyze sales data
agent.execute("Find the top 10 customers by revenue and highlight them in yellow")

# Generate insights
agent.execute("Create a pivot table showing monthly sales trends by product category")
```

### Data Cleaning
```python
# Clean messy data
agent.execute("Remove empty rows, standardize date formats, and fix spelling errors in product names")

# Validate data
agent.execute("Check for duplicate entries and flag any inconsistencies in the price column")
```

### Report Generation
```python
# Create reports
agent.execute("Generate a quarterly sales report with charts and key metrics")

# Format for presentation
agent.execute("Apply professional formatting and add conditional formatting to highlight important values")
```

## 🏗️ Architecture

Sheet-Agent is built with a modular architecture:

- **Core Engine**: LLM-powered reasoning and planning
- **Spreadsheet Parser**: Multi-format file handling and data extraction
- **Action Executor**: Implements specific spreadsheet operations
- **Natural Language Interface**: Command interpretation and response generation
- **Memory System**: Maintains context across multi-step operations

## 🔧 Configuration

Create a `config.yaml` file to customize behavior:

```yaml
llm:
  provider: "openai"  # or "anthropic", "huggingface"
  model: "gpt-4"
  temperature: 0.1

spreadsheet:
  max_rows: 100000
  supported_formats: ["xlsx", "xls", "csv", "ods"]
  
output:
  default_format: "xlsx"
  include_metadata: true
```

## 📚 API Reference

### SheetAgent Class

#### Methods

- `load_spreadsheet(file_path: str)` - Load a spreadsheet file
- `execute(command: str) -> Dict` - Execute a natural language command
- `save(file_path: str, format: str = None)` - Save the current spreadsheet
- `get_schema() -> Dict` - Get spreadsheet structure information
- `rollback(steps: int = 1)` - Undo recent operations

#### Properties

- `current_sheet` - Currently active worksheet
- `operation_history` - List of performed operations
- `data_summary` - Basic statistics about the data

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m pytest tests/

# Run specific test categories
python -m pytest tests/test_parsing.py
python -m pytest tests/test_operations.py

# Run with coverage
python -m pytest --cov=sheet_agent tests/
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- [SheetRM Benchmark](https://sheetagent.github.io/) - Evaluation benchmark for spreadsheet reasoning
- [LangChain](https://github.com/hwchase17/langchain) - Framework for LLM applications
- [OpenPyXL](https://openpyxl.readthedocs.io/) - Python library for Excel files

## 📞 Support

- **Documentation**: [Wiki](https://github.com/debraj-m/Sheet-Agent/wiki)
- **Issues**: [GitHub Issues](https://github.com/debraj-m/Sheet-Agent/issues)
- **Discussions**: [GitHub Discussions](https://github.com/debraj-m/Sheet-Agent/discussions)

## 🙏 Acknowledgments

- Thanks to the open-source community for inspiration and tools
- Built upon research in LLM-powered automation
- Special thanks to contributors and testers

## 📊 Performance

Sheet-Agent has been tested on:
- Large datasets (up to 1M rows)
- Complex multi-step operations
- Various spreadsheet formats and structures
- Real-world business scenarios

Performance benchmarks and detailed evaluations are available in the [benchmarks](benchmarks/) directory.

---

**Made with ❤️ by [Debraj](https://github.com/debraj-m)**
