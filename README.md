# AI-document-Analyser
# Financial Document Intelligence Agent for SMEs

> An agentic AI system that autonomously analyzes financial documents uploaded by Small and Medium Enterprises (SMEs), identifies financial gaps, and generates forward-looking business flags.

## Overview

Small and Medium Enterprises generate large volumes of financial data through invoices, bank statements, profit & loss statements, balance sheets, and cash-flow reports.

However, many SMEs do not have the resources to continuously analyze these documents and convert raw financial information into actionable insights.

This project addresses that gap by building an **Agentic AI-powered Financial Document Intelligence System**.

The system accepts financial documents from an SME owner and autonomously analyzes them to provide:

1. **Current State Analysis**
2. **Gap Detection**
3. **Forward-Looking Flags**

The goal is not simply to summarize financial documents, but to interpret the information and highlight important financial signals.

The original challenge requires the agent to initiate analysis from document upload rather than waiting for a user query, while keeping every derived insight traceable to the uploaded source.

---

## Problem Statement

SME owners often make important business decisions without having a complete and timely understanding of their financial position.

This can lead to situations such as:

* Unexpected cash-flow gaps
* Delayed vendor payments
* Poor receivables tracking
* Unmonitored expense growth
* Weak financial ratio monitoring
* Difficulty identifying financial risks early

The core challenge is not the absence of financial data, but the difficulty of **interpreting that data at the right time**.

---

## Our Solution

We propose an **Agentic Financial Intelligence System** that automatically starts processing when financial documents are uploaded.

### Input

The system can process supported financial documents such as:

* PDF financial statements
* CSV files
* Excel spreadsheets
* Scanned financial documents/images
* Other supported financial records

### Processing

The agent:

1. Detects the uploaded document type
2. Extracts relevant financial information
3. Structures the extracted information
4. Performs financial calculations
5. Identifies missing information
6. Analyzes financial patterns
7. Generates current-state insights
8. Generates forward-looking risk flags
9. Connects each insight back to its source

### Output

The system produces a structured financial intelligence report containing:

* Current financial position
* Key financial metrics
* Important financial trends
* Detected gaps
* Receivables-related risks
* Expense anomalies
* Cash-flow concerns
* Forward-looking flags
* Source references

---

# Key Features

## 1. Current State Analysis

The agent extracts and interprets important financial signals from uploaded documents.

Instead of simply producing a summary, it attempts to explain what the financial numbers indicate.

Example insights include:

* Liquidity analysis
* Profit margin trends
* Revenue concentration
* Expense patterns
* Cash-flow position
* Financial ratio analysis

The challenge specifically calls for a reasoned interpretation of financial signals rather than a basic document summary.

---

## 2. Gap Detection

The system identifies important information that is missing or incomplete from the uploaded document set.

For every detected gap, the system explains:

* What information is missing
* Why it matters
* Which financial analysis is affected
* What decision cannot be reliably made because of the missing information

For example:

> **Missing:** Accounts receivable aging data
> **Impact:** Receivables risk and collection efficiency cannot be fully assessed.

The goal is to treat missing information as a useful reminder rather than simply an error.

---

## 3. Forward-Looking Flags

The system identifies patterns that may require attention based on the current financial trajectory.

These are **not predictions**.

Instead, they are signals derived from observed financial patterns.

Examples:

* Potential cash-flow pressure
* Increasing receivables risk
* High expense growth
* Seasonal financial pressure
* Reduced financial runway

The challenge describes these as reasoned observations rather than definitive predictions.

---

## 4. Source Traceability

Every important financial insight should be traceable back to the uploaded document.

The system avoids creating unsupported financial figures.

If a required figure cannot be derived from the uploaded information, the system explicitly reports that the information is unavailable rather than estimating it.

This is an important requirement of the challenge.

---

## 5. Autonomous Agent Workflow

Unlike a traditional chatbot that waits for a question, this system initiates analysis after document upload.

### Workflow

