---
name: phone-origin
description: Look up the origin location, country, state/city, original carrier, and time zone of a phone number. Use when the user asks where a phone number is from or wants to look up an area code or phone number.
---

# Phone Number Origin Lookup

When the user provides a phone number and asks where it is from:

1. Run the lookup script using the Bash tool, from the repository root:
   `python3 .claude/skills/phone-origin/scripts/lookup.py "<PHONE_NUMBER>"`
2. Present the origin location, original carrier, and time zone clearly.
3. Briefly note that the location reflects where the number was originally issued, not necessarily the caller's live physical location.
