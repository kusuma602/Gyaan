from dataclasses import dataclass


@dataclass
class Domain_DTO:
    domain_id: int
    domain_name: str
    description: str