```text
             ┌──────────────────────┐
             │   Upload Documents   │
             └──────────┬───────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │ Document Processing  │
             └──────────┬───────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │ Data Extraction      │
             └──────────┬───────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │ Financial Analysis   │
             └──────────┬───────────┘
                        │
              ┌─────────┼─────────┐
              ▼         ▼         ▼
        Current State   Gap    Forward-Looking
         Analysis     Detection     Flags
              │         │         │
              └─────────┼─────────┘
                        ▼
             ┌──────────────────────┐
             │ Structured Report   │
             └──────────────────────┘
```

---

# Agent Reasoning Flow

The agent follows a structured reasoning pipeline:

```text
Document Upload
      ↓
Document Classification
      ↓
Information Extraction
      ↓
Data Validation
      ↓
Financial Metric Calculation
      ↓
Pattern & Trend Analysis
      ↓
Gap Detection
      ↓
Risk / Signal Identification
      ↓
Source Verification
      ↓
Financial Intelligence Report
```

---

# Example Output

## Current State

```text
Revenue: ₹25,00,000
Expenses: ₹18,00,000
Profit: ₹7,00,000

Observation:
The business is currently profitable, with expenses representing
a significant portion of revenue.
```

## Gap Detection

```text
Missing Information:
Accounts Receivable Aging

Why it matters:
Without receivables aging data, the system cannot reliably assess
collection delays or customer payment risk.
```

## Forward-Looking Flag

```text
Flag:
Receivables should be monitored closely.

Reason:
The available financial information indicates that outstanding
receivables may affect future cash availability.

Note:
This is a financial signal, not a prediction.
```

---

# Technology Stack

The implementation can be built using an agentic AI architecture.

### AI / Agent Layer

* Python
* LangGraph
* LangChain
* Large Language Model APIs
* Prompt Engineering
* Agentic AI workflows

### Data Processing

* Pandas
* NumPy
* PDF processing
* Excel/CSV processing
* Structured data extraction

### Retrieval / Knowledge Layer

* RAG
* Embeddings
* Vector Database
* ChromaDB / FAISS

### Backend

* FastAPI / Flask

### Frontend

* Streamlit / React

### Database

* SQLite / PostgreSQL

### Deployment

* Docker
* Cloud deployment

> Replace the technology names above with the exact technologies used in the final implementation.

---

# Project Architecture

```text
                    ┌─────────────────┐
                    │     SME User    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Document Upload │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Document Router │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
          PDF Parser     Excel/CSV      Image/OCR
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                    ┌─────────────────┐
                    │ Data Extraction │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Validation      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Agent / LLM     │
                    │ Reasoning Layer │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
         Current State    Gap Detection   Forward Flags
          Analysis
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                    ┌─────────────────┐
                    │ Source Tracing  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Final Report    │
                    └─────────────────┘
```

---

# Supported Analysis

Depending on the available documents, the system can analyze:

### Profitability

* Revenue
* Expenses
* Gross profit
* Net profit
* Profit margins

### Liquidity

* Current ratio
* Cash position
* Short-term obligations

### Expenses

* Expense categories
* Unusual increases
* Recurring expenses
* Expense concentration

### Receivables

* Outstanding invoices
* Due dates
* Payment status
* Receivables aging
* Collection-related signals

### Cash Flow

* Cash inflows
* Cash outflows
* Burn rate
* Potential cash-flow pressure

### Financial Gaps

* Missing statements
* Missing periods
* Missing financial metrics
* Incomplete transaction information

---

# Safety & Boundaries

The system is designed as a **financial intelligence and analysis tool**, not a financial advisor.

It does **not** provide:

* Tax guidance
* Investment recommendations
* Unsupported financial predictions
* Fabricated financial figures

If information is unavailable, the system should clearly state that it cannot derive the requested metric from the available documents.

The project brief explicitly requires the agent to define where analysis ends and advice begins, and prohibits crossing into tax guidance or investment recommendations.

---

# Dataset

The hackathon brief provides several recommended datasets that can be used as mock financial inputs, including:

* Financial statements
* Profit & Loss statements
* Financial transaction data
* Customer invoice data
* Synthetic financial transactions
* SME financial decision-making datasets

