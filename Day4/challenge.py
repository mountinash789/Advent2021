class BingoCard(object):
    raw_data = None
    rows = []
    columns = []
    drawn = []

    def __init__(self, data):
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


def part_two():
    pass


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
        for card in cards:
            b = BingoCard(card)
            card_objs.append(b)

        print(part_one(draw, card_objs))
