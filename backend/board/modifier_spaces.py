from backend.board.board import Outcome


class ModifierSpace:
    def __init__(self, outcomes: list[Outcome]):
        # effects: odds, outcome.
        # outcome - move, money
        self.outcomes = outcomes


class IncomeTax(ModifierSpace):
    def __init__(self):
        outcome = Outcome(prob=1, money=-200)
        self.outcomes = [outcome]


class CommunityChest(ModifierSpace):
    def __init__(self):
        # outcome = Outcome(prob=1, money=-200)
        self.outcomes = []


class Chance(ModifierSpace):
    def __init__(self):
        # outcome = Outcome(prob=1, money=-200)
        self.outcomes = []


class LuxuryTax(ModifierSpace):
    def __init__(self):
        # outcome = Outcome(prob=1, money=-200)
        self.outcomes = []


class Go(ModifierSpace):
    def __init__(self):
        # outcome = Outcome(prob=1, money=-200)
        self.outcomes = []


class FreeParking(ModifierSpace):
    def __init__(self):
        # outcome = Outcome(prob=1, money=-200)
        self.outcomes = []
