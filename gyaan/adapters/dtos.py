from dataclasses import dataclass


@dataclass
class UserDTO:
    user_id: int
    name: str
    is_admin: bool
    is_domain_expert: bool
