"""Exact finite checks for the corner-coherence examples in note.tex."""

from fractions import Fraction
from itertools import permutations, product
import json
from pathlib import Path


Rational = Fraction
WORDS = tuple(product(range(2), repeat=3))


def phase_sum(frequency):
    coefficients = [0, 0, 0]
    for phase in range(3):
        coefficients[(phase * frequency) % 3] += 1
    return (coefficients[0] - coefficients[2], coefficients[1] - coefficients[2])


def twirled_diagonal(parameters):
    return [
        product_fraction(
            probability if bit == 0 else 1 - probability
            for probability, bit in zip(parameters, word)
        )
        for word in product(range(2), repeat=len(parameters))
    ]


def product_fraction(values):
    result = Rational(1)
    for value in values:
        result *= value
    return result


def squared_distance(diagonal_first, corner_first, diagonal_second, corner_second):
    return sum((first - second) ** 2 for first, second in zip(diagonal_first, diagonal_second)) + 2 * (corner_first - corner_second) ** 2


def corner_matrix(diagonal, corner):
    dimension = len(diagonal)
    matrix = [[Rational(0) for column in range(dimension)] for row in range(dimension)]
    for position, value in enumerate(diagonal):
        matrix[position][position] = value
    matrix[0][-1] = matrix[-1][0] = corner
    return matrix


def matrix_multiply(first, second):
    dimension = len(first)
    return [[sum(first[row][middle] * second[middle][column] for middle in range(dimension)) for column in range(dimension)] for row in range(dimension)]


def characteristic_coefficients(matrix):
    dimension = len(matrix)
    coefficients = [Rational(0)] * (dimension + 1)
    for permutation in permutations(range(dimension)):
        inversions = sum(permutation[first] > permutation[second] for first in range(dimension) for second in range(first + 1, dimension))
        term = [Rational((-1) ** inversions)]
        for row, column in enumerate(permutation):
            factor = [-matrix[row][column], Rational(row == column)]
            next_term = [Rational(0)] * (len(term) + 1)
            for first_power, first_value in enumerate(term):
                for second_power, second_value in enumerate(factor):
                    next_term[first_power + second_power] += first_value * second_value
            term = next_term
        coefficients = [first + second for first, second in zip(coefficients, term)]
    return coefficients


def root_coefficients(roots):
    coefficients = [Rational(1)]
    for root in roots:
        next_coefficients = [Rational(0)] * (len(coefficients) + 1)
        for power, coefficient in enumerate(coefficients):
            next_coefficients[power] -= root * coefficient
            next_coefficients[power + 1] += coefficient
        coefficients = next_coefficients
    return coefficients


def gaussian_multiply(first, second):
    return (first[0] * second[0] - first[1] * second[1], first[0] * second[1] + first[1] * second[0])


