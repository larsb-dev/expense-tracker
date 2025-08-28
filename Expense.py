from dataclasses import dataclass

@dataclass
class Expense:
    id: int
    date: str
    category: str
    description: str
    amount: float