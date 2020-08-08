from typing import List

from django.db.models import Count

from gyaan.interactors.storages.storage_interface import \
    StorageInterface
from gyaan.storages.dtos import DomainDTO, PostDTO, PostReactionsCountDTO, CommentDTO, CommentRepliesCountDTO, \
    CommentReactionsCountDTO, PostCommentsCountDTO, PostTagDTO


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
        posts_count_dict = Post.objects \
            .filter(domain_id=domain_id) \
            .aggregate(count=Count('id'))

        posts_count = posts_count_dict['count']

        return posts_count

    def get_domain_members_count(self, domain_id: int) -> int:
        from gyaan.models import DomainFollower
        members_count_dict = DomainFollower.objects \
            .filter(domain_id=domain_id) \
            .aggregate(count=Count('id'))
        members_count = members_count_dict['count']
        return members_count

    def get_domain_experts_ids(self, domain_id: int) -> List[int]:
        from gyaan.models import DomainExpert

        expert_ids = DomainExpert.objects \
            .filter(domain_id=domain_id). \
            values_list('expert_id', flat=True)
        return list(expert_ids)

    def get_domain_book_marks_count(self, domain_id: int) -> int:
        return 10

    def get_valid_post_ids(self, post_ids: List[int]) -> List[int]:
        from gyaan.models import Post
        post_ids_in_db = Post.objects.all().values_list('id', flat=True)
        valid_post_ids = [
            post_id
            for post_id in post_ids
            if post_id in post_ids_in_db
        ]
        return valid_post_ids

    def get_post_dtos(self, post_ids: List[int]) -> List[PostDTO]:
        post_dtos = []
        for post_id in post_ids:
            post_dto = self._get_post_dto(post_id)
            post_dtos.append(post_dto)
        return post_dtos

    def get_post_reactions_counts(self, post_ids: List[int]) -> List[PostReactionsCountDTO]:
        post_reaction_count_list = []
        for post_id in post_ids:
            reaction_count_dto = self.get_post_reaction_count(post_id)
            post_reaction_count_list.append(reaction_count_dto)
        return post_reaction_count_list

    @staticmethod
    def get_post_reaction_count(post_id) -> PostReactionsCountDTO:
        from gyaan.models import Reaction
        reactions_count_dict = Reaction.objects \
            .filter(post_id=post_id). \
            aggregate(count=Count('id'))

        return PostReactionsCountDTO(
            post_id=post_id,
            reactions_count=reactions_count_dict['count']
        )

    def get_latest_comment_ids(
            self, post_id: int, no_of_comments: int) -> List[int]:
        from gyaan.models import Comment
        comment_ids = Comment.objects.all(). \
                          values_list('id', flat=True). \
                          order_by('-commented_at')[:no_of_comments]

        comment_ids = list(comment_ids)
        return comment_ids

    def get_comment_dtos(self, comment_ids: List[int]) -> List[CommentDTO]:
        comment_dtos = []
        for comment_id in comment_ids:
            comment_dto = self._get_comment_dto(comment_id)
            comment_dtos.append(comment_dto)
        return comment_dtos

    def get_comment_replies_count(self, comment_ids: List[int]) -> List[CommentRepliesCountDTO]:
        comment_replies_count_dtos = []
        for comment_id in comment_ids:
            replies_count = self._get_comment_replies_count_dto(comment_id)
            comment_replies_count_dtos.append(replies_count)
        return comment_replies_count_dtos

    def get_comment_reactions_count(self, comment_ids: List[int]) -> List[CommentReactionsCountDTO]:
        comment_reaction_count_list = []
        for comment_id in comment_ids:
            reaction_count_dto = self.get_comment_reaction_count(comment_id)
            comment_reaction_count_list.append(reaction_count_dto)
        return comment_reaction_count_list

    def get_post_comments_count(self, post_ids: List[int]) -> List[PostCommentsCountDTO]:
        post_comment_count_dtos = []
        for post_id in post_ids:
            comment_count_dtos = self.get_post_comment_count(post_id)
            post_comment_count_dtos.append(comment_count_dtos)
        return post_comment_count_dtos

    @staticmethod
    def _get_post_dto(post_id) -> PostDTO:
        from gyaan.models import Post
        post_object = Post.objects.get(id=post_id)
        return PostDTO(
            post_id=post_object.id,
            posted_at=post_object.posted_at,
            posted_by_id=post_object.posted_by_id,
            title=post_object.title,
            description=post_object.description,
            domain_id=post_object.domain_id,
            domain_name=post_id.domain.name
        )

    @staticmethod
    def _get_comment_dto(comment_id):
        from gyaan.models import Comment
        comment_object = Comment.objects.get(id=comment_id)
        return CommentDTO(
            comment_id=comment_object.id,
            commented_at=comment_object.commented_at,
            comment_content=comment_object.comment_content,
            commented_by_id=comment_object.commented_by_id,
            post_id=comment_object.post_id
        )

    @staticmethod
    def get_comment_reaction_count(comment_id) -> CommentReactionsCountDTO:
        from gyaan.models import Reaction
        reactions_count_dict = Reaction.objects \
            .filter(comment_id=comment_id). \
            aggregate(count=Count('id'))

        return CommentReactionsCountDTO(
            comment_id=comment_id,
            reactions_count=reactions_count_dict['count']
        )

    @staticmethod
    def _get_comment_replies_count_dto(comment_id) -> CommentRepliesCountDTO:
        from gyaan.models import Comment
        replies_count_dict = Comment.objects.\
            filter(parent_comment_id=comment_id).\
            aggregate(count=Count('id'))

        return CommentRepliesCountDTO(
            comment_id=comment_id,
            replies_count=replies_count_dict['count']
        )

    @staticmethod
    def get_post_comment_count(post_id) -> PostCommentsCountDTO:
        from gyaan.models import Comment
        comments_count_dict = Comment.objects\
            .filter(post_id=post_id)\
            .aggregate(count=Count('id'))

        return PostCommentsCountDTO(
            post_id=post_id,
            comments_count=comments_count_dict['count']
        )

    def get_post_tag_dto(self, post_id: int) -> PostTagDTO:
        pass
