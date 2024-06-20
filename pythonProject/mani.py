import csv
import math
import random


def decimal_to_binary_list(decimal_number):
    return [int(bit) for bit in bin(decimal_number)[2:]]

generator_polynomials = {
    (7, 4, 3): decimal_to_binary_list(11),
    (7, 3, 4): decimal_to_binary_list(35),

    (15, 11, 3): decimal_to_binary_list(23),
    (15, 10, 4): decimal_to_binary_list(65),
    (15, 7, 5): decimal_to_binary_list(721),
    (15, 6, 6): decimal_to_binary_list(1163),
    (15, 5, 7): decimal_to_binary_list(2467),
    (15, 4, 8): decimal_to_binary_list(7531),

    (17, 9, 5): decimal_to_binary_list(727),
    (17, 8, 6): decimal_to_binary_list(1171),

    (21, 16, 3): decimal_to_binary_list(61),
    (21, 15, 4): decimal_to_binary_list(123),
    (21, 12, 5): decimal_to_binary_list(1663),
    (21, 11, 6): decimal_to_binary_list(2531),
    (21, 10, 5): decimal_to_binary_list(5031),
    (21, 9, 8): decimal_to_binary_list(17053),
    (21, 5, 10): decimal_to_binary_list(214537),

    (23, 12, 7): decimal_to_binary_list(5343),
    (23, 11, 8): decimal_to_binary_list(17445),

    (25, 5, 5): decimal_to_binary_list(4102041),
    (25, 4, 10): decimal_to_binary_list(14306143),

    (27, 9, 3): decimal_to_binary_list(1001001),
    (27, 8, 6): decimal_to_binary_list(3003003),

    (31, 26, 3): decimal_to_binary_list(45),
    (31, 25, 4): decimal_to_binary_list(157),
    (31, 21, 5): decimal_to_binary_list(3551),
    (31, 16, 7): decimal_to_binary_list(107657),
    (31, 15, 8): decimal_to_binary_list(310361),
    (31, 11, 11): decimal_to_binary_list(5423325),
    (31, 6, 15): decimal_to_binary_list(313365047),
    (31, 5, 16): decimal_to_binary_list(535437151),

    (33, 23, 3): decimal_to_binary_list(3043),
    (33, 22, 6): decimal_to_binary_list(5145),
    (33, 21, 3): decimal_to_binary_list(17537),

    (45, 22, 8): decimal_to_binary_list(63335065),
    (45, 21, 3): decimal_to_binary_list(110111011),
    (45, 20, 6): decimal_to_binary_list(330333033),

    (47, 24, 11): decimal_to_binary_list(43073357),
    (47, 23, 12): decimal_to_binary_list(145115461),

    (49, 28, 3): decimal_to_binary_list(10040001),
    (49, 27, 4): decimal_to_binary_list(30140003),
    (49, 21, 4): decimal_to_binary_list(2010040001),

    (51, 43, 3): decimal_to_binary_list(433),
    (51, 35, 5): decimal_to_binary_list(266251),
    (51, 33, 6): decimal_to_binary_list(1403537),
    (51, 32, 6): decimal_to_binary_list(2020213),
    (51, 27, 9): decimal_to_binary_list(134531443),
    (51, 26, 10): decimal_to_binary_list(242245105),
    (51, 24, 10): decimal_to_binary_list(1762776477),
    (51, 19, 14): decimal_to_binary_list(50112257553),
    (51, 18, 14): decimal_to_binary_list(170336760675),
    (51, 10, 18): decimal_to_binary_list(62066722733023),

    (33, 20, 6): decimal_to_binary_list(20741),
    (33, 13, 10): decimal_to_binary_list(4172741),
    (33, 12, 10): decimal_to_binary_list(14217043),
    (33, 11, 11): decimal_to_binary_list(25456465),
    (33, 10, 12): decimal_to_binary_list(76563537),

    (35, 25, 4): decimal_to_binary_list(2565),
    (35, 24, 4): decimal_to_binary_list(7637),
    (35, 23, 3): decimal_to_binary_list(13627),
    (35, 20, 6): decimal_to_binary_list(147257),
    (35, 19, 6): decimal_to_binary_list(251761),
    (35, 18, 4): decimal_to_binary_list(735235),
    (35, 17, 6): decimal_to_binary_list(1532051),
    (35, 16, 7): decimal_to_binary_list(2433361),
    (35, 15, 8): decimal_to_binary_list(7455423),
    (35, 11, 5): decimal_to_binary_list(143676743),
    (35, 10, 10): decimal_to_binary_list(244303045),

    (39, 27, 3): decimal_to_binary_list(13617),
    (39, 26, 6): decimal_to_binary_list(34221),
    (39, 25, 3): decimal_to_binary_list(55263),
    (39, 24, 6): decimal_to_binary_list(167725),
    (39, 15, 10): decimal_to_binary_list(153651205),
    (39, 14, 10): decimal_to_binary_list(274373617),
    (39, 13, 12): decimal_to_binary_list(423136633),

    (41, 21, 9): decimal_to_binary_list(6647133),
    (41, 20, 10): decimal_to_binary_list(13351355),

    (43, 29, 6): decimal_to_binary_list(64213),
    (43, 28, 6): decimal_to_binary_list(134635),
    (43, 15, 13): decimal_to_binary_list(2607043415),
    (43, 14, 14): decimal_to_binary_list(7211144427),

    (45, 35, 4): decimal_to_binary_list(2113),
    (45, 29, 5): decimal_to_binary_list(230213),
    (45, 25, 5): decimal_to_binary_list(7217531),
    (45, 24, 6): decimal_to_binary_list(11620753),
    (45, 22, 7): decimal_to_binary_list(21113023),

    (55, 35, 5): decimal_to_binary_list(7164555),
    (55, 34, 8): decimal_to_binary_list(11235667),

    (57, 39, 3): decimal_to_binary_list(1341035),
    (57, 38, 6): decimal_to_binary_list(3443047),

    (63, 57, 3): decimal_to_binary_list(103),
    (63, 56, 4): decimal_to_binary_list(305),
    (63, 51, 5): decimal_to_binary_list(12471),
    (63, 45, 7): decimal_to_binary_list(1701317),
    (63, 39, 9): decimal_to_binary_list(166623567),
    (63, 36, 11): decimal_to_binary_list(1033500423),
    (63, 30, 13): decimal_to_binary_list(157464165547),
    (63, 24, 15): decimal_to_binary_list(17323260404441),
    (63, 18, 21): decimal_to_binary_list(1363026512351725),
    (63, 16, 23): decimal_to_binary_list(6331141367235453),
    (63, 10, 27): decimal_to_binary_list(472622305527250155),
    (63, 4, 31): decimal_to_binary_list(5231045543503271737),
}
def find_generator_polynomial(n, k, d):
    return generator_polynomials.get((n, k, d))

