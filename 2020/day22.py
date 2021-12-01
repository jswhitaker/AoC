from typing import Optional, Tuple, List


class Game(object):
    def __init__(self, player_1_deck: List[int], player_2_deck: List[int]):
        self.player_1_deck = player_1_deck.copy()
        self.player_2_deck = player_2_deck.copy()
        self.game_history = []

    def __play_round(self) -> Optional[int]:
        # Infinite loop prevention
        current_decks = (','.join([str(i) for i in self.player_1_deck]), ','.join([str(i) for i in self.player_2_deck]))
        if current_decks in self.game_history:
            return 1
        self.game_history.append(current_decks)

        p1_card = self.player_1_deck.pop(0)
        p2_card = self.player_2_deck.pop(0)

        # Recursive Combat
        if p1_card <= len(self.player_1_deck) and p2_card <= len(self.player_2_deck):
            new_game = Game(self.player_1_deck[:p1_card].copy(), self.player_2_deck[:p2_card].copy())
            sub_game_winner, _ = new_game.play_game()
            if sub_game_winner == 1:
                self.player_1_deck.append(p1_card)
                self.player_1_deck.append(p2_card)
            else:
                self.player_2_deck.append(p2_card)
                self.player_2_deck.append(p1_card)

        # Regular Combat
        else:
            if p1_card > p2_card:
                self.player_1_deck.append(p1_card)
                self.player_1_deck.append(p2_card)
            else:
                self.player_2_deck.append(p2_card)
                self.player_2_deck.append(p1_card)
        winner = None
        if len(self.player_1_deck) == 0 or len(self.player_2_deck) == 0:
            winner = 1 if len(self.player_1_deck) > 0 else 2
        return winner

    def play_game(self) -> Tuple[Optional[int], int]:
        winner = None
        while winner is None:
            winner = self.__play_round()
        winning_deck = self.player_1_deck if winner == 1 else self.player_2_deck
        score = sum([i * j for i, j in zip(winning_deck, range(len(winning_deck), 0, -1))])
        return winner, score


def main():
    with open('inputs/22-input.txt') as input_file:
        data = input_file.read()
    decks = data.split('\n\n')
    player_1_deck = [int(i) for i in decks[0].split('\n')[1:]]
    player_2_deck = [int(i) for i in decks[1].split('\n')[1:]]
    game = Game(player_1_deck, player_2_deck)
    _, score = game.play_game()
    return score


# Part 1
def old_main():
    with open('inputs/22-sample.txt') as input_file:
        data = input_file.read()
    decks = data.split('\n\n')
    player_1_deck = [int(i) for i in decks[0].split('\n')[1:]]
    player_2_deck = [int(i) for i in decks[1].split('\n')[1:]]
    while len(player_1_deck) > 0 and len(player_2_deck) > 0:
        p1_card = player_1_deck.pop(0)
        p2_card = player_2_deck.pop(0)
        if p1_card > p2_card:
            player_1_deck.append(p1_card)
            player_1_deck.append(p2_card)
        else:
            player_2_deck.append(p2_card)
            player_2_deck.append(p1_card)
    winning_deck = player_1_deck + player_2_deck
    score = sum([i*j for i, j in zip(winning_deck, range(len(winning_deck), 0, -1))])
    return score


if __name__ == '__main__':
    result = main()
    print(result)
