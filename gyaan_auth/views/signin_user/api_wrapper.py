from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from common.oauth2_storage import OAuth2SQLStorage
from .validator_class import ValidatorClass

from gyaan_auth.storages.storage_implementation import StorageImplementation
from gyaan_auth.presenters.presenter_implementation import  \
        LoginPresenterImplementation
from gyaan_auth.interactors.login_interactor import LoginInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']
    storage = StorageImplementation()
    presenter = LoginPresenterImplementation()
    oauth2_storage = OAuth2SQLStorage()
    interactor = LoginInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage
    )
    response = interactor.login_wrapper(
        presenter=presenter,
        username=username,
        password=password
    )
    return response
