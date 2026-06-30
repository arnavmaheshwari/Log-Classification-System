# Log Classification System

An intelligent, multi-layered log analysis and classification platform designed to automatically categorize system logs using a hybrid approach of RegEx, BERT embeddings, and LLM processing.

---

## Overview

The Log Classification System is a robust backend solution designed to ingest raw system logs, classify them into meaningful categories, and output structured data. It addresses the complexity of modern distributed systems by employing a tiered classification strategy:

1. **Rule-based Processing**: Rapid identification of known patterns via RegEx.
2. **ML Classification**: Contextual analysis of complex logs using BERT embeddings and scikit-learn models.
3. **Generative Intelligence**: High-level semantic reasoning for legacy system logs via Google Gemini LLM.

---

## Features

* **Hybrid Classification Engine**: Seamlessly switches between heuristic (RegEx) and probabilistic (BERT/LLM) models based on log source.
* **API-First Design**: Built with FastAPI for high-performance, asynchronous log processing.
* **Scalable ML Pipeline**: Utilizes pre-trained Sentence-Transformer models (`all-MiniLM-L6-v2`) for vectorization.
* **Legacy Support**: Dedicated LLM integration specifically for complex LegacyCRM log messages.
* **Batch Processing**: Supports CSV-based bulk classification and structured output generation.

---

## Tech Stack

| Category | Technology |
| --- | --- |
| **Backend** | Python 3.10, FastAPI |
| **ML/AI** | Sentence-Transformers, scikit-learn, LangChain, Google Gemini |
| **Data Processing** | Pandas, Joblib |
| **Utilities** | Uvicorn, python-dotenv |

---

## Project Structure

```text
├── Training/              # Notebooks and serialized ML models
├── __pycache__/           # Compiled Python files
├── log_classifier.py      # Core classification logic dispatcher
├── processor_bert.py      # BERT-based classification module
├── processor_llm.py       # LLM (Gemini) integration for legacy logs
├── processor_regex.py     # High-speed RegEx pattern matcher
├── server.py              # FastAPI application endpoints
├── How to run FastAPI.txt # Deployment instructions
└── test.csv               # Sample data for classification

```

---

## Getting Started

### Prerequisites

* Python 3.10+
* `pip` package manager
* A valid Google Gemini API Key

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd log-classification-system

```


2. Install dependencies:
```bash
pip install -r requirements.txt

```


3. Configure environment variables:
Create a `.env` file in the root directory:
```text
GEMINI_API_KEY=your_actual_api_key_here

```


4. Run the server:
```bash
uvicorn server:app --reload

```



---

## API Documentation

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | `/classify/` | Upload a CSV file (with `source` and `log_message` columns) for automated classification. |

---

## Deployment

The application is designed to be served via `uvicorn`. For production environments, it is recommended to containerize the application using Docker and deploy behind a reverse proxy (e.g., Nginx).

---

## Security

* **Input Validation**: Strict validation for CSV file extensions and required column headers (`source`, `log_message`).
* **Environment Security**: API keys are handled via `.env` files using `python-dotenv` to ensure secrets are not hardcoded in source control.
* **Resource Cleanup**: Automatic file handling with error catching to ensure system resources are released after processing.

---

## Future Improvements

* **Async Model Loading**: Refactor model initialization to support lazy loading for faster startup times.
* **Vector Database Integration**: Replace local Joblib models with a vector database (e.g., ChromaDB or FAISS) for handling larger classification datasets.
* **Enhanced Monitoring**: Add Prometheus metrics to track classification latency and model confidence scores.

---

## License

This project is licensed under the MIT License.

---

## Author

**Arnav Maheshwari**
