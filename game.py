class Player:
    def __init__(self, name):
        self.name = name
        self.total = 500
        self.move = -1

p1 = Player(input("Player 1 Name: "))
p2 = Player(input("Player 2 Name: "))


def new_game(p1, p2):
    while p1.total != 0 and p2.total != 0:
        new_round(p1, p2)
        print_players()

if p1.total == p2.total:
    print("tie")
else:
    print("Winner: {}".format((p2.name, p1.name)[p1.total > p2.total]))

def new_round(p1, p2):
    p1.move = input("What's your move, Player 1?").capitalize()
    p2.move = input("What's your move, Player 2?").capitalize()

compare(p1, p2)

def compare(p1, p2):
  results = {
    ('Split','Split') :split_split,
    ('Steal','Split') : steal_split,
    ('Split','Steal') : split_steal,
    ('Steal','Steal') : steal_steal
  }

  results[(p1.move, p2.move)](p1, p2)

def split_split(p1, p2):
  larger = max(p1.total, p2.total)
  p1.total += larger/2
  p2.total += larger/2

def steal_split(p1, p2):
  p1.total += p2.total
  p2.total = 0

def split_steal(p1, p2):
  p2.total += p1.total
  p1.total = 0

def steal_steal(p1, p2):
  p1.total = 0
  p2.total = 0

def print_players():
  players = [p1, p2]
  for player in players:
    print("{} : {}".format(player.name, player.total))

new_game(p1, p2)