import pytest
from unittest.mock import MagicMock

from craps.game import CrappingOut, Dice, Game, GameOver


@pytest.fixture
def dices():
    return [Dice(), Dice()]


def test_shooter_wins_on_opening_roll(dices):
    shooter = MagicMock()
    shooter.roll_dices.return_value = 11

    game = Game()

    game.play(shooter, dices)


def test_roll_dices_crapping_out(dices):
    shooter = MagicMock()
    shooter.roll_dices.return_value = 2

    game = Game()

    with pytest.raises(CrappingOut) as exc_info:
        game.play(shooter, dices)

    assert exc_info.type is CrappingOut


def test_shooter_wins_after_third_attempt(dices):
    def mock_shooter_roll_dices(value, attempts = [6, 4, 6, 7]):
        return attempts.pop(0)

    shooter = MagicMock()
    shooter.roll_dices.side_effect = mock_shooter_roll_dices

    game = Game()

    game.play(shooter, dices)


def test_shooter_loose_after_third_attempt(dices):
    def mock_shooter_roll_dices(value, attempts = [6, 4, 4, 7]):
        return attempts.pop(0)

    shooter = MagicMock()
    shooter.roll_dices.side_effect = mock_shooter_roll_dices

    game = Game()

    with pytest.raises(GameOver) as exc_info:
        game.play(shooter, dices)

    assert exc_info.type is GameOver