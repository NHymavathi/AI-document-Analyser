import os
import json
from typing import Dict, Any, List
from agents.state import GraphState

def document_classifier_agent(state: GraphState) -> Dict[str, Any]:
    """Agent 1: Classifies uploaded documents into the 4 mandatory datasets."""
    files = state.get('uploaded_files', [])
    logs = state.get('execution_logs', [])
    node_statuses = state.get('agent_node_statuses', {})
    
    node_statuses['document_classifier'] = 'Running'
    classified = {
        'financial_statements': [],
        'invoices_receivables': [],
        'financial_transactions': [],
        'sme_context': []
    }
    
    logs.append("🤖 [Document Classifier Agent] Analyzing file metadata and structures...")
    
    for f in files:
        fname = f.get('file_name', '').lower()
        
        if any(term in fname for term in ['balance', 'statement', 'pnl', 'profit', 'loss', 'bs_', 'financial_statement']):
            classified['financial_statements'].append(f['file_name'])
        elif any(term in fname for term in ['invoice', 'receivable', 'bill', 'due', 'aging', 'invoices']):
            classified['invoices_receivables'].append(f['file_name'])
        elif any(term in fname for term in ['transaction', 'ledger', 'bank', 'spend', 'payment', 'cash_flow', 'transactions']):
            classified['financial_transactions'].append(f['file_name'])
        elif any(term in fname for term in ['context', 'profile', 'sme', 'company', 'industry', 'registration']):
            classified['sme_context'].append(f['file_name'])
        else:
            if f.get('format') in ['.xlsx', '.xls', '.csv']:
                if 'tx' in fname or 'tran' in fname:
                    classified['financial_transactions'].append(f['file_name'])
                else:
                    classified['invoices_receivables'].append(f['file_name'])
            else:
                classified['sme_context'].append(f['file_name'])

    logs.append(f"✅ [Document Classifier Agent] Classification Complete: {json.dumps(classified)}")
    node_statuses['document_classifier'] = 'Completed'
    
    return {
        'classified_datasets': classified,
        'agent_node_statuses': node_statuses,
        'execution_logs': logs
    }
