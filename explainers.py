def explain_value(name, info):
    return {
        "marker":  name,
        "value":   info["value"],
        "status":  info["status"],
        "range":   info["range"],
        "meaning": info["meaning"],
        "insight": info["insight"],
        "tip":     info["tip"]
    }
