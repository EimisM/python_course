# Import re module
import re

# Define function to extract email strings from text
def extract_email(string: str) -> str:
    return re.findall(r"\S+@\S+", string)

# Define text that will be read while filtering emails
text = "Contact us at john.doe@example.com for support, jane.doe@company.org for sales, or admin@service.net for general inquiries."

# Perform filtering
emails = extract_email(text)

# Print result
print(emails)