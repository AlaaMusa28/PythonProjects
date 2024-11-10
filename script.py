import re
from googleapiclient.discovery import build

# Assuming you have set up OAuth and have a valid Gmail API service object
service = build('gmail', 'v1', credentials=your_credentials)

# Sample keywords to detect
phishing_keywords = ["urgent", "verify", "click here", "password", "account"]

def detect_phishing(email_text):
    """Detect phishing based on keyword presence."""
    for keyword in phishing_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', email_text, re.IGNORECASE):
            return True
    return False

def scan_emails():
    # Fetch the list of messages (email IDs)
    messages = service.users().messages().list(userId='me').execute().get('messages', [])
    
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        email_text = msg['snippet']  # Get the email snippet (basic example)
        
        if detect_phishing(email_text):
            print(f"Phishing detected in email with ID: {message['id']}")
            # Here, you could add a label or flagging action

