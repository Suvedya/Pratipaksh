# routes/citation_routes.py

from flask import Blueprint, request, jsonify
from agents.citation_agent import CitationAgent

citation_routes = Blueprint('citation_routes', __name__)

@citation_routes.route('/api/generate-citation-report', methods=['POST'])
def generate_report():
    data = request.get_json()
    counsel_name = data.get("counsel_name", "").strip()

    if not counsel_name:
        return jsonify({"error": "Counsel name is required"}), 400

    agent = CitationAgent(counsel_name)
    report = agent.generate_report()
    return jsonify(report)
