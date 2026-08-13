import pandas as pd
import os
from typing import Dict, List, Any

def extract_excel_csv_content(file_path: str) -> Dict[str, Any]:
    """Parses CSV or Excel (.xlsx/.xls) into structured dictionaries and sanitized DataFrames."""
    file_ext = os.path.splitext(file_path)[1].lower()
    sheets_data = {}
    
    if file_ext == '.csv':
        df = pd.read_csv(file_path)
        # Normalize column names: lowercase, stripped
        df.columns = [str(c).strip().lower().replace(' ', '_') for c in df.columns]
        sheets_data['Sheet1'] = {
            'columns': list(df.columns),
            'row_count': len(df),
            'records': df.to_dict(orient='records')
        }
    else:
        xls = pd.ExcelFile(file_path)
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            df.columns = [str(c).strip().lower().replace(' ', '_') for c in df.columns]
            sheets_data[sheet_name] = {
                'columns': list(df.columns),
                'row_count': len(df),
                'records': df.to_dict(orient='records')
            }
            
    return {
        'file_name': os.path.basename(file_path),
        'file_path': file_path,
        'format': file_ext,
        'sheets': sheets_data
    }
