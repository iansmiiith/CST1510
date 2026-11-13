raw = "[high], login error, can't log in "
parts = [p.strip()for p in raw.split(',')]
priority = parts[0].strip('[]').upper()
category = parts[1].title()
issue = parts[2].upper()
print(f"Priority:{priority} | Category: {category} | Issue:{issue}")
