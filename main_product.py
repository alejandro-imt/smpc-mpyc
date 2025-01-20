# Program to compute product of two secret values in MPC
from mpyc.runtime import mpc
import random

def main():
    party = mpc.pid
    orig_a = random.randint(0, 100)
    
    orig_b = random.randint(0, 100)
    
    # Starting the MPC runtime
    mpc.run(mpc.start())

    secret_a = mpc.input(mpc.SecInt(7)(orig_a), senders=0)
    secret_b = mpc.input(mpc.SecInt(7)(orig_b), senders=0)
    
    # Compute the product
    prod = mpc.run(mpc.output(mpc.mul(secret_a, secret_b), receivers=0))

    # Terminating the MPC runtime
    mpc.run(mpc.shutdown())
    
    # Show the product if it exists
    if prod is not None:
        print(f"Product of a={orig_a} and b={orig_b} according to P{party}: {prod}")
        print(f"Real product of a={orig_a} and b={orig_b}: {orig_a * orig_b}")
    else:
        print(f"No output specified for P{party}")

if __name__ == "__main__":
    main()
