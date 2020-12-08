class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def getNextPlayerposition(player_position, player_movement, length):
    player_position.y = player_position.y + player_movement.y
    player_position.x = player_position.x + player_movement.x
    while player_position.x >= length:
        player_position.x = player_position.x - length
    return player_position

def getHitTrees(player_position, player_movement):
    trees_hit = 0
    length = 0
    data = open('input/day3.txt', 'r')
    for line_number, line_content in enumerate(data):
        if not length:
            length = len(line_content) - 1
            player_position = getNextPlayerposition(player_position, player_movement, length)
            continue
        if player_position.y != line_number:
            continue
        if line_content[player_position.x] == '#':
            trees_hit += 1
        player_position = getNextPlayerposition(player_position, player_movement, length)
    data.close()
    return trees_hit


print("Day 3, Challenge 1")
hitTrees_3_1 = getHitTrees(Vector2(0, 0), Vector2(3, 1))
print("3, 1 hit", hitTrees_3_1, "trees")

hitTrees_1_1 = getHitTrees(Vector2(0, 0), Vector2(1, 1))
hitTrees_5_1 = getHitTrees(Vector2(0, 0), Vector2(5, 1))
hitTrees_7_1 = getHitTrees(Vector2(0, 0), Vector2(7, 1))
hitTrees_1_2 = getHitTrees(Vector2(0, 0), Vector2(1, 2))
print("Day 3, Challenge 2")
print("3, 1 hit", hitTrees_3_1, "trees")
print("1, 1 hit", hitTrees_1_1, "trees")
print("5, 1 hit", hitTrees_5_1, "trees")
print("7, 1 hit", hitTrees_7_1, "trees")
print("1, 2 hit", hitTrees_1_2, "trees")
print("product", hitTrees_1_1*hitTrees_3_1*hitTrees_5_1*hitTrees_7_1*hitTrees_1_2)