def poly_multiply(p1, p2):
    result = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] ^= p1[i] & p2[j]
    return result

def poly_divide(dividend, divisor):
    output = list(dividend)
    for i in range(len(dividend) - len(divisor) + 1):
        if output[i]:
            for j in range(1, len(divisor)):
                output[i + j] ^= divisor[j]
    return output[-(len(divisor)-1):]


def poly_add(bin1, bin2):
    def binary_to_decimal(binary_list):
        return int(''.join(map(str, binary_list)), 2)

    def decimal_to_binary(decimal_num):
        return list(map(int, bin(decimal_num)[2:]))

    num1 = binary_to_decimal(bin1)
    num2 = binary_to_decimal(bin2)

    result_decimal = num1 + num2

    return decimal_to_binary(result_decimal)

def hamming_weight(vector):
    return sum(1 for bit in vector if bit)


def rotate_right(vec):
    return [vec[-1]] + vec[:-1]


def rotate_left(vec):
    return vec[1:] + [vec[0]]


def correct_and_rotate(received, syndrome, rotations):
    corrected = poly_add_decode(received, syndrome)
    for _ in range(rotations):
        corrected = rotate_left(corrected)
    return corrected

def poly_add_decode(p1, p2):
    if len(p1) < len(p2):
        p1, p2 = p2, p1
    p2 = [0] * (len(p1) - len(p2)) + p2
    return [bit1 ^ bit2 for bit1, bit2 in zip(p1, p2)]


