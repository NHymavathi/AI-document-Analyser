from typing import Dict, Any, List
from agents.state import GraphState

def gap_detection_agent(state: GraphState) -> Dict[str, Any]:
    """Agent 6: Audits document presence across 5 core categories. Generates Section 6 Gap Matrix."""
    logs = state.get('execution_logs', [])
    classified = state.get('classified_datasets', {})
    node_statuses = state.get('agent_node_statuses', {})
    reasoning_chain = state.get('reasoning_chain', [])
    
    node_statuses['gap_detection'] = 'Running'
    logs.append("🤖 [Gap Detection Agent] Auditing 5 document categories for omissions...")

    # Document Coverage Matrix Checklist
    document_checklist = [
        {
            'category_id': 'balance_sheet',
            'title': 'Balance Sheet Statement',
            'uploaded': len(classified.get('financial_statements', [])) > 0,
            'file_name': classified.get('financial_statements', ['Not Uploaded'])[0] if classified.get('financial_statements') else None,
            'reason': 'Required for official debt-to-equity and long-term asset valuation.',
            'business_impact': 'Inability to calculate total long-term debt liabilities or solvency margins.',
            'blocked_decision': 'Cannot apply for commercial bank debt financing or enterprise valuation.',
            'priority': 'HIGH'
        },
        {
            'category_id': 'pnl_statement',
            'title': 'Profit & Loss (P&L) Statement',
            'uploaded': len(classified.get('financial_statements', [])) > 0,
            'file_name': classified.get('financial_statements', ['Not Uploaded'])[0] if classified.get('financial_statements') else None,
            'reason': 'Crucial to verify historical gross income vs net operating margins.',
            'business_impact': 'Uncertainty around historical tax liabilities and gross cost margins.',
            'blocked_decision': 'Cannot perform multi-year EBITDA growth benchmarking.',
            'priority': 'HIGH'
        },
        {
            'category_id': 'cash_flow',
            'title': 'Cash Flow Statement',
            'uploaded': len(classified.get('financial_transactions', [])) > 0,
            'file_name': classified.get('financial_transactions', ['transactions.csv'])[0] if classified.get('financial_transactions') else None,
            'reason': 'Required to track actual operating, investing, and financing cash movements.',
            'business_impact': 'Risk of unmonitored operational cash burn.',
            'blocked_decision': 'Cannot calculate exact monthly cash burn rate.',
            'priority': 'MEDIUM'
        },
        {
            'category_id': 'invoices_receivables',
            'title': 'Invoices & Customer Accounts Receivable',
            'uploaded': len(classified.get('invoices_receivables', [])) > 0,
            'file_name': classified.get('invoices_receivables', ['invoices.csv'])[0] if classified.get('invoices_receivables') else None,
            'reason': 'Necessary to measure Days Sales Outstanding (DSO) and customer credit defaults.',
            'business_impact': 'High risk of undetected bad debt write-offs.',
            'blocked_decision': 'Cannot set customer credit terms or payment penalties.',
            'priority': 'HIGH'
        },
        {
            'category_id': 'sme_context',
            'title': 'SME Business Context & Registration Profile',
            'uploaded': len(classified.get('sme_context', [])) > 0,
            'file_name': classified.get('sme_context', ['sme_context.json'])[0] if classified.get('sme_context') else None,
            'reason': 'Establishes industry-specific profit margin standards and company size tiers.',
            'business_impact': 'Lack of peer group comparison data.',
            'blocked_decision': 'Cannot evaluate competitive industry position.',
            'priority': 'LOW'
        }
    ]

    missing_docs = [doc for doc in document_checklist if not doc['uploaded']]

    gap_report = {
        'total_categories': 5,
        'uploaded_count': 5 - len(missing_docs),
        'missing_count': len(missing_docs),
        'document_checklist': document_checklist,
        'missing_documents_list': missing_docs,
        'strict_guarantee': 'Zero missing values were guessed or hallucinated by the AI Agent.'
    }

    reasoning_chain.append({
        'step_number': 2,
        'agent': 'Gap Detection Agent',
        'phase': 'Document Coverage Audit',
        'thought_process': f"Cross-referenced uploaded files against mandatory 5 document categories. Identified {len(missing_docs)} missing document types. Flagged blocked business decisions without hallucinating values.",
        'source_used': 'Classified Dataset Index'
    })

    logs.append(f"✅ [Gap Detection Agent] Audit complete. Identified {len(missing_docs)} missing categories.")
    node_statuses['gap_detection'] = 'Completed'

    return {
        'gap_detection_report': gap_report,
        'reasoning_chain': reasoning_chain,
        'agent_node_statuses': node_statuses,
        'execution_logs': logs
    }
