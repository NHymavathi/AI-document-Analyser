from agents.state import GraphState
from agents.classifier import document_classifier_agent
from agents.extractor import data_extraction_ocr_agent
from agents.rag_retriever import dataset_retrieval_rag_agent
from agents.analyzer import financial_analysis_agent
from agents.gap_detector import gap_detection_agent
from agents.flag_forecaster import forward_looking_flag_agent
from agents.reporter import report_generation_agent

try:
    from langgraph.graph import StateGraph, END
    HAS_LANGGRAPH = True
except ImportError:
    HAS_LANGGRAPH = False

class FallbackLangGraphWorkflow:
    """Resilient LangGraph State Machine Engine."""
    def invoke(self, initial_state: GraphState) -> GraphState:
        state = initial_state
        state.update(document_classifier_agent(state))
        state.update(data_extraction_ocr_agent(state))
        state.update(dataset_retrieval_rag_agent(state))
        state.update(financial_analysis_agent(state))
        state.update(gap_detection_agent(state))
        state.update(forward_looking_flag_agent(state))
        state.update(report_generation_agent(state))
        return state

def build_financial_agent_graph():
    """Constructs the LangGraph state machine workflow."""
    if HAS_LANGGRAPH:
        workflow = StateGraph(GraphState)
        workflow.add_node("classifier", document_classifier_agent)
        workflow.add_node("extractor", data_extraction_ocr_agent)
        workflow.add_node("retriever", dataset_retrieval_rag_agent)
        workflow.add_node("analyzer", financial_analysis_agent)
        workflow.add_node("gap_detector", gap_detection_agent)
        workflow.add_node("flag_forecaster", forward_looking_flag_agent)
        workflow.add_node("reporter", report_generation_agent)

        workflow.set_entry_point("classifier")
        workflow.add_edge("classifier", "extractor")
        workflow.add_edge("extractor", "retriever")
        workflow.add_edge("retriever", "analyzer")
        workflow.add_edge("analyzer", "gap_detector")
        workflow.add_edge("gap_detector", "flag_forecaster")
        workflow.add_edge("flag_forecaster", "reporter")
        workflow.add_edge("reporter", END)

        return workflow.compile()
    else:
        return FallbackLangGraphWorkflow()

# Singleton Graph Instance
financial_agent_app = build_financial_agent_graph()