def decode_received_vector(received, generator, t):
    print("========================================================================")
    print("DEKODOWANIE")
    syndrome = poly_divide(received, generator)
    print("Syndrom: ", syndrome)
    print("Waga syndromu:", hamming_weight(syndrome))
    if hamming_weight(syndrome) == 0:
        return received

    i = 0
    k = len(received) - len(generator) + 1
    print("T:", t)
    print("K:", k)
    while True:
        weight = hamming_weight(syndrome)

        if weight <= t:
            print("Prawo")
            corrected = poly_add_decode(received, syndrome)
            for _ in range(i):
                corrected = rotate_left(corrected)
            return corrected

        print("Lewo")
        received = rotate_right(received)
        i += 1
        print('i ', i)

        syndrome = poly_divide(received, generator)

        if i == k:
            return received
            
    print("DEKODOWANIE")
    print("========================================================================")

def cyclic_encode(n, k, msg, generator):
    print("========================================================================")
    print("KODOWANIE")
    r = n - k
    msg_shifted = msg + [0] * r
    print("Przesunieta wiadomosc:", msg_shifted)
    remainder = poly_divide(msg_shifted, generator)
    print("Reszta z dzieleni:", remainder)
    encoded = poly_add(msg_shifted, remainder)

    print("Zakodowana:", encoded)
    print("Dlugosc zakodowanej wiadomosci:", len(encoded))

    if len(encoded) < n :
        encoded = [0] * (n-len(encoded)) + encoded

    print("Kodowanie zakonczone")
    print("========================================================================")


    return encoded
def introduce_errors(encoded_msg, error_positions):
    for pos in error_positions:
        encoded_msg[len(encoded_msg) - pos] ^= 1
    return encoded_msg


import random
import math

def find_generator_polynomial(n, k, d):
    return [1] * (n - k + 1)

def cyclic_encode(n, k, msg, generator):
    return msg + [0] * (n - k)

def introduce_errors(codedmsg, error_position):
    for pos in error_position:
        codedmsg[pos-1] ^= 1
    return codedmsg

def decode_received_vector(codedwitherrors, generator, t):
    return codedwitherrors

def hamming_weight(error_position):
    return len(error_position)

import random
import math

def find_generator_polynomial(n, k, d):
    return [1] * (n - k + 1)

def cyclic_encode(n, k, msg, generator):
    return msg + [0] * (n - k)

def introduce_errors(encoded_msg, error_positions):
    for pos in error_positions:
        encoded_msg[pos] ^= 1  
    return encoded_msg

def decode_received_vector(codedwitherrors, generator, t):
    return codedwitherrors

def hamming_weight(error_position):
    return len(error_position)

