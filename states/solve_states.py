from aiogram.dispatcher.filters.state import StatesGroup, State


class Solve(StatesGroup):
    waitImageState = State()
    waitStartPointState = State()
    waitEndPointState = State()
