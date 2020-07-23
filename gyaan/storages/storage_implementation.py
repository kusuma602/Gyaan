from typing import List

from django.db.models import Count

from gyaan.interactors.storages.storage_interface import \
    StorageInterface
from gyaan.storages.dtos import DomainDTO


class StorageImplementation(StorageInterface):
    def validate_domain_id(self, domain_id: int):
        from gyaan.models import Domain
        from gyaan.exceptions import InvalidDomainID

        try:
            Domain.objects.get(id=domain_id)
        except Domain.DoesNotExist:
            raise InvalidDomainID

    def get_domain_dto(self, domain_id: int) -> DomainDTO:
        from gyaan.models import Domain
        domain_obj = Domain.objects.get(id=domain_id)
        domain_dto = DomainDTO(
            domain_id=domain_obj.id,
            description=domain_obj.description,
            domain_name=domain_obj.name
        )
        return domain_dto

    def get_domain_posts_count(self, domain_id: int) -> int:
        from gyaan.models import Post
        posts_count_dict = Post.objects\
            .filter(domain_id=domain_id)\
            .aggregate(count=Count('id'))

        posts_count = posts_count_dict['count']

        return posts_count

    def get_domain_members_count(self, domain_id: int) -> int:
        from gyaan.models import DomainFollower
        members_count_dict = DomainFollower.objects\
            .filter(domain_id=domain_id)\
            .aggregate(count=Count('id'))
        members_count = members_count_dict['count']
        print(members_count_dict)
        return members_count

    def get_domain_experts_ids(self, domain_id: int) -> List[int]:
        from gyaan.models import DomainExpert

        expert_ids = DomainExpert.objects\
            .filter(domain_id=domain_id).\
            values_list('expert_id', flat=True)
        return list(expert_ids)

    def get_domain_book_marks_count(self, domain_id: int) -> int:
        return 10
