from part1 import update_tail, Pos

def test_same():
    head = Pos(1,1)
    tail = Pos(1,1)

    update_tail(tail, head)

    assert tail.x == 1
    assert tail.y == 1

def test_adjacent_left():
    head = Pos(0,1)
    tail = Pos(1,1)

    update_tail(tail, head)

    assert tail.x == 1
    assert tail.y == 1

def test_adjacent_bottom():
    head = Pos(1,0)
    tail = Pos(1,1)

    update_tail(tail, head)

    assert tail.x == 1
    assert tail.y == 1

def test_move_left():
    head = Pos(-1,1)
    tail = Pos(1,1)

    update_tail(tail, head)

    assert tail.x == 0
    assert tail.y == 1

def test_move_bottom():
    head = Pos(1,-1)
    tail = Pos(1,1)

    update_tail(tail, head)

    assert tail.x == 1
    assert tail.y == 0

def test_move_diag_top_right():
    head = Pos(3,2)
    tail = Pos(1,1)

    update_tail(tail, head)

    assert tail.x == 2
    assert tail.y == 2

def test_move_diag_bottom_left():
    head = Pos(0,-1)
    tail = Pos(1,1)

    update_tail(tail, head)

    assert tail.x == 0
    assert tail.y == 0
