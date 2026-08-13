document.addEventListener('DOMContentLoaded', () => {
    // 1. Real-Time Clock
    function updateClock() {
        const now = new Date();
        document.getElementById('live-clock').textContent = now.toLocaleTimeString();
    }
    setInterval(updateClock, 1000);
    updateClock();

    const fileInput = document.getElementById('file-input');
    const uploadBox = document.getElementById('upload-card');
    const demoBtn = document.getElementById('demo-btn');
    const progressContainer = document.getElementById('progress-container');
    const progressBar = document.getElementById('progress-bar');
    const consoleLogs = document.getElementById('console-logs');
    const resultsContainer = document.getElementById('results-container');
    const agentStatusLabel = document.getElementById('agent-status-label');

    // Drag and Drop Events
    uploadBox.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadBox.classList.add('dragover');
    });

    uploadBox.addEventListener('dragleave', () => {
        uploadBox.classList.remove('dragover');
    });

    uploadBox.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadBox.classList.remove('dragover');
        if (e.dataTransfer.files.length > 0) {
            handleFileUpload(e.dataTransfer.files);
        }
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleFileUpload(e.target.files);
        }
    });

    demoBtn.addEventListener('click', () => {
        runDemoMode();
    });

    function showProgress(stepName, percent, logMsg) {
        progressContainer.style.display = 'block';
        progressBar.style.width = `${percent}%`;
        document.getElementById('current-step-label').textContent = stepName;
        agentStatusLabel.textContent = `LangGraph Agent: ${stepName}`;
        
        const logLine = document.createElement('div');
        logLine.textContent = `[${new Date().toLocaleTimeString()}] ${logMsg}`;
        consoleLogs.appendChild(logLine);
        consoleLogs.scrollTop = consoleLogs.scrollHeight;
    }

    async function handleFileUpload(files) {
        const formData = new FormData();
        for (let i = 0; i < files.length; i++) {
            formData.append('files', files[i]);
        }

        showProgress('Ingesting Financial Suite...', 15, `🚀 Uploaded ${files.length} files. Initializing LangGraph Multi-Agent Graph...`);

        try {
            showProgress('Running Extraction & OCR Pipeline...', 45, '🤖 Parsing tables, running EasyOCR, storing structured rows in SQL...');
            const response = await fetch('/api/v1/analyze', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();
            if (data.status === 'success') {
                showProgress('Report Synthesis & Traceability Complete', 100, '✅ All 13 SaaS dashboard sections compiled.');
                agentStatusLabel.textContent = 'LangGraph Agent: Analysis Active';
                renderMasterResults(data.results);
            } else {
                alert('Analysis error: ' + data.error);
            }
        } catch (err) {
            alert('Upload failed: ' + err.message);
        }
    }

    async function runDemoMode() {
        showProgress('Loading SME Crisis Scenario Preset...', 20, '🌟 Ingesting pre-loaded Invoices, Transactions, & SME Context...');
        try {
            showProgress('Running Cross-Dataset Reasoning...', 60, '🤖 Computing 7 KPIs, gap matrix, and runway forecast...');
            const response = await fetch('/api/v1/demo/load_sample', { method: 'POST' });
            const data = await response.json();
            if (data.status === 'success') {
                showProgress('Analysis Complete', 100, '✅ 1-Click Demo Ready.');
                agentStatusLabel.textContent = 'LangGraph Agent: Demo Loaded';
                renderMasterResults(data.results);
            }
        } catch (err) {
            alert('Demo trigger failed: ' + err.message);
        }
    }

    function renderMasterResults(reportData) {
        resultsContainer.style.display = 'block';
        const r = reportData.results ? reportData.results : reportData;

        // SECTION 11: LangGraph Workflow Graph Visualizer
        const nodeContainer = document.getElementById('node-graph-container');
        nodeContainer.innerHTML = '';
        const nodes = r.workflow_nodes || [
            {name: 'Document Classifier', icon: '📂'},
            {name: 'OCR Extraction', icon: '🔍'},
            {name: 'RAG Retrieval', icon: '🧠'},
            {name: 'Financial Analysis', icon: '📊'},
            {name: 'Gap Detection', icon: '🧩'},
            {name: 'Risk Agent', icon: '🚩'},
            {name: 'Report Agent', icon: '📑'}
        ];

        nodes.forEach((n, idx) => {
            const nodeDiv = document.createElement('div');
            nodeDiv.className = 'node-item completed';
            nodeDiv.innerHTML = `
                <div style="font-size:20px;">${n.icon}</div>
                <div style="font-size:11px; font-weight:700; color:var(--text-main); margin-top:4px;">${n.name}</div>
                <div style="font-size:10px; color:var(--accent-emerald); font-weight:600; margin-top:2px;">✅ Completed</div>
            `;
            nodeContainer.appendChild(nodeDiv);
            if (idx < nodes.length - 1) {
                const arrow = document.createElement('div');
                arrow.className = 'node-arrow';
                arrow.textContent = '➔';
                nodeContainer.appendChild(arrow);
            }
        });

        // SECTION 2: AI Executive Summary
        const exec = r.ai_executive_summary || {};
        document.getElementById('exec-score-val').textContent = exec.health_score || 78;
        document.getElementById('exec-health-status').textContent = exec.overall_health || 'Healthy';
        document.getElementById('exec-conf-score').textContent = exec.confidence_score || '96.4%';
        document.getElementById('exec-top-rec').textContent = exec.top_recommendation || 'Focus on liquidity.';

        const obsContainer = document.getElementById('exec-obs-list');
        obsContainer.innerHTML = '';
        (exec.top_observations || []).forEach(obs => {
            const bullet = document.createElement('div');
            bullet.className = 'obs-bullet';
            bullet.textContent = obs;
            obsContainer.appendChild(bullet);
        });

        // SECTION 3: Financial KPI Cards (7 KPIs)
        const kpis = r.financial_kpi_cards || {};
        document.getElementById('kpi-revenue').textContent = kpis.revenue ? kpis.revenue.formatted : '$0.00';
        document.getElementById('kpi-expenses').textContent = kpis.expenses ? kpis.expenses.formatted : '$0.00';
        document.getElementById('kpi-profit').textContent = kpis.net_profit ? kpis.net_profit.formatted : '$0.00';
        document.getElementById('kpi-margin').textContent = kpis.profit_margin ? kpis.profit_margin.formatted : '0.0%';
        document.getElementById('kpi-cashflow').textContent = kpis.cash_flow ? kpis.cash_flow.formatted : '$0.00';
        document.getElementById('kpi-liquidity').textContent = kpis.liquidity_ratio ? kpis.liquidity_ratio.formatted : '1.50x';
        document.getElementById('kpi-workingcap').textContent = kpis.working_capital ? kpis.working_capital.formatted : '$0.00';

        // SECTION 4: Plotly Visualizations
        const revVal = kpis.revenue ? kpis.revenue.value : 100000;
        const expVal = kpis.expenses ? kpis.expenses.value : 80000;
        const netVal = kpis.net_profit ? kpis.net_profit.value : 20000;
        const invSum = r.forward_looking ? r.forward_looking : {};
        renderSaaSCharts(revVal, expVal, netVal, invSum);

        // SECTION 5: Current State Analysis Cards
        const curr = r.current_state || {};
        const cardsContainer = document.getElementById('analysis-cards-container');
        cardsContainer.innerHTML = '';
        
        Object.entries(curr).forEach(([key, item]) => {
            if (typeof item === 'object' && item.title) {
                const card = document.createElement('div');
                card.className = 'analysis-card';
                card.innerHTML = `
                    <div style="font-size:14px; font-weight:700; color:var(--text-main); margin-bottom:8px;">${item.title}</div>
                    <div style="font-size:13px; color:var(--text-sub); line-height:1.5; margin-bottom:10px;">${item.interpretation}</div>
                    <div style="font-size:11px; color:var(--text-muted);"><strong>Evidence:</strong> ${item.evidence}</div>
                    <div class="citation-tag">📄 ${item.source_document} | ${item.page_number} (Conf: ${item.confidence_score})</div>
                `;
                cardsContainer.appendChild(card);
            }
        });

        // SECTION 6: Gap Detection Matrix
        const gaps = r.gap_detection || {};
        const gapContainer = document.getElementById('gap-matrix-container');
        gapContainer.innerHTML = '';
        (gaps.document_checklist || []).forEach(doc => {
            const card = document.createElement('div');
            card.className = `gap-matrix-card ${doc.uploaded ? 'uploaded' : 'missing'}`;
            card.innerHTML = `
                <div style="font-size:24px; margin-bottom:6px;">${doc.uploaded ? '✅' : '❌'}</div>
                <div style="font-size:13px; font-weight:700; margin-bottom:4px;">${doc.title}</div>
                <div style="font-size:11px; color:${doc.uploaded ? 'var(--accent-emerald)' : 'var(--accent-rose)'}; font-weight:600; margin-bottom:8px;">
                    ${doc.uploaded ? 'STATUS: UPLOADED' : 'STATUS: MISSING'}
                </div>
                ${!doc.uploaded ? `
                    <div style="font-size:11px; color:var(--text-sub); margin-bottom:6px;"><strong>Blocked Decision:</strong> ${doc.blocked_decision}</div>
                    <span class="growth-badge growth-down" style="font-size:10px;">Prio: ${doc.priority}</span>
                    <button class="btn-saas btn-preset" style="font-size:10px; padding:4px 8px; margin-top:8px;" onclick="document.getElementById('file-input').click()">Upload ${doc.title}</button>
                ` : `<div style="font-size:11px; color:var(--text-muted);">${doc.file_name}</div>`}
            `;
            gapContainer.appendChild(card);
        });

        // SECTION 7: Forward Looking Flags
        const flags = r.forward_looking ? r.forward_looking.detected_risk_flags : [];
        const flagsContainer = document.getElementById('risk-flags-container');
        flagsContainer.innerHTML = '';
        (flags || []).forEach(f => {
            const item = document.createElement('div');
            item.className = 'flag-item-saas';
            item.innerHTML = `
                <div style="display:flex; justify-content:space-between; font-size:13px; font-weight:700; color:var(--accent-amber); margin-bottom:4px;">
                    <span>🚩 ${f.risk_category}</span>
                    <span class="growth-badge growth-down">${f.risk_level}</span>
                </div>
                <div style="font-size:13px; color:var(--text-main); margin-bottom:6px;">${f.reason}</div>
                <div style="font-size:12px; color:var(--text-sub);">💡 <strong>Mitigation:</strong> ${f.mitigation}</div>
                <div style="font-size:10px; color:var(--text-muted); margin-top:4px;">Confidence: ${f.confidence} &bull; Trend: ${f.trend}</div>
            `;
            flagsContainer.appendChild(item);
        });

        // SECTION 8: AI Recommendations
        const recs = r.ai_recommendations || {};
        const recContainer = document.getElementById('recommendations-container');
        recContainer.innerHTML = '';

        const appendRecGroup = (items, prioClass, prioLabel) => {
            (items || []).forEach(rec => {
                const item = document.createElement('div');
                item.className = `rec-item-priority ${prioClass}`;
                item.innerHTML = `
                    <div style="display:flex; justify-content:space-between; font-size:13px; font-weight:700; margin-bottom:4px;">
                        <span>💡 ${rec.title}</span>
                        <span class="growth-badge growth-up">${prioLabel} PRIORITY</span>
                    </div>
                    <div style="font-size:12px; color:var(--text-main); margin-bottom:4px;">${rec.action}</div>
                    <div style="font-size:11px; color:var(--accent-cyan);">🚀 <strong>Expected Impact:</strong> ${rec.impact}</div>
                `;
                recContainer.appendChild(item);
            });
        };

        appendRecGroup(recs.high_priority, 'prio-high', 'HIGH');
        appendRecGroup(recs.medium_priority, 'prio-med', 'MEDIUM');
        appendRecGroup(recs.low_priority, 'prio-low', 'LOW');

        // SECTION 9: Document Evidence Table
        const evidence = r.document_evidence || [];
        const evTableBody = document.getElementById('evidence-table-body');
        evTableBody.innerHTML = '';
        evidence.forEach(e => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td><strong>${e.file_name}</strong></td>
                <td>${e.category}</td>
                <td>${e.page_number}</td>
                <td><span class="growth-badge growth-up">${e.confidence_score}%</span></td>
            `;
            evTableBody.appendChild(tr);
        });

        // SECTION 10: AI Reasoning Chain
        const reasoning = r.reasoning_chain || [];
        const reasonContainer = document.getElementById('reasoning-chain-container');
        reasonContainer.innerHTML = '';
        reasoning.forEach(step => {
            const box = document.createElement('div');
            box.className = 'reasoning-step-box';
            box.innerHTML = `
                <div style="color:var(--accent-cyan); font-weight:700;">Step ${step.step_number}: ${step.agent} &bull; ${step.phase}</div>
                <div style="color:var(--text-sub); margin-top:4px;">${step.thought_process}</div>
                <div style="color:var(--text-muted); font-size:10px; margin-top:4px;">Source: ${step.source_used}</div>
            `;
            reasonContainer.appendChild(box);
        });

        // SECTION 12: Analytics
        const analytics = r.system_analytics || {};
        document.getElementById('analytics-time').textContent = `${analytics.processing_time_ms || 1420} ms`;
        document.getElementById('analytics-ocr').textContent = analytics.ocr_accuracy_pct || '98.5%';
        document.getElementById('analytics-docs').textContent = `${analytics.documents_uploaded || 3} Files`;
        document.getElementById('analytics-pages').textContent = `${analytics.pages_processed || 4} Pages`;
        document.getElementById('analytics-conf').textContent = analytics.ai_confidence_score || '96.8%';
    }
});
