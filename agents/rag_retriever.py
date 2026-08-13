from typing import Dict, Any
from agents.state import GraphState
from database.db_manager import compute_sql_aggregations
from rag.vector_store import vector_rag_store

def dataset_retrieval_rag_agent(state: GraphState) -> Dict[str, Any]:
    """Agent 3: Combines SQL aggregations and Vector RAG context into unified dataset summaries."""
    session_id = state['session_id']
    logs = state.get('execution_logs', [])
    node_statuses = state.get('agent_node_statuses', {})
    
    node_statuses['dataset_retrieval_rag'] = 'Running'
    logs.append("🤖 [Dataset Retrieval Agent] Querying SQL database & RAG Vector Index...")
    
    # SQL Aggregations
    sql_stats = compute_sql_aggregations(session_id)
    
    invoices_summary = {
        'total_receivables': sql_stats['total_receivables'],
        'overdue_receivables': sql_stats['overdue_receivables'],
        'overdue_count': sql_stats['overdue_count'],
        'avg_days_overdue': sql_stats['avg_days_overdue']
    }
    
    transactions_summary = {
        'total_inflows': sql_stats['total_inflows'],
        'total_outflows': sql_stats['total_outflows'],
        'net_cash_flow': sql_stats['net_cash_flow']
    }
    
    # RAG Semantic Search
    sme_rag_results = vector_rag_store.search("SME industry category company size registration credit score", k=2)
    sme_context_text = "\n".join([doc['content'] for doc in sme_rag_results])
    
    sme_context = {
        'industry_type': 'Manufacturing & Wholesale SME' if 'manufacturing' in sme_context_text.lower() else 'General SME',
        'company_name': 'Apex Industrial SME',
        'company_size': 'Medium SME (45 Employees)',
        'context_raw': sme_context_text if sme_context_text else 'Standard SME Operating Profile'
    }

    logs.append("✅ [Dataset Retrieval Agent] Unified RAG context retrieved.")
    node_statuses['dataset_retrieval_rag'] = 'Completed'
    
    return {
        'invoices_summary': invoices_summary,
        'transactions_summary': transactions_summary,
        'sme_context': sme_context,
        'agent_node_statuses': node_statuses,
        'execution_logs': logs
    }
