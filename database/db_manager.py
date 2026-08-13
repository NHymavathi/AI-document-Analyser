import sqlite3
import json
import uuid
from typing import Dict, List, Any, Optional
from config import Config

def get_db_connection():
    conn = sqlite3.connect(Config.DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id TEXT PRIMARY KEY,
            session_id TEXT NOT NULL,
            file_name TEXT NOT NULL,
            file_type TEXT NOT NULL,
            dataset_category TEXT,
            ocr_applied INTEGER DEFAULT 0,
            file_path TEXT NOT NULL,
            upload_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id TEXT PRIMARY KEY,
            session_id TEXT NOT NULL,
            document_id TEXT,
            transaction_date TEXT,
            description TEXT,
            category TEXT,
            amount REAL NOT NULL,
            transaction_type TEXT,
            source_row INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS invoices (
            id TEXT PRIMARY KEY,
            session_id TEXT NOT NULL,
            document_id TEXT,
            invoice_number TEXT,
            customer_name TEXT,
            issue_date TEXT,
            due_date TEXT,
            amount REAL NOT NULL,
            status TEXT,
            days_overdue INTEGER DEFAULT 0,
            source_row INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS financial_summaries (
            id TEXT PRIMARY KEY,
            session_id TEXT NOT NULL UNIQUE,
            revenue REAL DEFAULT 0.0,
            total_expenses REAL DEFAULT 0.0,
            net_profit REAL DEFAULT 0.0,
            current_assets REAL DEFAULT 0.0,
            current_liabilities REAL DEFAULT 0.0,
            cash_balance REAL DEFAULT 0.0,
            profit_margin_pct REAL DEFAULT 0.0,
            current_ratio REAL DEFAULT 0.0,
            quick_ratio REAL DEFAULT 0.0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analysis_reports (
            id TEXT PRIMARY KEY,
            session_id TEXT NOT NULL UNIQUE,
            current_state_json TEXT NOT NULL,
            gap_detection_json TEXT NOT NULL,
            forward_looking_json TEXT NOT NULL,
            traceability_json TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def save_document_record(session_id: str, file_name: str, file_type: str, category: str, file_path: str, ocr_applied: bool = False) -> str:
    doc_id = str(uuid.uuid4())
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO documents (id, session_id, file_name, file_type, dataset_category, ocr_applied, file_path)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (doc_id, session_id, file_name, file_type, category, 1 if ocr_applied else 0, file_path))
    conn.commit()
    conn.close()
    return doc_id

def insert_transactions(session_id: str, document_id: str, tx_list: List[Dict[str, Any]]):
    conn = get_db_connection()
    cursor = conn.cursor()
    for tx in tx_list:
        cursor.execute('''
            INSERT INTO transactions (id, session_id, document_id, transaction_date, description, category, amount, transaction_type, source_row)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            str(uuid.uuid4()),
            session_id,
            document_id,
            tx.get('date', ''),
            tx.get('description', ''),
            tx.get('category', 'Uncategorized'),
            float(tx.get('amount', 0.0)),
            tx.get('type', 'DEBIT').upper(),
            tx.get('source_row', 0)
        ))
    conn.commit()
    conn.close()

def insert_invoices(session_id: str, document_id: str, inv_list: List[Dict[str, Any]]):
    conn = get_db_connection()
    cursor = conn.cursor()
    for inv in inv_list:
        cursor.execute('''
            INSERT INTO invoices (id, session_id, document_id, invoice_number, customer_name, issue_date, due_date, amount, status, days_overdue, source_row)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            str(uuid.uuid4()),
            session_id,
            document_id,
            inv.get('invoice_number', ''),
            inv.get('customer_name', ''),
            inv.get('issue_date', ''),
            inv.get('due_date', ''),
            float(inv.get('amount', 0.0)),
            inv.get('status', 'PENDING').upper(),
            int(inv.get('days_overdue', 0)),
            inv.get('source_row', 0)
        ))
    conn.commit()
    conn.close()

def compute_sql_aggregations(session_id: str) -> Dict[str, Any]:
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT 
            SUM(CASE WHEN transaction_type = 'CREDIT' THEN amount ELSE 0 END) as total_inflows,
            SUM(CASE WHEN transaction_type = 'DEBIT' THEN amount ELSE 0 END) as total_outflows,
            COUNT(*) as tx_count
        FROM transactions WHERE session_id = ?
    ''', (session_id,))
    tx_row = cursor.fetchone()
    
    cursor.execute('''
        SELECT 
            SUM(CASE WHEN status = 'OVERDUE' THEN amount ELSE 0 END) as overdue_receivables,
            SUM(CASE WHEN status = 'PENDING' OR status = 'OVERDUE' THEN amount ELSE 0 END) as total_receivables,
            SUM(CASE WHEN status = 'PAID' THEN amount ELSE 0 END) as collected_receivables,
            COUNT(CASE WHEN status = 'OVERDUE' THEN 1 END) as overdue_count,
            AVG(days_overdue) as avg_days_overdue
        FROM invoices WHERE session_id = ?
    ''', (session_id,))
    inv_row = cursor.fetchone()
    
    conn.close()
    
    inflows = tx_row['total_inflows'] if tx_row and tx_row['total_inflows'] else 0.0
    outflows = tx_row['total_outflows'] if tx_row and tx_row['total_outflows'] else 0.0
    
    total_rec = inv_row['total_receivables'] if inv_row and inv_row['total_receivables'] else 0.0
    overdue_rec = inv_row['overdue_receivables'] if inv_row and inv_row['overdue_receivables'] else 0.0
    avg_overdue = inv_row['avg_days_overdue'] if inv_row and inv_row['avg_days_overdue'] else 0.0
    
    return {
        'total_inflows': inflows,
        'total_outflows': outflows,
        'net_cash_flow': inflows - outflows,
        'total_receivables': total_rec,
        'overdue_receivables': overdue_rec,
        'overdue_count': inv_row['overdue_count'] if inv_row else 0,
        'avg_days_overdue': round(avg_overdue, 1)
    }

def save_analysis_report(session_id: str, current_state: Dict, gap_detection: Dict, forward_looking: Dict, master_payload: Dict):
    conn = get_db_connection()
    cursor = conn.cursor()
    report_id = str(uuid.uuid4())
    cursor.execute('''
        INSERT OR REPLACE INTO analysis_reports (id, session_id, current_state_json, gap_detection_json, forward_looking_json, traceability_json)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        report_id,
        session_id,
        json.dumps(current_state),
        json.dumps(gap_detection),
        json.dumps(forward_looking),
        json.dumps(master_payload)
    ))
    conn.commit()
    conn.close()

def get_analysis_report(session_id: str) -> Optional[Dict[str, Any]]:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM analysis_reports WHERE session_id = ?', (session_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    
    trace_data = json.loads(row['traceability_json']) if row['traceability_json'] else {}
    if 'current_state' in trace_data and 'ai_executive_summary' in trace_data:
        return trace_data

    return {
        'session_id': row['session_id'],
        'current_state': json.loads(row['current_state_json']),
        'gap_detection': json.loads(row['gap_detection_json']),
        'forward_looking': json.loads(row['forward_looking_json']),
        'traceability': trace_data,
        'created_at': row['created_at']
    }

init_db()
