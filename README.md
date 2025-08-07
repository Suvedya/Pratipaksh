# 🧑‍⚖️ Pratipaksh – The Opposing Counsel Citation Analyzer

**Pratipaksh** is a legal analytics tool that helps lawyers, researchers, or legal firms analyze an opposing counsel's strategy by extracting and ranking **frequently cited statutes and landmark cases** from their past court filings.

> 📌 Built as part of the Legal Sakha Engineering Foundation Internship (Phase 2)

---

## 🔍 What It Does

- ✅ Takes **only the name of an opposing counsel** as input
- 🔎 Simulates fetching their **past legal filings**
- 📑 Extracts **citations** using:
  - Regular Expressions (for statutes like “Section 420 of the IPC”)
  - spaCy Named Entity Recognition (NER) for case law patterns
- 📊 Returns a **structured, ranked JSON report** showing:
  - Citation type (`statute` or `case_law`)
  - Frequency of mention
  - Rank based on usage

---

## 📥 Input

- `POST /api/generate-citation-report`
- JSON Body:
  ```json
  {
    "counsel_name": "Sneha Desai"
  }

### 📤 Output

```json
[
  {
    "type": "statute",
    "text": "Article 21 of the Constitution",
    "frequency": 1,
    "rank": 1
  },
  {
    "type": "case_law",
    "text": "Maneka Gandhi v. Union",
    "frequency": 1,
    "rank": 2
  }
]
```

### 🏗️ Project Structure

```text
Pratipaksh_project/
├── agents/
│   └── citation_agent.py       # Core logic for citation extraction
├── routes/
│   └── citation_routes.py      # API route for citation report
├── services/
│   └── docket_search.py        # (Mock) document fetch logic
├── tests/
│   └── test_citation_agent.py  # Unit tests for the agent
├── main.py                     # Flask entry point
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```
