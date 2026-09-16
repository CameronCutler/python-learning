import re


def extract_names(records):
    """Return names from records containing a ``Name:`` field."""
    return [name.strip() for name in re.findall(r"Name:\s*([^|]+)", "\n".join(records))]


def extract_emails(records):
    """Return email addresses from records."""
    return re.findall(r"\b[\w.+-]+@[\w.-]+\.\w+\b", "\n".join(records))


def normalize_phones(records):
    """Return phone numbers normalized to XXX-XXX-XXXX."""
    phones = re.findall(
        r"(?:\(?(\d{3})\)?[.\s-]*)(\d{3})[.\s-]*(\d{4})",
        "\n".join(records),
    )
    return ["-".join(phone) for phone in phones]


def extract_dates(records):
    """Return common numeric dates, regardless of their separator or order."""
    return re.findall(
        r"\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{4}|\d{4}[/-]\d{1,2}[/-]\d{1,2})\b",
        "\n".join(records),
    )


records = [
    "Name: Alice Johnson | Email: alice.j@gmail.com | Phone: (555) 123-4567 | Joined: 01/15/2023",
    "Name: Bob Smith | Email: bob_smith@yahoo.com | Phone: 555.987.6543 | Joined: 03-22-2023",
    "Name: Charlie Brown | Email: charlie@outlook.com | Phone: 555 111 2222 | Joined: 2023/07/01",
    "Name: Diana Prince | Email: diana.prince@company.co.uk | Phone: (555)444-3333 | Joined: 11/30/2023",
]

print("Names:", extract_names(records))
print("Emails:", extract_emails(records))
print("Phones:", normalize_phones(records))
print("Dates:", extract_dates(records))