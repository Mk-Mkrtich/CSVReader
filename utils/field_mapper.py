from typing import Dict

ALTERNATIVE_NAMES = {
    "hourly_rate": {"rate", "salary", "hourly_rate"}
}


def map_fields(row: Dict[str, str]) -> Dict[str, str]:
    mapped = {}
    for key, value in row.items():
        standard_key = None
        for canonical, aliases in ALTERNATIVE_NAMES.items():
            if key.lower() in aliases:
                standard_key = canonical
                break
        mapped[standard_key or key] = value
    return mapped
