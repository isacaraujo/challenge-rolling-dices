import random

from typing import Callable
from dataclasses import dataclass

class GameOver(Exception):
    def __init__(self, result: int):
        super().__init__(f"expecting: {result}")


class CrappingOut(Exception):
    def __init__(self, result: int):
        super().__init__(f"crapping out: {result}")


class Dice:
    FACES = range(1, 6)

    def roll(self) -> int:
        return random.choice(self.FACES)


class Player:
    def roll_dices(self, dices: list[Dice]) -> int:
        result = map(lambda dice: dice.roll(), dices)
        return sum(result)


@dataclass
class GameEvent:
    result: int
    won: bool


class Game:
    COMING_OUT_ROLL_WIN = [7, 11]
    CRAPPING_OUT = [2, 3, 12]
    END_GAME_RESULT = 7

    def __init__(self) -> None:
        self._observers = []

    def observe(self, observer: Callable[[GameEvent], None]) -> None:
        self._observers.append(observer)

    def play(self, shooter: Player, dices: list[Dice]) -> None:
        result = shooter.roll_dices(dices)

        if result in self.COMING_OUT_ROLL_WIN:
            self._dispatch(GameEvent(result, won=True))
            return

        if result in self.CRAPPING_OUT:
            self._dispatch(GameEvent(result, won=False))
            raise CrappingOut(result)

        matched = False
        matcher = result

        while result != self.END_GAME_RESULT:
            result = shooter.roll_dices(dices)
            if not matched:
                matched = result == matcher
        
        if not matched:
            self._dispatch(GameEvent(matcher, won=False))
            raise GameOver(matcher)

        self._dispatch(GameEvent(matcher, won=True))

    def _dispatch(self, event: GameEvent) -> None:
        for observer in self._observers:
            observer(event)
