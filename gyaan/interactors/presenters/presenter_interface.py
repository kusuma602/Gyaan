from abc import ABC
from abc import abstractmethod


class GetDomainDetailsPresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_domain_id_exception(self):
        pass
