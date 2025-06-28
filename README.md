# Blood Test Report Analyser

A FastAPI-based application that uses AI to analyze blood test reports and provide comprehensive health recommendations.

## 🐛 **Debug Mode - All Bugs Fixed!** 

The following bugs have been identified and fixed:

### **Fixed Bugs:**

1. **agents.py**: 
   - ❌ **BUG**: `llm` variable was undefined
   - ✅ **FIX**: Added proper Google AI initialization with `ChatGoogleGenerativeAI`

2. **tools.py**: 
   - ❌ **BUG**: Missing `PDFLoader` import and incorrect async syntax
   - ✅ **FIX**: Added `PyPDFLoader` import and fixed method signatures

3. **main.py**: 
   - ❌ **BUG**: `file_path` parameter not being used in `run_crew`
   - ✅ **FIX**: Updated to pass `file_path` in context
   - ❌ **BUG**: Syntax error in query validation (`query==""`)
   - ✅ **FIX**: Fixed to `query == ""`

4. **task.py**: 
   - ❌ **BUG**: Task description didn't include `file_path` parameter
   - ✅ **FIX**: Updated task to use `{file_path}` parameter

5. **agents.py**: 
   - ❌ **BUG**: `tool` parameter should be `tools` (plural)
   - ✅ **FIX**: Changed to `tools=[...]`

6. **requirements.txt**: 
   - ❌ **BUG**: Missing critical dependencies
   - ✅ **FIX**: Added `langchain-google-genai`, `langchain-community`, `python-multipart`, etc.

## Getting Started

### 1. Install Required Libraries
```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables
Create a `.env` file in the root directory:
```bash
# Google AI API Key for Gemini Pro
GOOGLE_API_KEY=your_google_api_key_here

# Serper API Key for web search (optional)
SERPER_API_KEY=your_serper_api_key_here
```

### 3. Run the Application
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /`: Health check endpoint
- `POST /analyze`: Upload and analyze blood test reports

## Features

- PDF blood test report analysis
- AI-powered medical insights
- Comprehensive health recommendations
- Evidence-based medical advice

## Project Structure

```
blood-test-analyser-debug/
├── main.py              # FastAPI application
├── agents.py            # AI agents configuration
├── task.py              # Task definitions
├── tools.py             # Custom tools for PDF processing
├── requirements.txt     # Python dependencies
├── data/                # Sample PDF files
└── outputs/             # Generated outputs
```

## Dependencies

- FastAPI: Web framework
- CrewAI: Multi-agent framework
- LangChain: LLM integration
- Google AI: Gemini Pro model
- PyPDF2: PDF processing
