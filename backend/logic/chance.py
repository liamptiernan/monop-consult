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


class Probability:
    # dice roll - given a position, calculate most likely dice roll
    def roll_dice(self, current_loc):
        dice = {
            2: 0.0278,
            3: 0.0556,
            4: 0.0833,
            5: 0.1111,
            6: 0.1389,
            7: 0.1667,
            8: 0.1389,
            9: 0.1111,
            10: 0.0833,
            11: 0.0556,
            12: 0.0278,
        }

        probability = {}

        # current loc + x = y

        for key in dice.keys():
            space = (key + current_loc) % 40

            probability[space] = dice[key]

        return probability

    def modifiers():
        pass
