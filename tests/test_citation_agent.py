# tests/test_citation_agent.py

import pytest
from agents.citation_agent import CitationAgent

def test_fetch_documents():
    agent = CitationAgent("Sneha Desai")
    docs = agent.fetch_documents()
    assert isinstance(docs, list)
    assert len(docs) > 0

def test_extract_citations():
    agent = CitationAgent("Sneha Desai")
    agent.fetch_documents()
    citations = agent.extract_citations()
    assert isinstance(citations, list)
    assert any("Article" in c or "v." in c for c in citations)

def test_generate_report():
    agent = CitationAgent("Sneha Desai")
    report = agent.generate_report()
    assert isinstance(report, list)
    assert all(isinstance(item, dict) for item in report)
