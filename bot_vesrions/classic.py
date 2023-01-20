import uuid
from dataclasses import dataclass
from enum import Enum
from typing import List, Any


@dataclass
class Player:
    name: str
    piece_to_id = Any


class Color(Enum):
    BLACK = 1
    WHITE = 2


class ChessGameResult(Enum):
    PLAYER_1_WINS = 1
    PLAYER_2_WINS = 2
    DRAW = 3
    UNKNOWN = 4


class ChessGameStrategy(Enum):
    RANDOM = 1
    GREEDY = 2
    COUNT_MOVES = 3
    DRAW_IS_FINE = 4
    GENERATED_BY_COMPUTER = 5


class PieceType:
    PAWN = 1
    BISHOP = 2
    KNIGHT = 3
    QUEEN = 4
    TOURA = 5


class Piece:
    _id: str = None
    color: Color
    type: PieceType
    player: Player

    def __init__(self, color, type, player):
        self.color = color
        self.type = type
        self.player = player


    def piece_id(self):
        if self._id is None:
            self._id = uuid.uuid1()
        else:
            return self._id


    def __sub__(self, other: 'Piece'):
        self.player.piece_to_id.remove(self.piece_id)
        other.player.piece_to_id.remove(other.piece_id)


@dataclass
class ChessMove:
    x_1: int
    x_2: int
    y_1: int
    y_2: int
    player: Player
    available_pieces: List[Piece]
    time_to_player: dict[Player, float]


@dataclass
class ChessBoard:
    max_x: int
    max_y: int
    board: list[Player]
    moves: list[ChessMove]
    player_1_pieces: list[Piece]
    player_2_pieces: list[Piece]


@dataclass
class ChessGame:
    player_1: Player
    player_2: Player
    board: ChessBoard
    result: ChessGameResult


class ClassicPieceValue(Enum):
    PAWN = 1
    ROOK = 5
    KNIGHT = 3
    BISHOP = 3
    QUEEN = 10
    KING = 1


class ClassicPieceValue:
    piece: Piece
    def __add__(self, other, current_strategic=ChessGameStrategy.COUNT_MOVES):
        if current_strategic == ChessGameStrategy.COUNT_MOVES:
            if (
                self.piece.type == PieceType.BISHOP and
                other.piece.type == PieceType.BISHOP and
                current_strategic == ChessGameStrategy.COUNT_MOVES
            ):
                return 6.10

            return self.piece.value + other.piece.value
        else:
            raise NotImplementedError


class PieceStrategyType(Enum):
    SAVE_ALL = 1
    SAVE_BEST = 2
    SAVE_BEST_AND_ALL = 3
    SAVE_ALL_KING_DIE = 4
    BOARD_TO_SMALL = 5


class PieceStrategy:
    SAVE_YOURSELF = 1
    SAVE_ALL = 2
    SAVE_PAWN = 3


PIECE_TO_STRATEGY = {
    PieceType.PAWN: PieceStrategy.SAVE_YOURSELF,
    PieceType.ROOK: PieceStrategy.SAVE_ALL_YOUR_PIECES,
    PieceType.KNIGHT: PieceStrategy.SAVE_ALL_YOUR_PIECES,
    PieceType.BISHOP: PieceStrategy.SAVE_ALL_YOUR_PIECES,
    PieceType.QUEEN: PieceStrategy.SAVE_ALL_YOUR_PIECES,
    PieceType.KING: PieceStrategy.LOVE_ALL_YOUR_PIECES,
}




player_1 = Player(name='player 1')
player_2 = Player(name='player_2')


GAME = ChessBoard(
    max_x=8,
    max_y=8,
    board=[player_1, player_2],
    moves=[],
    player_1_pieces=[
        Piece(color=Color.WHITE, name='pawn') * 10,
        Piece(color=Color.WHITE, name='rook') * 2,
        Piece(color=Color.WHITE, name='knight') * 2,
        Piece(color=Color.WHITE, name='bishop') * 2,
        Piece(color=Color.WHITE, name='queen') * 1,
        Piece(color=Color.WHITE, name='king') * 1,
    ],
    player_2_pieces=[
        Piece(color=Color.BLACK, name='pawn') * 10,
        Piece(color=Color.BLACK, name='rook') * 2,
        Piece(color=Color.BLACK, name='knight') * 2,
        Piece(color=Color.BLACK, name='bishop') * 2,
        Piece(color=Color.BLACK, name='queen') * 1,
        Piece(color=Color.BLACK, name='king') * 1,
    ],
    result=ChessGameResult.UNKNOWN
)


class GameResult:
    player_1_color: Color
    player_2_color: Color
    result: ChessGameResult

    def generate_score(self):
        pass

@dataclass
class GameScore:
    player_1_score: float
    player_2_score: float


def generate_classic_score(game: ChessGame) -> GameScore:
    for player_1_pieces in

class CurrentGameScore:
    player_1_color: Color
    player_2_color: Color
    _current_score: float


    def __init__(self, game):
        return ...
    @property
    def current_score(self):
        if ChessStrategy.CLASSIC:



def find_perfect_combination(player, pieces):
    pass

def generate_chess_combination_score(player, pieces):
    pass

def find_history_combinations(player, pieces):
    pass



if __name__ == '__main__':
    players = [player_1, player_2]

    while GAME.result == ChessGameResult.UNKNOWN:
        current_player_index = 0
        max_player_index = len(players)
        while True:
            current_player_index += 1
            if current_player_index == max_player_index:
                current_player_index = 0

            current_player = players[current_player_index]
            if current_player == player_1:
                for piece in GAME.player_1_pieces:
                    pass



