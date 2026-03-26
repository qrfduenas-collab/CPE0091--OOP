def generate_truthtable(number_of_variables = 3):
    total_combinations = 2**number_of_variables
    combinations_list = []
    for i in range(total_combinations):
        bin_equivalent = bin(i)[2:]
        while len(bin_equivalent) < number_of_variables:
            bin_equivalent = "0" + bin_equivalent
        combinations_list.append(tuple(int(val) for val in bin_equivalent))
    return combinations_list

def evaluate_propositional_logic(c_list):
    print("A B C | Output")
    for row in c_list:
        A, B, C = row
        result = (A and B) or C
        print(A, B, C, "/", int(result))

print(generate_truthtable())
evaluate_propositional_logic(generate_truthtable(3))