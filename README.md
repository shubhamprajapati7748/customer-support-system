# Customer Support System with RAG

A powerful customer support system built using FastAPI and LangChain, implementing Retrieval-Augmented Generation (RAG) for intelligent customer query responses.

## Features

- FastAPI-based web application
- RAG implementation for context-aware responses
- Google's Generative AI integration
- Interactive chat interface
- Document retrieval system
- Customizable prompt templates

## Project Structure

```
├── config/             # Configuration files
├── data/              # Data storage
├── data_ingestion/    # Data processing scripts
├── prompt_library/    # Custom prompt templates
├── retriever/         # Document retrieval system
├── static/           # Static files (CSS, JS)
├── templates/        # HTML templates
├── utils/            # Utility functions
├── main.py           # FastAPI application
└── requirements.txt  # Project dependencies
```

## Prerequisites

- Python 3.10
- Conda (for environment management)
- Google API credentials (for Gemini integration)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/shubhamprajapati7748/customer-support-system
cd customer-support-system
```

2. Create and activate the conda environment:
```bash
conda create -p venv python=3.10 -y
conda activate venv
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory and add your Google API credentials:
```
GOOGLE_API_KEY=your_api_key_here
```

## Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload --port 8001
```

The application will be available at `http://localhost:8001`

## Usage

1. Open your web browser and navigate to `http://localhost:8001`
2. Use the chat interface to interact with the customer support system
3. The system will retrieve relevant information and generate context-aware responses

## Development

- The main application logic is in `main.py`
- Custom prompts can be modified in the `prompt_library/` directory
- Document retrieval system is implemented in the `retriever/` directory
- Frontend templates are located in the `templates/` directory

## Contributing

Contributions to the Google Gemini-Pro Chat Application are welcome! If you have suggestions, enhancements, or bug fixes, please follow the steps below:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

- Shubham Prajapati - [shubhamprajapati7748@gmail.com](mailto:shubhamprajapati7748@gmail.com)
