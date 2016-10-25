
from cost_function_definition import f, f_prime, f_double_prime


def minimize(f0, f1, f2, guess, epsilon):
    firstprime = f1(guess)
    secondprime = f2(guess)

    delta = -f1(guess)/f2(guess)
    old_guess = guess
    new_guess = old_guess - f1(old_guess)/f2(old_guess)
    if f_double_prime(guess) != 0:
        while abs(delta) > epsilon:
            old_guess = new_guess
            new_guess = old_guess - f1(old_guess)/f2(old_guess)
            delta = -f1(old_guess)/f2(old_guess)
        print(new_guess)
    else:
        print("The denominator is 0")
minimize(f, f_prime, f_double_prime, 0.0, 0.000001)