from reports.payout import generate_payout


def test_generate_payout_output(capsys):
    data = [
        {"name": "Alice", "department": "HR", "hours_worked": "160", "hourly_rate": "50"},
        {"name": "Bob", "department": "Design", "hours_worked": "150", "hourly_rate": "40"},
    ]
    generate_payout(data)
    captured = capsys.readouterr()

    assert "HR" in captured.out
    assert "Alice" in captured.out
    assert "$  8000" in captured.out

    assert "Design" in captured.out
    assert "Bob" in captured.out
    assert "$  6000" in captured.out
