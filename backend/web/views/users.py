from typing import Optional

from fastapi import APIRouter, Depends, Response, status, HTTPException
from dependency_injector.wiring import inject, Provide

from schemas import UsersSchemas, AuthResponseSchemas, PulseTemperaturePressureStatusResponseModel, \
    WeightFatMuscleMassResponseModel
from web.controllers import UpdatePulseTemperaturePressureController, AuthenticationController, \
    GetWeightFatMuscleMassController
from web.controllers.Users import UsersController
from web.containers.Container import UserControllerContainer
from web.controllers.get_pulse_temperature_pressure import GetPulseTemperaturePressureController
from web.controllers.update_weight_fat_muscle_mass import UpdateWeightFatMuscleMassController
from web.controllers.registry_new_user import RegistrationNewUserController

router = APIRouter(prefix="/users")


# @router.get("/hello/marat")
# @inject
# def hello_world():
#     return "Hello world!!!!!!!!!!!!!!!"
#
#
# @router.get("/all")
# @inject
# def get_all_user(
#         user_controller: UsersController = Depends(Provide[UserControllerContainer.user_controller]),
# ):
#     print("Hello world")
#     return user_controller.get_all_users()
#
#
# @router.get("/{user_id}")
# @inject
# def get_user_by_id(
#         user_id: int,
#         user_controller: UsersController = Depends(Provide[UserControllerContainer.user_controller]),
# ):
#     return user_controller.get_user_by_id(user_id=user_id)


@router.post("/register")
@inject
def insert_new_user(sex: bool, name: str, height: int, email: str,
        controller: RegistrationNewUserController = Depends(Provide[UserControllerContainer.registration_new_user_controller]),
):
    try:
        controller(name=name, sex=sex, height=height, email=email)
    except ValueError as msg:
        raise HTTPException(status_code=400, detail=str(msg))


@router.put("/weight_fat_muscle_mass")
@inject
def insert_weight_fat_muscle_mass(
        user_id: int,
        weight: Optional[int] = None,
        fat_mass: Optional[int] = None,
        muscle_mass: Optional[int] = None,
        controller: UpdateWeightFatMuscleMassController = Depends(Provide[UserControllerContainer.update_weight_fat_muscle_mass_controller]),
):
    try:
        controller(user_id=user_id, weight=weight, fat_mass=fat_mass, muscle_mass=muscle_mass)
    except ValueError as msg:
        raise HTTPException(status_code=400, detail=str(msg))


@router.put("/pulse_temperature_pressure")
@inject
def update_pulse_temperature_pressure(
        user_id: int,
        pulse: Optional[int] = None,
        temperature: Optional[int] = None,
        diastolic_pressure: Optional[int] = None,
        systolic_pressure: Optional[int] = None,
        controller: UpdatePulseTemperaturePressureController =
        Depends(Provide[UserControllerContainer.update_pulse_temperature_pressure_controller]),
):
    try:
        controller(user_id=user_id, pulse=pulse, temperature=temperature, diastolic_pressure=diastolic_pressure,
                   systolic_pressure=systolic_pressure)
    except ValueError as msg:
        raise HTTPException(status_code=400, detail=str(msg))


@router.get("/auth/", response_model=AuthResponseSchemas)
@inject
def auth(
        email: str,
        controller: AuthenticationController = Depends(Provide[UserControllerContainer.authentication_controller]),
):
    try:
        return controller(email=email)
    except ValueError as msg:
        raise HTTPException(status_code=400, detail=str(msg))


@router.get("/pulse_pressure_temperature/", response_model=PulseTemperaturePressureStatusResponseModel)
@inject
def get_pulse_pressure_temperature(user_id: int,
                                   controller: GetPulseTemperaturePressureController =
                                   Depends(Provide[UserControllerContainer.get_pulse_temperature_pressure_controller])):
    try:
        return controller(user_id=user_id)
    except ValueError as msg:
        raise HTTPException(status_code=400, detail=str(msg))


@router.get("/weight_fat_muscle_mass/", response_model=WeightFatMuscleMassResponseModel)
@inject
def get_weight_fat_muscle_mass(user_id: int,
                               controller: GetWeightFatMuscleMassController =
                               Depends(Provide(UserControllerContainer.get_weight_fat_muscle_mass_controller))):
    try:
        return controller(user_id=user_id)
    except ValueError as msg:
        raise HTTPException(status_code=400, detail=str(msg))
