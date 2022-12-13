from part2 import update_nodes, Pos

def test_same_with_2():
    poses = [Pos(1,1), Pos(1,1), Pos(1,1)]

    update_nodes(poses)

    assert poses[2].x == 1
    assert poses[2].y == 1

def test_same_with_3():
    poses = [Pos(1,1), Pos(1,1), Pos(1,1)]

    update_nodes(poses)

    assert poses[2].x == 1
    assert poses[2].y == 1

def test_adjacent_left_with_3():
    poses = [Pos(0,1), Pos(1,1), Pos(1,1)]

    update_nodes(poses)

    assert poses[0].x == 0
    assert poses[0].y == 1
    assert poses[1].x == 1
    assert poses[1].y == 1
    assert poses[2].x == 1
    assert poses[2].y == 1

def test_adjacent_bottom_with_3():
    poses = [Pos(1,0), Pos(1,1), Pos(1,1)]

    update_nodes(poses)

    assert poses[0].x == 1
    assert poses[0].y == 0
    assert poses[1].x == 1
    assert poses[1].y == 1
    assert poses[2].x == 1
    assert poses[2].y == 1

def test_move_left_with_three():
    poses = [Pos(-1,1), Pos(1,1), Pos(1,1)]

    update_nodes(poses)

    assert poses[0].x == -1
    assert poses[0].y == 1
    assert poses[1].x == 0
    assert poses[1].y == 1
    assert poses[2].x == 1
    assert poses[2].y == 1

def test_move_bottom_with_three():
    poses = [Pos(1,-1), Pos(1,1), Pos(1,1)]

    update_nodes(poses)

    assert poses[0].x == 1
    assert poses[0].y == -1
    assert poses[1].x == 1
    assert poses[1].y == 0
    assert poses[2].x == 1
    assert poses[2].y == 1

def test_move_diag_top_right_with_three():
    poses = [Pos(3,2), Pos(1,1), Pos(1,1)]

    update_nodes(poses)

    assert poses[0].x == 3
    assert poses[0].y == 2
    assert poses[1].x == 2
    assert poses[1].y == 2
    assert poses[2].x == 1
    assert poses[2].y == 1

def test_move_diag_bottom_left_with_three():
    poses = [Pos(0,-1), Pos(1,1), Pos(1,1)]

    update_nodes(poses)

    assert poses[0].x == 0
    assert poses[0].y == -1
    assert poses[1].x == 0
    assert poses[1].y == 0
    assert poses[2].x == 1
    assert poses[2].y == 1

def test_trail_top_right_diag_top_right_with_three():
    poses = [Pos(2,1), Pos(1,1), Pos(1,1)]

    update_nodes(poses)

    assert poses[0].x == 2
    assert poses[0].y == 1
    assert poses[1].x == 1
    assert poses[1].y == 1
    assert poses[2].x == 1
    assert poses[2].y == 1

    poses[0].y += 1
    update_nodes(poses)

    assert poses[0].x == 2
    assert poses[0].y == 2
    assert poses[1].x == 1
    assert poses[1].y == 1
    assert poses[2].x == 1
    assert poses[2].y == 1

    poses[0].x += 1
    update_nodes(poses)

    assert poses[0].x == 3
    assert poses[0].y == 2
    assert poses[1].x == 2
    assert poses[1].y == 2
    assert poses[2].x == 1
    assert poses[2].y == 1

    poses[0].y += 1
    update_nodes(poses)

    assert poses[0].x == 3
    assert poses[0].y == 3
    assert poses[1].x == 2
    assert poses[1].y == 2
    assert poses[2].x == 1
    assert poses[2].y == 1

    poses[0].x += 1
    update_nodes(poses)

    assert poses[0].x == 4
    assert poses[0].y == 3
    assert poses[1].x == 3
    assert poses[1].y == 3
    assert poses[2].x == 2
    assert poses[2].y == 2
