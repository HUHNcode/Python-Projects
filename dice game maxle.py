import random

player_count = int(input('Wie viele Spieler?: '))
runden = 0
again = True
game = True
points_all = 51

class Players:
    def __init__(self):
        self.player1 = points_all
        self.player2 = points_all
        self.player3 = points_all
        self.player4 = points_all
        self.player5 = points_all
        self.player6 = points_all

Players_all = Players()

print(Players_all.player1)

while game:
    while True:
        runden += 1
        next_player = runden % player_count
        print(f'RUNDE {runden}')
        print(f'Spieler {next_player + 1}:')

        würfel1 = random.randint(1, 6)
        würfel2 = random.randint(1, 6)
        print(f'Würfel: {würfel1}, {würfel2}')

        except_player = input(f'Spieler {next_player + 2} aussetzen? (J/N): ')
        if except_player.lower() == 'n':
            player_next = input('Ist er sicher? (J/N): ')

            if player_next.lower() == 'n':
                if next_player == 0:
                    Players_all.player1 -= 1
                elif next_player == 1:
                    Players_all.player2 -= 1
                elif next_player == 2:
                    Players_all.player3 -= 1
                elif next_player == 3:
                    Players_all.player4 -= 1
                elif next_player == 4:
                    Players_all.player5 -= 1
                elif next_player == 5:
                    Players_all.player6 -= 1

        if runden >= player_count:
            break

    game = False

print(Players_all.player1)
