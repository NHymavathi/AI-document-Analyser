import os
import uuid
from flask import Flask, render_template, request, jsonify
from config import Config
from agents.graph import financial_agent_app
from database.db_manager import get_analysis_report

app = Flask(__name__)
app.config.from_object(Config)

# Force UPLOAD_FOLDER to /tmp for Vercel/serverless write permissions
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', '/tmp')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Fallback for SAMPLE_FOLDER
SAMPLE_FOLDER = getattr(Config, 'SAMPLE_FOLDER', os.path.join(app.root_path, 'uploads'))
app.config['SAMPLE_FOLDER'] = SAMPLE_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/v1/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'online',
        'system': 'Financial Document Intelligence Agent for SMEs',
        'version': '1.0.0-hackathon',
        'gemini_configured': bool(getattr(Config, 'GEMINI_API_KEY', None))
    })


@app.route('/api/v1/analyze', methods=['POST'])
def analyze_documents():
    """Uploads document set and triggers autonomous LangGraph execution."""
    if 'files' not in request.files:
        return jsonify({'error': 'No files uploaded'}), 400

    uploaded_files_list = request.files.getlist('files')
    if not uploaded_files_list or uploaded_files_list[0].filename == '':
        return jsonify({'error': 'Empty file list'}), 400

    session_id = str(uuid.uuid4())
    session_dir = os.path.join(app.config['UPLOAD_FOLDER'], session_id)
    os.makedirs(session_dir, exist_ok=True)

    file_metadata = []
    for f in uploaded_files_list:
        file_path = os.path.join(session_dir, f.filename)
        f.save(file_path)
        file_metadata.append({
            'file_name': f.filename,
            'file_path': file_path,
            'format': os.path.splitext(f.filename)[1].lower()
        })

    initial_state = {
        'session_id': session_id,
        'uploaded_files': file_metadata,
        'extracted_text_blocks': [],
        'classified_datasets': {},
        'structured_financials': {},
        'invoices_summary': {},
        'transactions_summary': {},
        'sme_context': {},
        'current_state_analysis': {},
        'gap_detection_report': {},
        'forward_looking_flags': {},
        'traceability_map': {},
        'execution_logs': [f"🚀 [Gateway] Uploaded {len(file_metadata)} files for session {session_id[:8]}"],
        'error': None
    }

    # Trigger LangGraph Workflow Execution
    try:
        final_state = financial_agent_app.invoke(initial_state)
        report = get_analysis_report(session_id)

        return jsonify({
            'status': 'success',
            'session_id': session_id,
            'execution_logs': final_state.get('execution_logs', []),
            'results': report
        })
    except Exception as e:
        app.logger.error(f"Execution Error: {str(e)}")
        return jsonify({'error': f"Agent Workflow Failed: {str(e)}"}), 500


@app.route('/api/v1/demo/load_sample', methods=['POST'])
def load_sample_demo():
    """Instant 1-Click Hackathon Demo Preset."""
    try:
        session_id = f"demo-{str(uuid.uuid4())[:8]}"
        sample_dir = app.config.get('SAMPLE_FOLDER', os.path.join(app.root_path, 'uploads'))

        sample_files = [
            {'file_name': 'invoices.csv', 'file_path': os.path.join(sample_dir, 'invoices.csv'), 'format': '.csv'},
            {'file_name': 'transactions.csv', 'file_path': os.path.join(sample_dir, 'transactions.csv'), 'format': '.csv'},
            {'file_name': 'sme_context.json', 'file_path': os.path.join(sample_dir, 'sme_context.json'), 'format': '.json'}
        ]

        initial_state = {
            'session_id': session_id,
            'uploaded_files': sample_files,
            'extracted_text_blocks': [],
            'classified_datasets': {},
            'structured_financials': {},
            'invoices_summary': {},
            'transactions_summary': {},
            'sme_context': {},
            'current_state_analysis': {},
            'gap_detection_report': {},
            'forward_looking_flags': {},
            'traceability_map': {},
            'execution_logs': [f"🌟 [Demo Mode] Initializing pre-loaded SME Crisis Dataset (Session {session_id})"],
            'error': None
        }

        final_state = financial_agent_app.invoke(initial_state)
        report = get_analysis_report(session_id)

        return jsonify({
            'status': 'success',
            'session_id': session_id,
            'execution_logs': final_state.get('execution_logs', []),
            'results': report
        })
    except Exception as e:
        app.logger.error(f"Demo Load Error: {str(e)}")
        return jsonify({'error': f"Demo execution failed: {str(e)}"}), 500


@app.route('/api/v1/results/<session_id>', methods=['GET'])
def get_results(session_id):
    report = get_analysis_report(session_id)
    if not report:
        return jsonify({'error': 'Session not found'}), 404
    return jsonify({'session_id': session_id, 'results': report})


if __name__ == '__main__':
    print("=" * 70)
    print("FINANCIAL DOCUMENT INTELLIGENCE AGENT FOR SMEs")
    print("Serving on http://127.0.0.1:5000")
    print("=" * 70)
    app.run(host='0.0.0.0', port=5000, debug=True)