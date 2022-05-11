import random


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


class Game:
    COMING_OUT_ROLL_WIN = [7, 11]
    CRAPPING_OUT = [2, 3, 12]
    END_GAME_RESULT = 7

    def play(self, shooter: Player, dices: list[Dice]) -> None:
        result = shooter.roll_dices(dices)

        if result in self.COMING_OUT_ROLL_WIN:
            return

        if result in self.CRAPPING_OUT:
            raise CrappingOut(result)

        matched = False
        matcher = result

        while result != self.END_GAME_RESULT:
            result = shooter.roll_dices(dices)
            if not matched:
                matched = result == matcher
        
        if not matched:
            raise GameOver(matcher)
