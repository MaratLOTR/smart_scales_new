from dependency_injector import containers, providers

from config import DatabaseSettings
from repositories import UserRepository, ParametersRepository
from utils.database import get_connection_url, Database
from utils.recommendation_system import RecommendationSystem
from web.controllers import UpdatePulseTemperaturePressureController, AuthenticationController, \
    GetWeightFatMuscleMassController
from web.controllers.Users import UsersController
from web.controllers.get_pulse_temperature_pressure import GetPulseTemperaturePressureController
from web.controllers.update_weight_fat_muscle_mass import UpdateWeightFatMuscleMassController
from web.controllers.registry_new_user import RegistrationNewUserController


class UserControllerContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["web.views.users"])
    config = providers.Configuration()
    config.from_pydantic(DatabaseSettings())
    database = providers.Singleton(Database, db_url=get_connection_url(config))

    user_repository = providers.Factory(
        UserRepository,
        session_factory=database.provided.session,
    )

    parameters_repository = providers.Factory(
        ParametersRepository,
        session_factory=database.provided.session,
    )

    recommendation_system = providers.Factory(RecommendationSystem)

    update_weight_fat_muscle_mass_controller = providers.Factory(
        UpdateWeightFatMuscleMassController,
        user_repository=user_repository,
    )

    update_pulse_temperature_pressure_controller = providers.Factory(
        UpdatePulseTemperaturePressureController,
        user_repository=user_repository,
    )

    user_controller = providers.Factory(
        UsersController,
        user_repository=user_repository,
    )

    registration_new_user_controller = providers.Factory(
        RegistrationNewUserController,
        user_repository=user_repository,
    )

    authentication_controller = providers.Factory(
        AuthenticationController,
        user_repository=user_repository
    )

    get_pulse_temperature_pressure_controller = providers.Factory(
        GetPulseTemperaturePressureController,
        user_repository=user_repository,
        recommendation_system=recommendation_system,
    )

    get_weight_fat_muscle_mass_controller = providers.Factory(
        GetWeightFatMuscleMassController,
        user_repository=user_repository,
        recommendation_system=recommendation_system,
    )

class ParametersControllerContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["web.views.parameters"])
    config = providers.Configuration()
    config.from_pydantic(DatabaseSettings())
    database = providers.Singleton(Database, db_url=get_connection_url(config))

    parameters_repository = providers.Factory(
        ParametersRepository,
        session_factory=database.provided.session,
    )


    