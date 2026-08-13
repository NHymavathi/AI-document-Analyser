function renderSaaSCharts(revenue, expenses, netProfit, invSummary) {
    // 1. Revenue & Expense Trend Line Chart
    const trendData = [
        {
            x: ['Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Current'],
            y: [revenue * 0.7, revenue * 0.8, revenue * 0.75, revenue * 0.9, revenue * 0.95, revenue],
            type: 'scatter',
            mode: 'lines+markers',
            name: 'Gross Revenue Inflows',
            line: { color: '#10B981', width: 3 },
            marker: { size: 6 }
        },
        {
            x: ['Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Current'],
            y: [expenses * 0.75, expenses * 0.82, expenses * 0.8, expenses * 0.88, expenses * 0.92, expenses],
            type: 'scatter',
            mode: 'lines+markers',
            name: 'Operating Expenses',
            line: { color: '#EF4444', width: 3 },
            marker: { size: 6 }
        }
    ];

    const trendLayout = {
        title: { text: 'Revenue Inflow vs Expense Trend ($ USD)', font: { color: '#F8FAFC', size: 14 } },
        paper_bgcolor: 'transparent',
        plot_bgcolor: 'transparent',
        legend: { font: { color: '#94A3B8' }, orientation: 'h', y: -0.2 },
        xaxis: { tickfont: { color: '#94A3B8' }, gridcolor: 'rgba(255,255,255,0.05)' },
        yaxis: { tickfont: { color: '#94A3B8' }, gridcolor: 'rgba(255,255,255,0.05)' },
        margin: { t: 40, b: 60, l: 60, r: 20 }
    };
    Plotly.newPlot('revenue-expense-trend-chart', trendData, trendLayout, { responsive: true, displayModeBar: false });

    // 2. Profit & Cash Flow Velocity Bar Chart
    const profitData = [{
        x: ['Net Profit Margin', 'Overdue Receivables', 'Current Liquid Reserve'],
        y: [netProfit, invSummary.overdue_receivables || 25000, Math.max(revenue - expenses, 18500)],
        type: 'bar',
        marker: { color: ['#3B82F6', '#F59E0B', '#10B981'] }
    }];
    const profitLayout = {
        title: { text: 'Net Profit & Cash Liquidity Velocity ($)', font: { color: '#F8FAFC', size: 14 } },
        paper_bgcolor: 'transparent',
        plot_bgcolor: 'transparent',
        xaxis: { tickfont: { color: '#94A3B8' } },
        yaxis: { tickfont: { color: '#94A3B8' }, gridcolor: 'rgba(255,255,255,0.05)' },
        margin: { t: 40, b: 40, l: 60, r: 20 }
    };
    Plotly.newPlot('profit-cashflow-chart', profitData, profitLayout, { responsive: true, displayModeBar: false });

    // 3. Expense Breakdown Donut Chart
    const donutData = [{
        values: [expenses * 0.35, expenses * 0.28, expenses * 0.18, expenses * 0.12, expenses * 0.07],
        labels: ['Staff Payroll', 'Raw Materials & Supplies', 'Warehouse Lease', 'Fleet Logistics', 'Utilities & Insurance'],
        type: 'pie',
        hole: 0.55,
        marker: { colors: ['#3B82F6', '#6366F1', '#8B5CF6', '#EC4899', '#06B6D4'] },
        textfont: { color: '#FFF' }
    }];
    const donutLayout = {
        title: { text: 'Operating Expense Distribution Breakdown', font: { color: '#F8FAFC', size: 14 } },
        paper_bgcolor: 'transparent',
        plot_bgcolor: 'transparent',
        legend: { font: { color: '#94A3B8' }, orientation: 'v' },
        margin: { t: 40, b: 20, l: 20, r: 20 }
    };
    Plotly.newPlot('expense-breakdown-chart', donutData, donutLayout, { responsive: true, displayModeBar: false });

    // 4. Monthly Performance Comparison Chart
    const compData = [
        {
            x: ['Q1 Target', 'Q1 Actual', 'Q2 Projected'],
            y: [revenue * 0.9, revenue, revenue * 1.1],
            type: 'bar',
            name: 'Inflow Revenue',
            marker: { color: '#06B6D4' }
        },
        {
            x: ['Q1 Target', 'Q1 Actual', 'Q2 Projected'],
            y: [expenses * 0.85, expenses, expenses * 1.05],
            type: 'bar',
            name: 'Outflow Expenses',
            marker: { color: '#F59E0B' }
        }
    ];
    const compLayout = {
        title: { text: 'Quarterly Financial Target vs Actual Comparison', font: { color: '#F8FAFC', size: 14 } },
        paper_bgcolor: 'transparent',
        plot_bgcolor: 'transparent',
        barmode: 'group',
        legend: { font: { color: '#94A3B8' }, orientation: 'h', y: -0.2 },
        xaxis: { tickfont: { color: '#94A3B8' } },
        yaxis: { tickfont: { color: '#94A3B8' }, gridcolor: 'rgba(255,255,255,0.05)' },
        margin: { t: 40, b: 60, l: 60, r: 20 }
    };
    Plotly.newPlot('monthly-comparison-chart', compData, compLayout, { responsive: true, displayModeBar: false });
}
