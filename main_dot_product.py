# Program to compute the dot product of two secret vectors in MPC
from mpyc.runtime import mpc
import random
import numpy as np
import time

def main():
    # Initialize the MPC
    mpc.run(mpc.start())
    party = mpc.pid

    orig_a = [random.randint(0, 10) for _ in range(260000)]
    orig_b = [random.randint(0, 10) for _ in range(260000)]

    tic = time.process_time()
    
    # Secure integer vectors
    int_a = [mpc.SecInt(16)(a) for a in orig_a]
    int_b = [mpc.SecInt(16)(b) for b in orig_b]

    # Input the secret integer vectors for each party
    sec_a = mpc.input(int_a, senders=0)
    sec_b = mpc.input(int_b, senders=0)

    # Compute the dot product
    dot_product = mpc.run(mpc.output(mpc.in_prod(sec_a, sec_b)))
    
    elapsed_time = time.process_time() - tic

    # Reconstructed vectors
    rec_a = mpc.run(mpc.output(sec_a, receivers=0))
    rec_b = mpc.run(mpc.output(sec_b, receivers=0))

    # Compare the secrets
    if party == 0:
        real_dot_product = np.dot(rec_a, rec_b)
        if dot_product != real_dot_product:
            print("\nERROR")
        
    # Terminate the MPC
    mpc.run(mpc.shutdown())
    
    return elapsed_time

if __name__ == "__main__":
    num_tests = 10
    elapsed_times = []
    for _ in range(num_tests):
        elapsed_time = main()
        elapsed_times.append(elapsed_time)
    print(f"\nAverage elapsed time: {sum(elapsed_times)/num_tests} seconds")
