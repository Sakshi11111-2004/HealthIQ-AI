import re

def parse_medical_values(text):
    patterns = {
        "Hemoglobin": r"Hemoglobin\s+([\d.]+)",
        "RBC Count": r"RBC Count\s+([\d.]+)",
        "Platelet Count": r"Platelet Count\s+([\d.]+)",
        "LDL": r"LDL(?: Cholesterol)?\s+([\d.]+)",
        "HDL": r"HDL(?: Cholesterol)?\s+([\d.]+)",
        "Vitamin B12": r"Vitamin B12\s+([\d.]+)",
        "HbA1c": r"HbA1c\s+([\d.]+)"
    }

    results = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                results[key] = float(match.group(1))
            except:
                continue
    return results
