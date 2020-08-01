import pytest

from gyaan.adapters.dtos import UserDTO
from gyaan.interactors.dtos import CompleteDomainDetailsDTO
from gyaan.storages.dtos import DomainDTO


@pytest.fixture()
def domain_details_dto():
    domain_dto = CompleteDomainDetailsDTO(
        domain_dto=DomainDTO(
            domain_id=1,
            domain_name='domain_1',
            description='domain_1 description'
        ),
        domain_posts_count=2,
        domain_members_count=3,
        book_marks_count=4,
        domain_expert_dtos=[
            UserDTO(
                user_id=1,
                name='user_1',
                is_admin=False,
                is_domain_expert=False
            ),
            UserDTO(
                user_id=2,
                name='user_2',
                is_admin=False,
                is_domain_expert=False
            )
        ]
    )
    return domain_dto
