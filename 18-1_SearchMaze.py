def is_path(maze, x, y):
    """Perform DFS on a rectangle Maze, start from x,y coordinates and find end.

    W = White Piece (passable), B = Black Piece (impassable), E = End

    Args:
        maze: 2-d List Containing W,B,E chars for pieces
        x: starting x-coordinate
        y: starting y-coordinate

    Returns:
        Boolean of if maze is passable (is a path)

    """

    # If we're out of bounds, or a black piece, or a already visited piece return false
    if x >= len(maze[0]) or x < 0 or y >= len(maze) or y < 0 or maze[y][x] in ['B', 'V']:
        return False

    # We found it
    elif maze[y][x] == 'E':
        return True

    # Keep searching
    else:
        maze[y][x] = 'V'
        return is_path(maze, x-1, y) or is_path(maze, x+1, y) or is_path(maze, x, y-1) or is_path(maze, x, y+1)


if __name__ == "__main__":
    """Test"""
    maze_board_passable = [
        ['W', 'B', 'W', 'W', 'B'],
        ['W', 'W', 'W', 'W', 'W'],
        ['B', 'W', 'B', 'B', 'W'],
        ['W', 'W', 'W', 'W', 'W'],
        ['W', 'B', 'B', 'W', 'B'],
        ['W', 'E', 'W', 'W', 'B'],
    ]

    maze_board_impassable = [
        ['W', 'B', 'W', 'W', 'B'],
        ['W', 'W', 'W', 'W', 'W'],
        ['B', 'W', 'B', 'B', 'W'],
        ['W', 'W', 'W', 'W', 'W'],
        ['W', 'B', 'B', 'W', 'B'],
        ['B', 'E', 'B', 'W', 'B'],
    ]

    passable_path = is_path(maze_board_passable, 2, 0)
    impassable_path = is_path(maze_board_impassable, 2, 0)

    print("Passable:", passable_path)
    print("Impassable:", impassable_path)
