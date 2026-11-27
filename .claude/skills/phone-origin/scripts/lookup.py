import sys
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def lookup_number(raw_number):
    try:
        # Defaults to "US" if no country code like +44 is provided
        parsed = phonenumbers.parse(raw_number, "US")
        if not phonenumbers.is_valid_number(parsed):
            print(f"Invalid number: {raw_number}")
            return

        location = geocoder.description_for_number(parsed, "en") or "Unknown"
        net_carrier = carrier.name_for_number(parsed, "en") or "Unknown"
        zones = ", ".join(timezone.time_zones_for_number(parsed)) or "Unknown"
        formatted = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

        print(f"Number:    {formatted}")
        print(f"Origin:    {location}")
        print(f"Carrier:   {net_carrier}")
        print(f"Time Zone: {zones}")
    except Exception as e:
        print(f"Error parsing number: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lookup.py <phone_number>")
    else:
        lookup_number(" ".join(sys.argv[1:]))
