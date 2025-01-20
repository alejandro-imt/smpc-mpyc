# Program to compute the absolute differente of two secrets in MPC
from mpyc.runtime import mpc
import random
import numpy as np

def main():
    # Initialize the MPC
    mpc.run(mpc.start())
    party = mpc.pid

    orig_a = random.randint(0, 100)
    orig_b = random.randint(0, 100)

    # Secure integer vectors
    int_a = mpc.SecInt(7)(orig_a)
    int_b = mpc.SecInt(7)(orig_b)

    # Input the secret integer vectors for each party
    sec_a = mpc.input(int_a, senders=0)
    sec_b = mpc.input(int_b, senders=1)

    if party == 0:
        print(f"\nOriginal secret of P0: {orig_a}")
    elif party == 1:
        print(f"\nOriginal secret of P1: {orig_b}")

    # Compute the absolute difference
    abs_diff = mpc.run(mpc.output(mpc.abs(sec_a - sec_b)))
    
    # Reconstructed values
    rec_a = mpc.run(mpc.output(sec_a, receivers=[0, 1]))
    rec_b = mpc.run(mpc.output(sec_b, receivers=[0, 1]))
    
    # Compute the real absolute difference
    real_abs_diff = np.abs(rec_a - rec_b)

    print(f"\nAbsolute difference from the secrets: {abs_diff}")
    print("\nReal absolute difference: ", real_abs_diff)

    # Compare the results
    if abs_diff == real_abs_diff:
        print("\nAbsolute difference is correct.")
    else:
        print("\nERROR: Absolute difference is incorrect.")

    # Terminate the MPC
    mpc.run(mpc.shutdown())

if __name__ == "__main__":
    main()
