from dataclasses import dataclass


@dataclass
class DomainDTO:
    domain_id: int
    domain_name: str
    description: str
