import re
import spacy

class CitationAgent:
    def __init__(self, counsel_name):
        self.counsel_name = counsel_name
        self.documents = []
        self.nlp = spacy.load("en_core_web_sm")  # Load spaCy model

    def fetch_documents(self):
        dummy_docs = {
            "Ravi Kumar": [
                "The accused was charged under Section 420 of the IPC...",
                "In the landmark case of K.S. Puttaswamy v. Union of India..."
            ],
            "Sneha Desai": [
                "Relied upon Article 21 of the Constitution...",
                "As per Maneka Gandhi v. Union of India..."
            ]
        }
        self.documents = dummy_docs.get(self.counsel_name, [])
        return self.documents

    def extract_citations(self):
        statute_pattern = r"(Section\s\d+[A-Za-z]*\s+of\s+the\s+[A-Za-z\s]+|Article\s\d+[A-Za-z]*\s+of\s+the\s+[A-Za-z\s]+)"
        case_law_pattern = r"[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*\s+v(?:s\.?|\.?)\s+[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*"


        citations = []

        for doc in self.documents:
            # Regex citations
            statutes = re.findall(statute_pattern, doc)
            cases = re.findall(case_law_pattern, doc)

            # NER-based detection
            nlp_doc = self.nlp(doc)
            for ent in nlp_doc.ents:
                if ent.label_ in ["LAW", "ORG", "PERSON"] and "v." in ent.text:
                    cases.append(ent.text.strip())

            citations.extend(statutes + cases)

        return citations

    def generate_report(self):
        self.fetch_documents()
        citations = self.extract_citations()

        citation_freq = {}
        for c in citations:
            citation_freq[c] = citation_freq.get(c, 0) + 1

        # Convert to structured format
        structured = []
        for idx, (text, freq) in enumerate(
            sorted(citation_freq.items(), key=lambda x: -x[1]), start=1
        ):
            citation_type = "case_law" if "v." in text else "statute"
            structured.append({
                "type": citation_type,
                "text": text,
                "frequency": freq,
                "rank": idx
            })

        return structured

