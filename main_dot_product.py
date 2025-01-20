# Program to compute the dot product of two secret vectors in MPC
from mpyc.runtime import mpc
import random
import numpy as np

def main():
    # Initialize the MPC
    mpc.run(mpc.start())
    party = mpc.pid

    orig_a = [random.randint(0, 100) for _ in range(1000000)]
    orig_b = [random.randint(0, 100) for _ in range(1000000)]

    # Secure integer vectors
    int_a = [mpc.SecInt(7)(a) for a in orig_a]
    int_b = [mpc.SecInt(7)(b) for b in orig_b]

    # Input the secret integer vectors for each party
    sec_a = mpc.input(int_a, senders=0)
    sec_b = mpc.input(int_b, senders=1)

    # if party == 0:
    #     print(f"\nOriginal secret vector of P0: {orig_a}")
    # elif party == 1:
    #     print(f"\nOriginal secret vector of P1: {orig_b}")

    # Compute the dot product
    dot_product = mpc.run(mpc.output(mpc.in_prod(sec_a, sec_b)))

    # Reconstructed vectors
    rec_a = mpc.run(mpc.output(sec_a, receivers=[0, 1]))
    rec_b = mpc.run(mpc.output(sec_b, receivers=[0, 1]))

    print(f"\nDot product from the secrets: {dot_product}")
    print("\nReal dot product: ", np.dot(rec_a, rec_b))

    # Reconstructed vectors
    rec_a = mpc.run(mpc.output(sec_a, receivers=[0, 1]))
    rec_b = mpc.run(mpc.output(sec_b, receivers=[0, 1]))

    # Compare the secrets
    if party == 0:
        if orig_a == rec_a:
            print("\nSecret vector of P0 is correct.")
        else:
            print("\nSecret vector of P0 is incorrect.")
    if party == 1:
        if orig_b == rec_b:
            print("\nSecret vector of P1 is correct.")
        else:
            print("\nSecret vector of P1 is incorrect.")
        
    # Terminate the MPC
    mpc.run(mpc.shutdown())

if __name__ == "__main__":
    main()
