# Blood Test Report Analyser

A FastAPI-based application that uses CrewAI to analyze blood test reports and provide medical, nutritional, and exercise recommendations. The system leverages multiple AI agents to process PDF reports and respond to user queries.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Overview
The Blood Test Report Analyser is a Python application built with FastAPI and CrewAI. It processes uploaded PDF blood test reports and provides comprehensive health recommendations using specialized AI agents:
- **Doctor Agent**: Analyzes blood test results and provides medical advice.
- **Verifier Agent**: Validates the uploaded file as a blood test report.
- **Nutritionist Agent**: Offers dietary and supplement recommendations.
- **Exercise Specialist Agent**: Creates tailored exercise plans.

**Note**: This system is designed for experimental or satirical use. It should not be used for real medical advice without proper validation and professional oversight.

## Features
- Upload PDF blood test reports via a REST API.
- Process user queries with AI-driven analysis.
- Multi-agent system for medical, nutritional, and exercise recommendations.
- Temporary file storage with automatic cleanup.
- Configurable via environment variables for LLM and API keys.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/blood-test-report-analyser.git
   cd blood-test-report-analyser
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with the following variables:
   ```plaintext
   OPENAI_API_KEY=your-openai-api-key
   SERPER_API_KEY=your-serper-api-key
   ```

## Usage
1. Start the FastAPI server:
   ```bash
   python main.py
   ```

2. The API will be available at `http://localhost:8000`.

3. Use the `/analyze` endpoint to upload a PDF blood test report and provide a query (optional).

## API Endpoints
- **GET /**: Health check endpoint.
  - Response: `{"message": "Blood Test Report Analyser API is running"}`

- **POST /analyze**: Analyze a blood test report.
  - Request:
    - `file`: PDF file (required)
    - `query`: User query (optional, defaults to "Summarize my Blood Test Report")
  - Example:
    ```bash
    curl -X POST -F "file=@sample_blood_report.pdf" -F "query=Summarize my blood test" http://localhost:8000/analyze
    ```
  - Response:
    ```json
    {
      "status": "success",
      "query": "Summarize my Blood Test Report",
      "analysis": "...",
      "file_processed": "sample_blood_report.pdf"
    }
    ```

## Project Structure
```
blood-test-report-analyser/
├── agents.py         # Defines AI agents (Doctor, Verifier, Nutritionist, Exercise Specialist)
├── tools.py          # Custom tools for PDF reading, nutrition, and exercise planning
├── task.py           # Task definitions for CrewAI
├── main.py           # FastAPI application
├── requirements.txt  # Project dependencies
├── data/             # Temporary storage for uploaded files
├── .env             # Environment variables (not tracked in git)
└── README.md        # This file
```

## Dependencies
Key dependencies include:
- `fastapi==0.110.3`: Web framework for the API.
- `crewai==0.130.0`: Multi-agent orchestration framework.
- `langchain-community==0.0.38`: For PDF loading (`PyPDFLoader`).
- `langchain-openai==0.1.7`: For LLM integration.
- See `requirements.txt` for the full list.

## Environment Variables
Create a `.env` file with:
```plaintext
OPENAI_API_KEY=your-openai-api-key
SERPER_API_KEY=your-serper-api-key
```

- `OPENAI_API_KEY`: Required for the LLM (e.g., GPT-4o-mini).
- `SERPER_API_KEY`: Optional, for web search functionality (if used).

## Running the Application
1. Ensure the `.env` file is configured.
2. Run the server:
   ```bash
   python main.py
   ```
3. The API will be available at `http://localhost:8000`.

## Testing
Test the API using tools like `curl`, Postman, or a custom client:
```bash
curl -X POST -F "file=@sample_blood_report.pdf" -F "query=What are my health risks?" http://localhost:8000/analyze
```

To test locally:
1. Prepare a sample PDF blood test report.
2. Use the `/analyze` endpoint to verify the response includes medical, nutritional, and exercise advice.

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

**Disclaimer**: This system is for experimental purposes only. Do not use it for actual medical advice without consulting a licensed healthcare professional.
