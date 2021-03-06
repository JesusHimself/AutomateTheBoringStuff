def isValidChessBoard(board):
    validChessboard = {'1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h',
                       '1g','2g', '3g', '4g', '5g', '6g', '7g', '8g',
                       '1f', '2f', '3f', '4f', '5f', '6f', '7f', '8f',
                       '1e', '2e', '3e', '4e', '5e', '6e', '7e', '8e',
                       '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d',
                       '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c',
                       '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b',
                       '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a'}
    types = {'pawn': 8, 'knight': 1, 'bishop': 1, 'rook': 1, 'queen': 1, 'king': 1}
    colours = ('b', 'w')
    
    # Make use of fault error when dictionaries don't match! (try, exempt)
    