def test_decoder():
    polynomials_to_test = [
        (7, 4, 3),
        (15, 11, 3),
        (25, 5, 5),
        (45, 21, 3),
        (51, 10, 18),
        (63, 36, 11)
    ]

    def count_error_types(original, decoded):
        single_errors = 0
        double_errors = 0
        group_errors = 0

        i = 0
        while i < len(original):
            if original[i] != decoded[i]:
                start = i
                while i < len(original) and original[i] != decoded[i]:
                    i += 1
                error_length = i - start
                if error_length == 1:
                    single_errors += 1
                elif error_length == 2:
                    double_errors += 1
                else:
                    group_errors += 1
            else:
                i += 1

        return single_errors, double_errors, group_errors

    with open("output.csv", "w", newline='') as csvfile:
        fieldnames = ['Polynomial', 'Msg', 'Coded', 'Code with Errors', 'Decoded', 'Errors', 'Single Errors', 'Double Errors', 'Group Errors']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for (n, k, d) in polynomials_to_test:
            generator = find_generator_polynomial(n, k, d)
            m = math.log2(n + 1)
            t = int(m - 1) - 1

            num_messages = min(100, 2 ** k)
            for _ in range(num_messages):
                msg = [random.randint(0, 1) for _ in range(k)]
                codedmsg = cyclic_encode(n, k, msg, generator)

                max_errors = n - k
                num_errors = random.randint(t + 1, max_errors)
                error_position = random.sample(range(n - max_errors, n), num_errors)

                codedwitherrors = introduce_errors(codedmsg[:], error_position)
                decoded = decode_received_vector(codedwitherrors, generator, t)

                single_errors, double_errors, group_errors = count_error_types(codedmsg, decoded)

                writer.writerow({
                    'Polynomial': f'[{n}, {k}, {d}]',
                    'Msg': msg,
                    'Coded': codedmsg,
                    'Code with Errors': codedwitherrors,
                    'Decoded': decoded,
                    'Errors': num_errors,
                    'Single Errors': single_errors,
                    'Double Errors': double_errors,
                    'Group Errors': group_errors
                })



def main():
    test_decoder()
    n = int(input("Podaj n (długość słowa do zakodowania): "))
    k = int(input("Podaj k (ilość elementów informacyjnych): "))
    d = int(input("Podaj d (odległość minimalna): "))
    m = math.log2(n + 1)
    t = int(m - 1) - 1
    generator = find_generator_polynomial(n, k, d)

    if generator is None:
        print("Nie znaleziono odpowiedniego wielomianu generującego.")
        return

    choice = input(
        "Wybierz opcję: 1. Zakodowanie wiadomości, 2. Dekodowanie wiadomości, 3. Zakodowanie i Dekodowanie wiadomości, 4. Testowanie dekodera, 5. Analiza:  ")
    if choice == '1':
        msg = [int(input(f"Podaj bit {i+1} wiadomości: ")) for i in range(k)]
        encoded_msg = cyclic_encode(n, k, msg, generator)
        print("Zakodowana wiadomość:", encoded_msg)
    elif choice == '2':
        received_msg = [int(input(f"Podaj bit {i+1} otrzymanej wiadomości: ")) for i in range(n)]
        decoded_msg = decode_received_vector(received_msg, generator, t)
        if decoded_msg is not None:
            print("Zdekodowana wiadomość:", decoded_msg)
        else:
            print("Nie udało się zdekodować wiadomości.")
    elif choice == '3':
        msg = [int(input(f"Podaj bit {i+1} wiadomości: ")) for i in range(k)]
        encoded_msg = cyclic_encode(n, k, msg, generator)
        print("Zakodowana wiadomość:", encoded_msg)
        decoded_msg = decode_received_vector(encoded_msg, generator, t)
        if decoded_msg is not None:
            print("Zdekodowana wiadomość:", decoded_msg)
        else:
            print("Nie udało się zdekodować wiadomości.")
    elif choice == '4':
        msg = [int(input(f"Podaj bit {i + 1} wiadomości: ")) for i in range(k)]
        encoded_msg = cyclic_encode(n, k, msg, generator)
        print("Zakodowana wiadomość:", encoded_msg)

        error_positions = [int(x) for x in
                           input("Podaj pozycje bitów, które mają zostać zmienione (oddzielone spacjami): ").split()]
        received_msg = introduce_errors(encoded_msg, error_positions)
        print("Wiadomość z błędami:", received_msg)

        decoded_msg = decode_received_vector(received_msg, generator, t)
        if decoded_msg is not None:
            print("Zdekodowana wiadomość:", decoded_msg)
        else:
            print("Nie udało się zdekodować wiadomości.")
    elif choice == '5':
        test_decoder()



if __name__ == "__main__":
    main()
