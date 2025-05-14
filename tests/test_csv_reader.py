import pytest
from reader.csv_reader import parse_csv


def test_parse_csv_with_varied_headers():
    csv = """id,email,name,department,hours_worked,salary
1,a@x.com,Alice,Sales,160,30
"""
    result = parse_csv(csv)
    assert result[0]["hourly_rate"] == "30"
    assert result[0]["name"] == "Alice"
