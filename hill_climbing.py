import math
import random

def random_queen():
    queen_list = [0] * 8
    for i in range(8):
        queen_list[i] = random.randint(0, 7)
    return queen_list


def number_of_attacks(list):
    count = 0
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            distance_of_rows = math.pow(list[i] - list[j], 2)
            distance_of_column = math.pow(i - j, 2)
            if distance_of_rows == 0:
                count += 1
            elif distance_of_column == distance_of_rows:
                count += 1
    return count


def create_heuristic_matrix(queen_list):
    solution_matrix = [[0] * 8 for k in range(8)]
    for j in range(8):
        real_value = queen_list[j]
        for i in range(8):
            queen_list[j] = i
            solution_matrix[j][i] = number_of_attacks(queen_list)
        queen_list[j] = real_value
    return solution_matrix


def print_board(queen_list):
    board = [["-"] * 8 for k in range(len(queen_list))]
    for j in range(len(board)):
        for i in range(len(board)):
            if queen_list[j] == i:
                board[i][j] = "Q"
    for i in board:
        print(i)


def print_matrix(matrix):
    board = [["-"] * 8 for k in range(8)]
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            board[i][j] = matrix[j][i]
    for i in board:
        print(i)


def find_min(matrix):
    min_value = 1000
    for clm in matrix:
        for element in clm:
            if min_value > element:
                min_value = element
    return min_value


def best_successor(attack_matrix, queen_list):
    list_of_min = []
    min_value = find_min(attack_matrix)
    for i in range(len(attack_matrix)):
        for j in range(len(attack_matrix)):
            if attack_matrix[i][j] == min_value:
                list_of_min.append([i, j])
    var = random.randint(0, len(list_of_min)-1)
    x,y = list_of_min[var]
    new_queen_list = queen_list.copy()
    new_queen_list[x] = y
    return new_queen_list


def hill_climbing_algorithm():
    queen_list = random_queen()
    random_count = 0
    shift_count = 0
    while number_of_attacks(queen_list) != 0:
        attack_matrix = create_heuristic_matrix(queen_list)
        new_queen_list = best_successor(attack_matrix, queen_list)
        shift_count += 1
        if number_of_attacks(new_queen_list) < number_of_attacks(queen_list):
            queen_list = new_queen_list
        else:
            random_count += 1
            queen_list = random_queen()
    return queen_list, random_count, shift_count


for i in range(15):
    list31, rc, sc = hill_climbing_algorithm()
    print_matrix(create_heuristic_matrix(list31))
    print_board(list31)
    print()
    print(list31, rc, sc)
    print(number_of_attacks(list31))
    print()

