from typing import TypedDict, List, Dict, Any, Optional

class GraphState(TypedDict):
    session_id: str
    uploaded_files: List[Dict[str, Any]]        # file_name, file_path, format
    extracted_text_blocks: List[Dict[str, Any]] # text, page/row, doc_id
    classified_datasets: Dict[str, List[str]]   # Category -> List of File Names
    structured_financials: Dict[str, Any]       # Revenue, Expenses, Assets, Liabilities
    invoices_summary: Dict[str, Any]            # Overdue, Total, Days Overdue
    transactions_summary: Dict[str, Any]        # Inflows, Outflows, Net Cash Flow
    sme_context: Dict[str, Any]                 # Industry Type, SME Size, Category
    current_state_analysis: Dict[str, Any]      # Health, Ratios, Liquidity, Interpretation
    gap_detection_report: Dict[str, Any]        # Missing Docs, Blocked Decisions, Gaps
    forward_looking_flags: Dict[str, Any]       # Receivable risk, Runway, Expense Growth
    traceability_map: Dict[str, Any]            # Metric -> Source Citation
    
    # Enterprise SaaS Extensions
    ai_executive_summary: Dict[str, Any]        # Health Score (0-100), Risk Level, Top 3 Observations
    financial_kpi_cards: Dict[str, Any]         # 7 KPIs: Revenue, Expenses, Net Profit, Margin, Cash Flow, Liquidity, Working Capital
    reasoning_chain: List[Dict[str, Any]]       # Transparent step-by-step reasoning steps
    agent_node_statuses: Dict[str, str]         # Node ID -> Status (Completed, Running, Waiting)
    document_evidence: List[Dict[str, Any]]     # Extracted Evidence Table with confidence scores
    ai_recommendations: Dict[str, Any]         # Immediate Actions grouped by Priority (High, Medium, Low)
    system_analytics: Dict[str, Any]            # Processing Time, OCR Accuracy, Pages Processed
    
    execution_logs: List[str]                   # Step logs
    error: Optional[str]
