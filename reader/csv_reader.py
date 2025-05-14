from typing import List, Dict
from utils.field_mapper import map_fields


def parse_csv(content: str) -> List[Dict[str, str]]:
    lines = [line.strip() for line in content.strip().splitlines() if line.strip()]
    header = lines[0].split(",")
    header = [h.strip() for h in header]
    records = []

    for line in lines[1:]:
        values = [v.strip() for v in line.split(",")]
        row = dict(zip(header, values))
        row = map_fields(row)
        records.append(row)

    return records


def read_csv_files(filepaths: List[str]) -> List[Dict[str, str]]:
    all_records = []
    for path in filepaths:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            all_records.extend(parse_csv(content))
    return all_records
