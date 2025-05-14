from typing import Callable, Optional
from .payout import generate_payout

REPORTS = {
    "payout": generate_payout
}


def get_report(name: str) -> Optional[Callable]:
    return REPORTS.get(name)
