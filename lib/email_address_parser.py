# your code goes here!]
import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Split on commas or whitespace
        parts = re.split(r"[,\s]+", self.addresses.strip())

        # Keep only valid email addresses
        email_pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
        emails = [p for p in parts if email_pattern.fullmatch(p)]

        # Deduplicate and sort
        return sorted(set(emails))