These datasets are intended to support development and testing of the reasoning pipeline rather than requiring real client financial documents.

---

# Project Structure

```text
financial-document-intelligence-agent/
│
├── app/
│   ├── agents/
│   │   ├── financial_agent.py
│   │   ├── analysis_agent.py
│   │   └── gap_detection_agent.py
│   │
│   ├── document_processing/
│   │   ├── pdf_processor.py
│   │   ├── csv_processor.py
│   │   ├── excel_processor.py
│   │   └── document_classifier.py
│   │
│   ├── analysis/
│   │   ├── ratios.py
│   │   ├── trends.py
│   │   ├── anomaly_detection.py
│   │   └── cashflow.py
│   │
│   ├── rag/
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   └── retriever.py
│   │
│   ├── api/
│   │   └── routes.py
│   │
│   └── utils/
│       └── helpers.py
│
├── data/
│   └── sample/
│
├── tests/
│
├── frontend/
│
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── main.py
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/financial-document-intelligence-agent.git

cd financial-document-intelligence-agent
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file:

```env
LLM_API_KEY=your_api_key
```

Do not commit your `.env` file to GitHub.

## 5. Run the Application

```bash
python main.py
```

If using Streamlit:

```bash
streamlit run app.py
```

---

# Usage

### Step 1

Open the application.

### Step 2

Upload one or more financial documents.

### Step 3

The agent automatically begins processing the uploaded documents.

### Step 4

The system extracts and validates financial information.

### Step 5

The agent generates:

```text
Current State Analysis
        +
Gap Detection
        +
Forward-Looking Flags
```

### Step 6

Review the generated financial intelligence report and source references.

---

# Why Agentic AI?

A conventional document-processing application might simply follow:

```text
Upload → Extract → Summarize
```

Our approach is designed around:

```text
Upload
   ↓
Understand
   ↓
Analyze
   ↓
Identify Missing Information
   ↓
Reason Over Financial Patterns
   ↓
Generate Financial Signals
   ↓
Verify Sources
   ↓
Report
```

The advantage is that the system does not require the SME owner to know which financial questions to ask first.

The challenge specifically asks for an agent that autonomously analyzes uploaded documents and produces the three required categories of output without being prompted by the user.

---

# Limitations

The system has several important limitations:

* Analysis quality depends on document quality.
* Missing financial information can limit the available analysis.
* OCR errors may affect scanned documents.
* Financial signals should be reviewed by qualified professionals before major business decisions.
* The system does not provide tax or investment advice.
* Forward-looking flags are observations based on available patterns, not guaranteed predictions.

---

# Future Enhancements

Future versions could include:

* Multi-document financial reconciliation
* Real-time bank transaction integration
* Advanced invoice aging analysis
* Automated financial dashboards
* Industry-specific benchmarks
* Multi-language document processing
* Better OCR for scanned statements
* Continuous financial monitoring
* Email-based document ingestion
* Automated alerts for important financial signals
* Cloud deployment and scalable document processing

---

# Hackathon Deliverable

The project is designed around the hackathon's required end-to-end flow:

```text
Document Upload
      ↓
Agent Analysis
      ↓
Structured Financial Intelligence
```

The challenge requires a working prototype demonstrating this complete flow along with a pitch covering the scoped problem, rationale for using an agent, reasoning loop, demonstration, limitation, and future development.

---

# Team

**Team Size:** 4–5 members

### Contributors

* [Member 1](https://github.com/)
* [Member 2](https://github.com/)
* [Member 3](https://github.com/)
* [Member 4](https://github.com/)
* [Member 5](https://github.com/)

---

# Project Status

**Status:** Hackathon Prototype

The current project focuses on demonstrating an end-to-end agentic financial document analysis workflow for SMEs.

---

# License

This project is developed for educational and hackathon purposes.

---

## Acknowledgements

This project was developed based on the **Financial Document Intelligence Agent for SMEs** hackathon challenge brief.

The challenge focuses on transforming financial documents into timely, traceable financial insights for SMEs through an autonomous agentic workflow.

Deployment link:[https://ai-document-analyser-eight.vercel.app/]

