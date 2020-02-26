import enum

def find_winning_move(game_state, next_player):
    for candidate_move in game_state.legal_moves(next_player):
        next_state = game_state.apply_move(candidate_move)
        if next_state.is_over() and next_state.winner == next_player:
            return candidate_move
    return None

def eliminate_losing_moves(game_state, next_player):
    opponent = next_player.other()
    possible_moves = []
    for candidate_move in game_state.legal_moves(next_player):
        next_state = game_state.apply_move(candidate_move)
        opponent_winning_move = find_winning_move(next_state, opponent)
        if opponent_winning_move is None:
            possible_moves.append(candidate_move)
        return possible_moves

def find_two_state_move(game_state, next_player):
    opponent = next_player.other()
    for candidate_move in game_state.legal_moves(next_player):
        next_state = game_state.apply_move(candidate_move)
        good_responses = eliminate_losing_moves(next_state, opponent)
        if not good_responses:
            return candidate_move
    return None

class GameResult(enum.Enum):
    loss = 1
    draw = 2
    win = 3

def best_result(game_state):
    if game_state.is_over():
        if game_state.winner() == game_state.next_player:
            return GameResult.win
        elif game_state.winner() is None:
            return GameResult.draw
        else:
            return GameResult.loss
        
