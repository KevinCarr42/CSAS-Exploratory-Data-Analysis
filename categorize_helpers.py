"""Helper functions for content categorization and language detection."""
from langdetect import detect, LangDetectException
import re

def detect_language(text):
    """Detect language of text using langdetect."""
    if not text or len(text.strip()) < 3:
        return 'unknown'
    try:
        return detect(text)
    except LangDetectException:
        return 'unknown'

def normalize_text(text):
    """Normalize whitespace in text."""
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

# Keyword definitions for categorization
ACTION_KEYWORDS_REFINED = {
    'explicit': ['action item', 'action:', 'to do', 'todo:', 'deliverable', 'deliver by'],
    'responsibility': ['responsibility', 'responsible for', 'owner:', 'lead:', 'assigned to'],
    'deadline': ['by:', 'deadline:', 'due date', 'due by', 'timeline', 'date:'],
    'future_tense': ['will', 'shall', 'should', 'needs to', 'must', 'required to'],
    'completion': ['implement', 'complete', 'finish', 'develop', 'create', 'establish']
}

RECOMMENDATION_KEYWORDS_REFINED = {
    'recommendation': ['recommendation', 'recommend', 'we recommend'],
    'best_practice': ['best practice', 'best practices', 'approach', 'option'],
    'suggestion': ['suggest', 'propose', 'consider', 'should consider'],
    'process': ['process', 'workflow', 'procedure', 'protocol']
}

CONTENTION_KEYWORDS_REFINED = {
    'concern': ['concern', 'issue', 'problem', 'risk', 'challenge'],
    'conflict': ['disagreement', 'debate', 'conflict', 'tension'],
    'unclear': ['unclear', 'undefined', 'pending', 'pending decision', 'to be determined'],
    'discussion': ['discuss', 'discussion needed', 'needs discussion']
}

def check_keywords(text, keyword_dict):
    """Check which categories match in text."""
    text_lower = text.lower()
    matches = []
    for category, keywords in keyword_dict.items():
        if any(kw in text_lower for kw in keywords):
            matches.append(category)
    return matches

def categorize_content(text):
    """Categorize text by action, recommendation, and contention signals."""
    return {
        'action_categories': check_keywords(text, ACTION_KEYWORDS_REFINED),
        'recommendation_categories': check_keywords(text, RECOMMENDATION_KEYWORDS_REFINED),
        'contention_categories': check_keywords(text, CONTENTION_KEYWORDS_REFINED)
    }

# Theme definitions
THEMES = {
    'Publications': ['publication', 'publish', 'timing', 'overdue', 'document', 'csas'],
    'Transformation': ['transformation', 'modernization', 'tool', 'system', 'change'],
    'Web/Centralization': ['web', 'centralization', 'cdos', 'database', 'platform'],
    'Process/Best Practices': ['process', 'workflow', 'practice', 'procedure', 'standard'],
    'Survival/Exercise': ['exercise', 'survival', 'game', 'simulation'],
}

def detect_themes(text):
    """Detect which themes apply to text."""
    text_lower = text.lower()
    detected = []
    for theme, keywords in THEMES.items():
        if any(kw in text_lower for kw in keywords):
            detected.append(theme)
    return detected if detected else ['General']
