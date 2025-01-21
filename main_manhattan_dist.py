# Program to compute the dot product of two secret vectors in MPC
from mpyc.runtime import mpc
import random
import numpy as np

def main():
    # Initialize the MPC
    mpc.run(mpc.start())
    party = mpc.pid

    orig_a = [random.randint(0, 4) for _ in range(1000)]
    orig_b = [random.randint(0, 4) for _ in range(1000)]

    # Secure integer vectors
    int_a = [mpc.SecInt(8)(a) for a in orig_a]
    int_b = [mpc.SecInt(8)(b) for b in orig_b]

    # Input the secret integer vectors for each party
    sec_a = mpc.input(int_a, senders=0)
    sec_b = mpc.input(int_b, senders=0)

    # Compute the vector differences
    vec_diff = mpc.vector_sub(sec_a, sec_b)
    
    vec_abs = [None] * len(vec_diff)
    for i in range(len(vec_diff)):
        vec_abs[i] = mpc.abs(vec_diff[i])
        
    manhattan_dist = mpc.run(mpc.output(mpc.sum(vec_abs), receivers=0))
    
    if party == 0:
        print(f"\nManhattan distance from the secrets: {manhattan_dist}")
        print("\nReal Manhattan distance: ", np.sum(np.abs(np.subtract(orig_a, orig_b))))
    
    # Compute the Manhattan distance
    # manhattan_dist = mpc.run(mpc.sum(mpc.abs(vec_diff)))
    

    # # Reconstructed vectors
    # rec_a = mpc.run(mpc.output(sec_a, receivers=[0, 1]))
    # rec_b = mpc.run(mpc.output(sec_b, receivers=[0, 1]))

    # print(f"\nDot product from the secrets: {dot_product}")
    # print("\nReal dot product: ", np.dot(rec_a, rec_b))

    # # Reconstructed vectors
    # rec_a = mpc.run(mpc.output(sec_a, receivers=[0, 1]))
    # rec_b = mpc.run(mpc.output(sec_b, receivers=[0, 1]))

    # # Compare the secrets
    # if party == 0:
    #     if orig_a == rec_a:
    #         print("\nSecret vector of P0 is correct.")
    #     else:
    #         print("\nSecret vector of P0 is incorrect.")
    # if party == 1:
    #     if orig_b == rec_b:
    #         print("\nSecret vector of P1 is correct.")
    #     else:
    #         print("\nSecret vector of P1 is incorrect.")

    # Terminate the MPC
    mpc.run(mpc.shutdown())

########### Main Program ###########
if __name__ == "__main__":
    main()
