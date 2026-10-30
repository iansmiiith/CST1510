def check_status(percent, warning_at=100):
    if percent >= 100:
            return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"
percent = 90.0

