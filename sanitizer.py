import re

def redact_sensitive_data(text):
    """
    Simple Proof of Concept for Loi 25 Compliance.
    Removes emails and phone numbers from text strings.
    """
    # Pattern for Emails
    text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[EMAIL_REDACTED]', text)
    
    # Pattern for Phone Numbers (North America)
    text = re.sub(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', '[PHONE_REDACTED]', text)
    
    return text

if __name__ == "__main__":
    sample = "Contact Me.Maurice at 555-0199 or maurice@cabinet.law."
    print("Original:", sample)
    print("Sanitized:", redact_sensitive_data(sample))