def check_isotropic_product_mixture():
    half = Rational(1, 2)
    local_parameters = [(1, 0, 0), (0, 0, 0), (half, half, 0), (half, -half, 0), (half, 0, half), (half, 0, -half)]
    average = [[(Rational(0), Rational(0)) for column in range(4)] for row in range(4)]
    for diagonal_first, real_corner, imaginary_corner in local_parameters:
        local = [[(Rational(diagonal_first), Rational(0)), (Rational(real_corner), Rational(imaginary_corner))], [(Rational(real_corner), -Rational(imaginary_corner)), (1 - Rational(diagonal_first), Rational(0))]]
        assert diagonal_first * (1 - diagonal_first) == real_corner ** 2 + imaginary_corner ** 2
        for row, column in product(range(4), repeat=2):
            first = local[row // 2][column // 2]
            second = local[row % 2][column % 2]
            entry = gaussian_multiply(first, (second[0], -second[1]))
            previous = average[row][column]
            average[row][column] = (previous[0] + entry[0] / 6, previous[1] + entry[1] / 6)
    expected = corner_matrix([Rational(1, 3), Rational(1, 6), Rational(1, 6), Rational(1, 3)], Rational(1, 6))
    assert average == [[(entry, Rational(0)) for entry in row] for row in expected]


def polynomial_add(first, second):
    result = first.copy()
    for powers, coefficient in second.items():
        result[powers] = result.get(powers, 0) + coefficient
    return {powers: coefficient for powers, coefficient in result.items() if coefficient}


def polynomial_scale(polynomial, coefficient):
    return {powers: value * coefficient for powers, value in polynomial.items() if value * coefficient}


def polynomial_multiply(first, second):
    result = {}
    for first_powers, first_coefficient in first.items():
        for second_powers, second_coefficient in second.items():
            powers = tuple(first_power + second_power for first_power, second_power in zip(first_powers, second_powers))
            result[powers] = result.get(powers, 0) + first_coefficient * second_coefficient
    return {powers: coefficient for powers, coefficient in result.items() if coefficient}


def constant(value):
    return {(0, 0, 0, 0): Rational(value)} if value else {}


def variable(position):
    powers = [0, 0, 0, 0]
    powers[position] = 1
    return {tuple(powers): Rational(1)}


def subtract(first, second):
    return polynomial_add(first, polynomial_scale(second, -1))


def square(polynomial):
    return polynomial_multiply(polynomial, polynomial)


def check_square_completion():
    shape_a, shape_b, real_corner, imaginary_corner = [variable(position) for position in range(4)]
    upper_corner = polynomial_scale(shape_a, Rational(1, 2))
    upper_middle = polynomial_scale(shape_b, Rational(1, 3))
    lower_middle = polynomial_scale(subtract(subtract(constant(1), shape_a), shape_b), Rational(1, 3))
    distance = {}
    for coefficient, term in [
        (2, subtract(constant(Rational(1, 5)), upper_corner)),
        (3, subtract(constant(Rational(1, 5)), upper_middle)),
        (3, lower_middle),
        (2, subtract(constant(Rational(11, 112)), real_corner)),
        (2, imaginary_corner),
    ]:
        distance = polynomial_add(distance, polynomial_scale(square(term), coefficient))
    certificate = constant(Rational(109, 23520))
    for coefficient, term in [
        (2, subtract(upper_corner, constant(Rational(3, 16)))),
        (3, subtract(upper_middle, constant(Rational(3, 16)))),
        (3, subtract(lower_middle, constant(Rational(1, 48)))),
        (2, subtract(real_corner, constant(Rational(1, 16)))),
        (2, imaginary_corner),
    ]:
        certificate = polynomial_add(certificate, polynomial_scale(square(term), coefficient))
    halfspace = subtract(
        subtract(constant(Rational(1, 2)), polynomial_scale(polynomial_add(shape_a, shape_b), Rational(7, 15))),
        real_corner,
    )
    certificate = polynomial_add(certificate, polynomial_scale(halfspace, Rational(1, 7)))
    assert subtract(distance, certificate) == {}


def check_twirl_support():
    supported = 0
    for left, right in product(WORDS, repeat=2):
        differences = [left[position] - right[position] for position in range(3)]
        frequencies = [(differences[position] - differences[2]) % 3 for position in range(2)]
        averages_nonzero = all(phase_sum(frequency) == (3, 0) for frequency in frequencies)
        desired = left == right or (left == (0, 0, 0) and right == (1, 1, 1)) or (left == (1, 1, 1) and right == (0, 0, 0))
        assert averages_nonzero == desired
        supported += int(desired)
    assert supported == 10


def check_three_qubit_examples():
    gamma = Rational(11, 112)
    rho_diagonal = [Rational(1, 5)] * 4 + [Rational(0)] * 3 + [Rational(1, 5)]
    assert sum(rho_diagonal) == 1 and gamma < Rational(1, 5)
    parameters = [Rational(9, 10), Rational(199, 400), Rational(199, 400)]
    averaged_corner = Rational(119997, 1600000)
    assert all(0 <= probability <= 1 for probability in parameters)
    assert averaged_corner ** 2 == product_fraction(probability * (1 - probability) for probability in parameters)
    diagonal_tau = [Rational(5, 6) * value for value in twirled_diagonal(parameters)]
    diagonal_tau[-1] += Rational(1, 6)
    corner_tau = Rational(5, 6) * averaged_corner
    assert diagonal_tau == [Rational(value, 1920000) for value in [356409, 359991, 359991, 363609, 39601, 39999, 39999, 360401]]
    assert corner_tau == Rational(119997, 1920000)
    assert 9 * Rational(5, 54) + Rational(1, 6) == 1
    assert sum(diagonal_tau) == 1
    distance_tau = squared_distance(rho_diagonal, gamma, diagonal_tau, corner_tau)
    assert distance_tau == Rational(417965512477, 90316800000000)
    shape_minimum = Rational(109, 23520)
    assert shape_minimum - distance_tau == Rational(84926789, 12902400000000) > 0
    boundary_parameters = [Rational(9, 10), Rational(1, 2), Rational(1, 2)]
    diagonal_boundary = [Rational(5, 6) * value for value in twirled_diagonal(boundary_parameters)]
    diagonal_boundary[-1] += Rational(1, 6)
    assert diagonal_boundary == [Rational(3, 16)] * 4 + [Rational(1, 48)] * 3 + [Rational(3, 16)]
    assert squared_distance(rho_diagonal, gamma, diagonal_boundary, Rational(1, 16)) == shape_minimum
    shape_a, shape_b, lower_mass, eta_corner = Rational(5, 16), Rational(5, 8), Rational(1, 16), Rational(33, 512)
    assert shape_a + shape_b + lower_mass == 1
    assert eta_corner < shape_a / 2
    partial_transpose_minor = shape_b * lower_mass / 9 - eta_corner ** 2
    assert partial_transpose_minor > 0
    witness_bound = Rational(1, 2) - Rational(7, 15) * (shape_a + shape_b)
    assert witness_bound == Rational(1, 16)
    assert eta_corner - witness_bound == Rational(1, 512)
    eta_matrix = corner_matrix([shape_a / 2] + [shape_b / 3] * 3 + [lower_mass / 3] * 3 + [shape_a / 2], eta_corner)
    for qubit_position in range(3):
        partial_transpose = [[Rational(0) for column in range(8)] for row in range(8)]
        bit_mask = 1 << qubit_position
        for row, column in product(range(8), repeat=2):
            if bool(row & bit_mask) != bool(column & bit_mask):
                partial_transpose[row ^ bit_mask][column ^ bit_mask] = eta_matrix[row][column]
            else:
                partial_transpose[row][column] = eta_matrix[row][column]
        off_diagonal = [(row, column) for row, column in product(range(8), repeat=2) if row != column and partial_transpose[row][column]]
        assert len(off_diagonal) == 2
        block_first, block_second = off_diagonal[0]
        assert all(partial_transpose[position][position] >= 0 for position in range(8))
        assert partial_transpose[block_first][block_first] * partial_transpose[block_second][block_second] - eta_corner ** 2 == partial_transpose_minor
    diagonal_coefficients = [Rational(1, 15), Rational(1, 30), Rational(0), Rational(1, 15), Rational(0), Rational(3, 5), Rational(9, 10), Rational(0)]
    witness_norm_squared = Rational(1, 2) + sum(value ** 2 for value in diagonal_coefficients)
    assert witness_norm_squared == Rational(42, 25)
    eta_distance_lower = Rational(1, 512) ** 2 / witness_norm_squared
    assert eta_distance_lower == Rational(25, 11010048)
    small_gamma = Rational(1, 2048)
    assert 2 * small_gamma ** 2 < eta_distance_lower
    return {
        'rho_gamma': str(gamma),
        'restricted_minimum': str(shape_minimum),
        'tau_squared_distance': str(distance_tau),
        'strict_gap': str(shape_minimum - distance_tau),
        'eta_partial_transpose_minor': str(partial_transpose_minor),
        'eta_separability_inequality_violation': str(eta_corner - witness_bound),
        'eta_distance_lower_bound': str(eta_distance_lower),
        'small_gamma_distance_upper_bound': str(2 * small_gamma ** 2),
    }


def check_two_qubit_examples():
    check_isotropic_product_mixture()
    target = [Rational(1, 3), Rational(1, 3), Rational(0), Rational(1, 3)]
    candidate = [Rational(7, 24), Rational(1, 3), Rational(1, 12), Rational(7, 24)]
    averaged = twirled_diagonal([Rational(2, 3), Rational(1, 3)])
    mixture = [Rational(3, 4) * entry for entry in averaged]
    mixture[0] += Rational(1, 8)
    mixture[-1] += Rational(1, 8)
    assert mixture == candidate
    assert product_fraction([Rational(2, 3) * Rational(1, 3)] * 2) == Rational(2, 9) ** 2
    assert Rational(3, 4) * Rational(2, 9) == Rational(1, 6)
    for left, right in product(tuple(product(range(2), repeat=2)), repeat=2):
        frequency = left[0] - right[0] - left[1] + right[1]
        desired = left == right or (left == (0, 0) and right == (1, 1)) or (left == (1, 1) and right == (0, 0))
        assert (phase_sum(frequency) == (3, 0)) == desired
    upper_bound = squared_distance(target, Rational(1, 4), candidate, Rational(1, 6))
    assert upper_bound == Rational(7, 288)
    assert Rational(7, 12) - Rational(1, 12) == Rational(1, 2)
    spin_flip = [[0, 0, 0, -1], [0, 0, 1, 0], [0, 1, 0, 0], [-1, 0, 0, 0]]
    target_matrix = corner_matrix(target, Rational(1, 4))
    flipped_target = matrix_multiply(matrix_multiply(spin_flip, target_matrix), spin_flip)
    target_product = matrix_multiply(target_matrix, flipped_target)
    assert characteristic_coefficients(target_product) == root_coefficients([Rational(7, 12) ** 2, Rational(1, 12) ** 2, 0, 0])
    for concurrence in [Rational(1, 2), Rational(2, 5)]:
        bell_weight = (1 + concurrence) / 2
        assert bell_weight - 3 * (1 - bell_weight) / 3 == concurrence
        assert upper_bound < concurrence ** 2 / 3
        other_weight = (1 - bell_weight) / 3
        isotropic_matrix = corner_matrix([(bell_weight + other_weight) / 2, other_weight, other_weight, (bell_weight + other_weight) / 2], (bell_weight - other_weight) / 2)
        assert matrix_multiply(matrix_multiply(spin_flip, isotropic_matrix), spin_flip) == isotropic_matrix
        assert characteristic_coefficients(isotropic_matrix) == root_coefficients([bell_weight] + [other_weight] * 3)
        boundary = [Rational(1, 3), Rational(1, 6), Rational(1, 6), Rational(1, 3)]
        assert squared_distance([isotropic_matrix[position][position] for position in range(4)], isotropic_matrix[0][-1], boundary, Rational(1, 6)) == concurrence ** 2 / 3
    return {
        'x_state_concurrence': '1/2',
        'x_state_distance_upper_bound': str(upper_bound),
        'equal_concurrence_isotropic_distance': '1/12',
        'smaller_concurrence_isotropic_distance': '4/75',
        'concurrence_spectra': 'Exact characteristic polynomials for the spin-flipped X-state product and the Bell-isotropic matrices',
        'isotropic_boundary': 'Exact equal mixture of six pure product projectors',
    }


def main():
    check_twirl_support()
    check_square_completion()
    report = {
        'arithmetic': 'exact rational arithmetic and coefficient comparison',
        'phase_support': 'all 64 three-qubit matrix positions and all 16 two-qubit positions',
        'square_completion': 'identically zero difference in four polynomial variables',
        'three_qubit': check_three_qubit_examples(),
        'two_qubit': check_two_qubit_examples(),
        'scope': 'Finite algebraic checks supplement the product-state inequalities and continuous-parameter proofs in note.tex.',
    }
    text = json.dumps(report, indent=2) + '\n'
    Path('verification.json').write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
