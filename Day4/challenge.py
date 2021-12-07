class BingoCard(object):
    id = None
    raw_data = None
    rows = []
    columns = []
    drawn = []

    def __init__(self, data, id):
        self.id = id
        self.raw_data = data
        self.rows = []
        self.columns = []
        self.drawn = []
        for row in data:
            self.rows.append(row)
            for e, value in enumerate(row):
                if len(self.columns) <= e:
                    self.columns.append([])
                self.columns[e].append(value)

    def __str__(self):
        return f'Card {self.id}'

    def draw(self, value):
        self.drawn.append(value)
        for e, row in enumerate(self.rows):
            for c, i in enumerate(row):
                if value == i:
                    self.rows[e].pop(c)
        for e, col in enumerate(self.columns):
            for c, i in enumerate(col):
                if value == i:
                    self.columns[e].pop(c)

    def has_won(self):
        for i in self.rows:
            if len(i) == 0:
                return True
        for i in self.columns:
            if len(i) == 0:
                return True
        return False

    def score(self):
        remaining = []
        for row in self.rows:
            for c in row:
                remaining.append(int(c))
        return sum(remaining) * int(self.drawn[-1])


def part_one(draw, cards):
    for value in draw:
        for card in cards:
            card.draw(value)
            if card.has_won():
                return card.score()


def part_two(draw, cards):
    """
    Answer is 31892 try to reverse engineer it.
    """
    winners = []
    while len(cards) > 0:
        for value in draw:
            if len(cards) == 0:
                break
            winnder_idx = None
            for index, card in enumerate(cards):
                card.draw(value)
                if card.has_won():
                    winnder_idx = index
                    winners.append(card.score())
            if winnder_idx is not None:
                cards.pop(winnder_idx)
    return winners[-1]


if __name__ == "__main__":
    with open('input.txt') as file:
        cards = []
        data = [line.rstrip() for line in file.readlines()]
        draw = data[0].split(',')
        card = None
        for row in data[1:]:
            if len(row) == 0:
                if card:
                    cards.append(card)
                card = []
            else:
                l = []
                for i in row.split(' '):
                    x = i.replace(' ', '')
                    if len(x) > 0:
                        l.append(x)
                card.append(l)
        cards.append(card)

        card_objs = []
        for i, card in enumerate(cards, start=1):
            b = BingoCard(card, i)
            card_objs.append(b)

        print(part_one(draw, card_objs))
        print(part_two(draw, card_objs))
