# pylint: disable=missing-module-docstring
from aiogram.dispatcher.filters.state import StatesGroup, State

class Solve(StatesGroup):
    """StateGroup that solves maze"""
    waitImageState = State()
    waitStartPointState = State()
    waitEndPointState = State()
