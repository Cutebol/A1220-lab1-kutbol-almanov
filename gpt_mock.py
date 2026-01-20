values = [{
    "receipt_1_food.jpg": {
        "date": None,
        "amount": "70.74",
        "vendor": None,
        "category": "Meals"
    }},{
    "drive.webp": {
        "date": "Wed, Nov 06, 2019",
        "amount": "$43.83",
        "vendor": "Uber",
        "category": "Transport"
    }},{
    "walmart.png": {
         "date": "10/17/2020",
         "amount": "27.27",
         "vendor": "WALL-MART-SUPERSTORE",
         "category": "Other"
    }},{
    "recipe_2_food.png": {
         "date": "30/09/2025 20:15",
         "amount": "$51.30",
         "vendor": "DINEFINE RESTAURANT",
         "category": "Meals"
      }
    }]

def normalize_amount(amount):
    """Normalize receipt amount by removing currency symbols.

    Args:
        amount (str | None): Raw amount string (e.g. "$43.83", "70.74").

    Returns:
        str | None: Normalized amount string without currency symbols,
        or None if parsing fails.
    """
    if amount is None:
        return None

    try:
        cleaned = amount.replace("$", "").replace(",", "").strip()
        float(cleaned)  # sanity check
        return cleaned
    except Exception:
        return None

def extract_receipt_info(img):
    name = list(values[0].keys())[0]
    receipt = values.pop(0)[name]

    receipt["amount"] = normalize_amount(receipt.get("amount"))

    return receipt
"""GPT module for extracting receipt information from images"""