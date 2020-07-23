from dataclasses import dataclass
from typing import List


from gyaan.storages.dtos import DomainDTO
from gyaan_auth.storages.dtos import UserDTO


@dataclass
class CompleteDomainDetailsDTO:
    domain_dto: DomainDTO
    domain_posts_count: int
    domain_members_count: int
    book_marks_count: int
    domain_expert_dtos: List[UserDTO]
