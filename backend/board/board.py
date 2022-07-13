from backend.board.modifier_spaces import (
    IncomeTax,
    CommunityChest,
    Chance,
    LuxuryTax,
    Go,
    FreeParking,
)


class Outcome:
    def __init__(
        self,
        prob: int,
        space: int | None = None,
        move: int | None = None,
        money: int | None = None,
    ) -> None:
        self.prob = prob
        self.space = space
        self.move = move
        self.money = money


class Board:
    def __init__(self) -> None:
        self.spaces = "test"
