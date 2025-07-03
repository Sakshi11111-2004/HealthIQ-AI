from medical import MEDICAL_MARKERS

def analyze_values(vals):
    out = {}
    for k, v in vals.items():
        if k not in MEDICAL_MARKERS: continue
        lo, hi, meaning, tip = MEDICAL_MARKERS[k]
        status = "Normal" if lo <= v <= hi else ("High" if v>hi else "Low")
        insight = f"{k} level is {status}"
        out[k] = {
            "value": v,
            "range": (lo, hi),
            "status": status,
            "meaning": meaning,
            "insight": insight,
            "tip": tip
        }
    return out
