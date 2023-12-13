from typing import Optional

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from web.controllers.Users import UsersController
from web.containers.Container import UserControllerContainer

router = APIRouter(prefix="/users",)


@router.get("/hello/marat")
@inject
def hello_world():
    return "Hello world!!!!!!!!!!!!!!!"


@router.get("/all")
@inject
def get_all_user(
        user_controller: UsersController = Depends(Provide[UserControllerContainer.user_controller]),
):
    print("Hello world")
    return user_controller.get_all_users()


@router.get("/{user_id}")
@inject
def get_user_by_id(
        user_id: int,
        user_controller: UsersController = Depends(Provide[UserControllerContainer.user_controller]),
):
    return user_controller.get_user_by_id(user_id=user_id)


@router.post("/new")
@inject
def insert_new_user(
        sex: int,
        name: str,
        height: int,
        user_controller: UsersController = Depends(Provide[UserControllerContainer.user_controller]),
):
    return user_controller.insert_new_user(name=name, sex=sex, height=height)


@router.post("/new_user_with_parameters")
@inject
def insert_new_user_with_parameters(
        sex: int,
        name: str,
        height: int,
        user_controller: UsersController = Depends(Provide[UserControllerContainer.insert_new_user_controller]),
):
    return user_controller(name=name, sex=sex, height=height)
