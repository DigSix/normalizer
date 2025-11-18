from common.config import STATES

def clean_state_preserving(text: str) -> str:
    """Replaces all occurrences of 'UF-' with three spaces."""
    for state in STATES:
        text = text.replace(f"{state}-", "   ")
    return text
