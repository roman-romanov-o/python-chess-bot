import re
from bot_vesrions.classic import ChessGame
from enum import Enum
from dataclasses import dataclass
import typing

MAX_MOVES = 10 ** 20
EXAMPLE_RESPONSE = """
[White "lichess AI level 4"]
[Black "Romanov_Roman"]
1. e4 e5 
2. Nf3 Nc6 
3. Bc4 h6 
{ C50 Italian Game: Anti-Fried Liver Defense } 
4. d3 a6 
5. c3 Nf6 
6. Be3 Be7 
7. a3 O-O 
8. Nbd2 Ng4 
9. Qc2 Nxe3 
10. fxe3 Bg5 
11. h4 Be7 
12. Bd5 Qe8 
13. b4 d6 
14. c4 Nd8 
15. Rc1 Be6 16. d4 exd4 17. Nf1 Bxd5 18. exd5 c6 19. Nxd4 Rc8 20. Qf5 Rc7 21. Qb1 c5 22. Nf3 b6 23. Kf2 Nb7 24. Qd3 Qd8 25. Rc2 Qc8 26. e4 cxb4 27. axb4 b5 28. Ne3 Bd8 29. Qe2 a5 30. Nd4 axb4 31. g3 bxc4 32. Nxc4 Nc5 33. Nxd6 Qd7 34. N6b5 Be7 35. Nxc7 Qxc7 36. Nb5 Qb6 37. Nd4 b3 38. Nf5 Re8 39. Qg4 Nd3+ 40. Kg2 { Black resigns. } 1-0
"""


class SpecialMoves(Enum):
    SHORT_CASTLING = 1
    LONG_CASTLING = 2
    DRAW = 3


SPECIAL_NOTATION_MAPING = {
    'O-O': SpecialMoves.SHORT_CASTLING,
    'O-O-O': SpecialMoves.LONG_CASTLING,
    '1/2-1/2': SpecialMoves.DRAW
}

ALL_X_COORDINATES_MAPING = {
    word: index
    for word, index in enumerate('abcdefgh'.split(''))
}

ALL_Y_COORDINATES_MAPING = {
    word: index
    for word, index in enumerate('12345678'.split(''))
}

ALL_COMBINATIONS = {
    f'{word_1}_{word_2}': (index_1, index_2)
    for word_1, index_1 in ALL_X_COORDINATES_MAPING.items()
    for word_2, index_2 in ALL_Y_COORDINATES_MAPING.items()
}


@dataclass
class Coordinate:
    x: int
    y: int


class MoveType(Enum):
    SIMPLE = 1
    SHORT_CASTLING = 2
    LONG_CASTLING = 3
    DRAW = 4


@dataclass
class Move:
    move_type: MoveType
    first_coordinate: typing.Optional[Coordinate]
    second_coordinate: typing.Optional[Coordinate]


def raw_move_to_coordinate(raw_move: str) -> Move:
    parsed = raw_move.parse('(%s %s)')
    first_move_string = parsed.group(0)
    second_move_string = parsed.group(1)
    special_notation_move = SPECIAL_NOTATION_MAPING.get(first_move_string, None)
    if special_notation_move is not None:
        return Move(special_notation_move, None, None)
    simple_move_x_1 = first_move_string[0]
    simple_move_y_1 = first_move_string[1]
    simple_move_x_2 = second_move_string[0]
    simple_move_y_2 = second_move_string[1]
    return Move(
        move_type=MoveType.SIMPLE,
        first_coordinate=Coordinate(
            x=simple_move_x_1,
            y=simple_move_y_1,
        ),
        second_coordinate=Coordinate(
            x=simple_move_x_2,
            y=simple_move_y_2,
        ),
    )


def parse_game_notation(notation: str) -> ChessGame:
    white_player = re.parse('[White %s]', notation)
    black_player = re.parse('[Black %s]', notation)
    moves = []
    for move_index in range(0, MAX_MOVES):
        move_search_regexp = fr'{move_index}. %(coordinate_1)s %(coordinate_2)s'
        move = re.parse(move_search_regexp, notation)
        if move is None:
            break
        moves.append(move_rxaw)

    return ChessGame(white_player, black_player, raw_move_to_coordinate(moves))